#Print the elemets of the following list using a loop
list=[1,4,9,16,25,36,49,81,100]
for xx in list:
    print(xx)

yy=int(input("enter the number to be found from list:"))   
for uu in list:
    if uu ==yy:
        print("number found")
        break
    # else:
    #     print("number not found") 