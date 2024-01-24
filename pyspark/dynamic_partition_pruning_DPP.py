'''
To reduce the volume of data:
    Predicate pushdown
    Partition pruning

Dynamic partition pruning:
    Requirements to met
        works for one large and another small table
        large table must be partitioned
        broadcast the small table

Solution
    Enable Dynamic Partition Pruning Feature
    Apply broadcast on the small table

tabela dimensao é menor
tabela fato é maior
'''
