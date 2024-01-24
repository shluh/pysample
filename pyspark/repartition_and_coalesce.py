'''
REPARTITION

When you should repartition
    1. repartition causes shuffle
    2. do not repartition without a cause
    3. common repartition scenarios
        - reuse df multiple times and filter data on some specific column. 
            In this case repartition on filter column cloud be worth it
        - you have very few partitions and your data is not well distributed across the cluster
            In that case, repartitioning with large number of partitions can spread your data more 
                appropriately across the cluster and speed up the rest of the processing
        - the partitions are large, or you have some skewed partitions 
            In this scenario, you may want to uniformly repartition the dataframe to a large number 
                of uniform partitions. 

You should use repartitioning when you want to increase the number of partitions or repartition on specific col.

TO REDUCE THE NUMBER OF PARTITIONS USE COALESCE


COALESCE
    Doesnt cause shuffle/sort
    It combines local partition only
    Coalesce will not increase the number of partitions
    Coalesce can cuase skewed partitions
        wich can cause OOM exception
'''