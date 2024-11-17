# 1. Write a Python script to sort (ascending and descending) a dictionary by value

def dic_sort(a):
    b=list(a.values())
    b.sort()
    print(b)

a={'a':2,'b':4,'c':3}
dic_sort(a)