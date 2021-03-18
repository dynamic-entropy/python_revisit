import time


def do_work(sec, ret=True):
    print(f'Starting ... Time required  = {sec} second(s)')
    time.sleep(sec)

    if ret:
        return f'Completed ... Time took {sec} seconds'
    else:
        print(f'Completed ... Time took {sec} seconds')
