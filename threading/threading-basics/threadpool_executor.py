import concurrent.futures
from utils import do_work


# results result in order of task completion
def run_using_threadpool_executor_submit(seconds):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_objs = [executor.submit(do_work, sec) for sec in seconds]

    for f in concurrent.futures.as_completed(future_objs):
        print(f.result())


# returns results in order of initiating task
def run_using_threadpool_executor_map(seconds):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(do_work, seconds)

    for res in results:
        print(res)


if __name__ == "__main__":
    import time

    start_time = time.perf_counter()
    run_using_threadpool_executor_map([3, 4, 5, 2, 1])
    finish_time = time.perf_counter()

    print(f'Map::Finished in {round(finish_time - start_time, 3)} second(s)')

    start_time = time.perf_counter()
    run_using_threadpool_executor_submit([3, 4, 5, 2, 1])
    finish_time = time.perf_counter()

    print(f'Submit::Finished in {round(finish_time - start_time, 3)} sec(s)')
