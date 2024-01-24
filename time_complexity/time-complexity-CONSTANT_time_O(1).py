''''
https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7
'''
import time

def constant_time_O_Um(data):
    # Constant Time — O(1)
    ''''
    An algorithm is said to have a constant time when it is not dependent on the input data (n). 
    No matter the size of the input data, the running time will always be the same.
    '''
    start = time.time()
    
    dataf = data[0]
    
    end = time.time()
    r_ms = (end-start) * 10**3   
    print("The time of execution of constant_time_O_Um is:", r_ms, "ms")
    
    return dataf


if __name__ == '__main__': 
    sorted_list = [1, 2, 3, 4, 6, 5, 7, 8, 9]
    print(constant_time_O_Um(sorted_list))

