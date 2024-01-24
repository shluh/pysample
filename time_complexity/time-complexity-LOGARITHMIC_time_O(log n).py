''''
https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7
'''
import time


def logarithmic_time_O_log_n(data, value):
    # Logarithmic Time — O(log n)
    
    ''''
    An algorithm is said to have a logarithmic time complexity when it reduces the 
        size of the input data in each step (it don't need to look at all values of the input data)
    
    Algorithms with logarithmic time complexity 
        are commonly found in operations on binary trees 
        or when using binary search. 
        Let's take a look at the example of a binary search, 
        where we need to find the position of an element in a sorted list:
    '''

    n = len(data)
    left = 0
    right = n - 1
    middle = (left + right) // 2
    print('N len :', n, '; Left :', left, '; Right:', right, '; Middle: ', middle, '; Middle Value: ', data[middle])
    
    while left <= right:
        middle = (left + right) // 2 # recupera o index do elemento central
        print('loop\'s middle index: ',middle)
        
        if value < data[middle]:
            right = middle - 1
            print('right index:', right)

        elif value > data[middle]:
            left = middle + 1
            print('left index:', left)
        else:
            return print('Index do elemento procurado: [',middle, ']')
    raise ValueError('Value is not in the list')

if __name__ == '__main__':
    # unsorted_list = [1, 2, 9, 8, 3, 4, 7, 6, 5]  
    sorted_list = [1, 2, 3, 4, 6, 5, 7, 8, 9] 
    element = 2
    logarithmic_time_O_log_n(sorted_list, element) 

