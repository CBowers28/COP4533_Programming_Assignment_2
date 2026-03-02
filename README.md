# Names

Dylan Esperto

UFID: 53118184

Christopher Bowers 

UFID: 19272960

# Instructions

Use Python 13 to run src\main.py in order to use the cache replacement comparer.

```
python src\main.py INPUT
```

## Example Usage

```powershell
python src\main.py 3 5
1 2 3 4 5
```

To recreate the out1.txt, you can use the following command, or just manually type the input data in in1.txt:

```powershell
cat data\in1.txt | python src\main.py
```

# Question 1

| File | k | m | FIFO | LRU | OPTFF |
| ---- | --- | --- | --- | --- | --- |
| File1 | 30 |  50 |      31 |      31 |      31 |
| File2 | 30 | 100 |      80 |      79 |      66 |
| File3 | 30 | 150 |     124 |     122 |      97 |
| File4 | 30 | 200 |     175 |     180 |     139 |
| File5 | 30 | 250 |     211 |     212 |     164 |
| File6 | 30 | 300 |     274 |     273 |     210 |
| File7 | 30 | 400 |     364 |     363 |     280 |
| File8 | 30 | 500 |     478 |     478 |     377 |

- It is clear that OPTFF outperforms the other algorithms. It has the fewest misses in all cases except the first, where all the algorithms tie.
- FIFO and LRU perform quite similarly. Sometimes, FIFO is slightly better than LRU, and sometimes LRU is better. It seems there isn't much difference in performance between the two.

# Question 2

The following input:

3 7

5 2 1 5 0 5 2

Gives the resulting hit counts:

FIFO  : 6

LRU   : 5

OPTFF : 4

It makes sense that OPTFF is more optimal than FIFO/LRU. OPTFF uses information from the future to make the best current decision, while the other algorithms only consider what has already occurred, and can't make any decisions based on future requests. 

# Question 3

Assume A is an optimal offline algorithm. Let t be the first time at which A and OPTFF differ.

At time t, suppose there is a page fault and the cache is full. Let OPTFF evict page x, and let A evict a different page y.

By definition of OPTFF, page x is the page whose next request occurs farthest in the future among all pages currently in the cache. Therefore, the next time page x is requested will be further in the future than the next time page y is requested.

In A, we can instead evict page x at time t and page y where page x used to be. This action of swapping can only decrease or not affect the number of future page faults in algorithm A, it cannot make it worse. So A can be modified like this repeatedly each time A and OPTFF differ.

When the end of this is reached, A has been modified without loss of optimality to OPTFF. Therefore, OPTFF is optimal.

