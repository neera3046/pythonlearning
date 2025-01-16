#WAF  to print the length of a list. (list is the parameter)
# def len_calculator(listx=[]):
#     return(len(listx))
# print(len_calculator([1,2,3,4,6]))
# print(len_calculator())

#WAF to find the factorial of n.
# def calculate_fact(fact):
#     x=1
#     y=1
#     while x<=fact:
#         y=x*y
#         x+=1
#     print(y)
#     return(y)    

# print(calculate_fact(10))

#Waf to print whether number is even or odd
def odd_even(num):
    if num%2 != 0:
        result="ODD"
    else:
        result="EVEN"  

    return(result)
print(odd_even(7))      

