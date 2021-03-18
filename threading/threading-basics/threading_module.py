import threading
from utils import do_work


def run_using_threading_module(seconds):
    threads = [threading.Thread(target=do_work, args=[sec, False])
               for sec in seconds]
    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    import time

    start_time = time.perf_counter()
    run_using_threading_module([3, 4, 5, 2, 1])
    finish_time = time.perf_counter()

    print(f'Finished in {round(finish_time - start_time, 3)} sec(s)')
