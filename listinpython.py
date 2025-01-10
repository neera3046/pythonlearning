# listt=[1]
# listt.append(4)
# print(listt)
# listt.insert(3,7)
# print(listt)
# list2=["1","neeraj","3","verma"]
# list2.sort()
# print(list2)
# WAP to ask user eneter the names of their 3 favourite movies & store them in a list.

# print("this the movie list program")
# movie_list=[]
# movie_list.append(input("Enter first movie name : "))
# movie_list.append(input("Enter second movie name : "))
# movie_list.append(input("Enter third movie name : "))
# print(movie_list)


#WAP to check if a list contains a palindrome of elements.

sample_lst=[1,2,3,2,1]
second_lst=sample_lst
second_lst.reverse()
print(second_lst)
if second_lst == sample_lst:
    print("pallindrome list")
else:
    print("not pallindrome")

print(sample_lst)        