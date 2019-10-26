from os import cpu_count
from time import time

from tqdm import tqdm

from pool_proc import Pool

n_list = 10000


def f(x):
    return x**x


def single_processor():
    t_start = time()
    results = list()
    pbar = tqdm(desc='Single', total=n_list, ascii=True)
    for x in range(n_list):
        results.append(f(x))
        pbar.update(1)
    pbar.close()
    print(f'It took {round(time()-t_start, 2)} sec')
    print(len(results))


def multi_processor():
    t_start = time()
    results = list()
    pool = Pool(n_processes=cpu_count() - 1, save_results=True)
    pbar = tqdm(desc='Multi', total=n_list, ascii=True)
    for x in range(n_list):
        pool.add_task(f, x)
        pbar.update(1)
    pool.wait_completion()
    response = pool.get_results()
    pbar.close()
    for elem in response:
        results.append(elem)
    print(f'It took {round(time()-t_start, 2)} sec')
    print(len(results))
    pool.terminate()


if __name__ == "__main__":
    single_processor()
    multi_processor()
