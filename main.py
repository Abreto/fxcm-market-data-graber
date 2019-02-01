#!/usr/bin/env python3

import os, time
from multiprocessing import Pool
import config

def handler(periodicity, instrument, year):
    taskname = '/{}/{}/{}'.format(periodicity, instrument, year)
    print('Handle task {} ({})'.format(taskname, os.getpid()))
    
    start_time = time.time()
    pass
    end_time = time.time()
    print('Task {} runs {:.2f} seconds.'.format(taskname, end_time - start_time))

if __name__ == '__main__':
    print('Pulling begins')
    p = Pool(config.workers)
    for pd in config.periodicity:
        for i in config.instruments:
            for y in config.years:
                p.apply_async(handler, args=(pd, i, y))
    
    print('Tasks distributed, waiting for all tasks done...')
    p.close()
    p.join()
    print('All tasks done.')
