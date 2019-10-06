from threading import Lock
class Foo:
    def __init__(self):
        self.firstJobLock = Lock()
        self.secondJobLock = Lock()
        self.firstJobLock.acquire()
        self.secondJobLock.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstJobLock.release() #release first job lock in order to let second job execute
        
    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.firstJobLock: #use context manager to acquire/release lock
            # acquires the first Job Lock in order to execute printSecond()
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
        self.secondJobLock.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.secondJobLock:
            # acquires the second Job Lock in order to execute printThird()
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
