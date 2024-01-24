''''
EXECUTOR PROCESS
    reserved memory
    spark memory
        executor memory pool: dataframe computations
        storage memory pool: caching dataframes ***
    user mememory
'''

'''
How do you cache?
    cache() - use de default MEMORY_AND_DISK storage level
    persist() - more flexible on storage level (but do the same as cache())


persist args
    useDisk True
    useMemory True
    useOffHeap False (can be set to true, but needs to be activated previously, to have an effect on this configuration)
    deserialized False (if true object will be serialized and then, save some memory, but incur costs when spark access 
        the data, coz needs to be deserialized)

we should cache when df fits in memory, and will be used in frequently in different actions
do not cache when df doesnt fit in memory; when do not use frequently; or when df is to small
'''


