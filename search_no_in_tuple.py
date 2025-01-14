tuplen=(1,4,9,16,25,36,49,64,81,100)
no_to_be_searched=int(input("Please enter the number to be searched: "))
len_of_tuple=len(tuplen)-1
i=0
while i<=len_of_tuple:
    if tuplen[i]== no_to_be_searched:
        print("number found at index ",i ," is ",no_to_be_searched,".")
    i+=1