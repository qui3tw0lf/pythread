import time
import requests
from pythread import PyThread


def client(*args):
    # print("Hello, client!", args)
    req = requests.get('https://www.google.com')
    # print(req.status_code)


def main():
    pyThread = PyThread(handler=client, threads=100, verbose=True, progress=False)
    for x in range(500):
        pyThread.add_task("hello %d" % x)

    for x in range(500):
        pyThread.add_task("world %d" % x)
    pyThread.stop()


if __name__ == '__main__':
    main()
