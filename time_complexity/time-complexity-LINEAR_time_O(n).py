''''
https://pt.linkedin.com/pulse/o-algoritmo-de-busca-linear-e-java-udinei-silva#:~:text=O%20algoritmo%20de%20Busca%20Linear%20%C3%A9%20um%20algoritmo%20simples%2C%20que,)%20desordenado%2C%20de%20modo%20sequencial.&text=O%20primeiro%20elemento%20tem%20o%20%C3%ADndice%200%20(zero).

The Linear Search algorithm is a simple algorithm,
    that searches for an element
    in a DISORDERERED vector (array or list), in a sequential manner. 
'''

import time
 
def linear_search_brute_force(vector, number_wanted): 
    '''
    This algorithm, in terms of its complexity, is an O(n) algorithm.

    O(1) - best case: the element sought is the first in the array
    O(N) - worst case: the element sought is the last in the array or does not exist in the array
    O(N/2) - average case: the element is found after (N+1)/2 comparisons.
    '''

    start = time.time()
    value = -1

    for i in range(len(vector)):
        ''' 
        fruits.index('banana'), 
            Return zero-based index in the list of the first item whose value is equal to x. 
            Raises a ValueError if there is no such item.
        '''    
        if vector[i] == number_wanted:
            value = i 
        
    end = time.time()
    r_ms = (end-start) * 10**3
    print("The time of execution of force brute is:",
        r_ms, "ms")
    
    return value


def linear_search_hash_map(vector, number_wanted): 
    
    start = time.time()
    value = -1
    mydict = {}

    for i in range(len(vector)):
        mydict[vector[i]] = i

    if number_wanted in mydict:
        value = i

    end = time.time()
    r_ms = (end-start) * 10**3

    print("The time of execution of hashmap is:", r_ms, "ms")
    
    return value

def linear_search_hash_map_improved(vector, number_wanted): 
    
    start = time.time()
    value = -1
    mydict = {}

    for i in range(len(vector)):
        if number_wanted in mydict:
            value = i
        mydict[vector[i]] = i

    end = time.time()
    r_ms = (end-start) * 10**3

    print("The time of execution of hashmap improved is:", r_ms, "ms")
    
    return value


mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
number_wanted = 50

linear_search_brute_force(mylist, number_wanted)
linear_search_hash_map(mylist, number_wanted)
linear_search_hash_map_improved(mylist, number_wanted)