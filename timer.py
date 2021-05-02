import time


def timer(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        res = func(*args, **kwargs)
        t1 = time.time()
        print(f"time: {t1-t0}")
        return res
    return wrapper