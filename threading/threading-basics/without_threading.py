from utils import do_work


def run_without_thread(seconds):
    results = [do_work(sec) for sec in seconds]

    for res in results:
        print(res)


if __name__ == "__main__":
    import time

    start_time = time.perf_counter()
    run_without_thread([3, 4, 5, 2, 1])
    finish_time = time.perf_counter()

    print(f'Finished in {round(finish_time - start_time, 3)} second(s)')
