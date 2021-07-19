# pythread
Make any script multi threaded.


## Usage

1. First create a handler function in your code.
```python
def client(*args):
    print("Hello,", args)
```

2. Create an instance of the PyThread class.
```python
pyThread = PyThread(handler=client, threads=100, verbose=True, progress=False, debug=False)
```

3. Then you can start adding to it.
```python
pyThread.add_task("test")
pyThread.add_task("test", "task")
pyThread.add_task(["test", "task"])
pyThread.add_task(("test", "task"))
pyThread.add_task({1: "test", 2: "task"})
```

4. Finally, we can tell it when we're done adding so that it can exit as soon as all the tasks are finished.
```python
pyThread.stop()
```

## Arguments

* **handler**   -   The handler function that will be run for each tasks
* **threads**  -   Maximum number of threads to run in parallel
* **progress**  -   Show a progress bar to display the status
* **debug**  -   Enable logging from the module
* **verbose**  -   Provide verbose logging from the module
