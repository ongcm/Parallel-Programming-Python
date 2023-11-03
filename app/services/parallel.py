import math
import numpy as np
from timebudget import timebudget
from multiprocessing import Pool, Process
import time
import main
import os

output_list = []
process_list = []
random_numbers = []

def startTimer():
    start = time.time()
    return start

def endTimer():
    end = time.time()
    return end

def returnRuntime(start, end):
    return end-start

def generate_random_numbers(num):
    return [int(1e5+i) for i in range(num)]

def parallel_operation(data):
    list_fibo = [0, 1, 1]
    for i2 in range(data-3):
        list_fibo.append(list_fibo[-1]+list_fibo[-2])
    process_list.append(os.getpid())
    return list_fibo[-1]

def runProgram(processes_count, num_numbers):
    random_numbers = generate_random_numbers(num_numbers)
    start = startTimer()
    output_list = []
    with Pool(processes_count) as pool:
        number = pool.map(parallel_operation, random_numbers)
        output_list = [str(num)[0]+"."+str(num)[1:3]+f"e{len(str(num))-1}" for num in number]
        pool.close()
        pool.join()
    end = endTimer()
    return [random_numbers, output_list, returnRuntime(start,end)]
