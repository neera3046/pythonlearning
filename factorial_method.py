def fact_method(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n* fact_method(n-1)
    

print(fact_method(5))    