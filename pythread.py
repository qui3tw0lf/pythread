import time
import queue
import logging
import threading
import progressbar


class PyThread:

    def __init__(self, handler, threads=10, verbose=False, debug=False, progress=True):
        if not debug:
            logging.basicConfig(level=logging.ERROR)
        elif verbose:
            logging.basicConfig(level=logging.DEBUG)
        logging.debug("Thread manager started.")

        self.KEEP_RUNNING = True
        self.QUEUE = queue.Queue(threads)
        self.LOCK = threading.Lock()
        self.MAX = threads
        self.HANDLER = handler
        self.HANDLER_MOD = self.handler_mod
        self.TOTAL = 0
        self.BAR = progressbar.ProgressBar(max_value=progressbar.UnknownLength)

        # Main loop
        thread_main = threading.Thread(target=self.start, args=())
        thread_main.start()


    def handler_mod(self, *args):
        def mod(args):
            print("Running")
            self.HANDLER(args)
        return mod


    def start(self):
        logging.debug("Main loop started")
        while True:
            size = self.QUEUE.qsize()
            if not self.KEEP_RUNNING and not size:
                logging.warning("Quitting")
                break
            tmp_size = size
            if tmp_size > self.MAX:
                tmp_size = self.MAX
            if tmp_size:
                logging.debug("Getting %d / %d" % (tmp_size, size))
            for x in range(tmp_size):
                # with self.LOCK:
                # logging.debug("Getting %d" % x)
                tmp_task = self.QUEUE.get()
                logging.info("[*] Exec: " + str(tmp_task))
                tmp_thread = threading.Thread(target=self.HANDLER, args=(tmp_task,))
                tmp_thread.start()
            time.sleep(0.5)


    def stop(self):
        self.KEEP_RUNNING = False
        logging.debug("Stopped")


    def add_task(self, *task):
        self.TOTAL += 1
        logging.debug("[+] Task: " + str(task))
        self.QUEUE.put(task)
        self.BAR.update(self.TOTAL)
