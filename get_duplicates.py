# Ques) Given three arrays, we have to find common element in three sorted list using set.
# ar1=[1,5,10,20,80,40]
# ar2=[6,7,20,80,100]
# ar3=[3,4,15,20,80,30,120]
# Solution-

ar1=[1,5,10,20,80,40]
ar2=[6,7,20,80,100]
ar3=[3,4,15,20,80,30,120]

# Typecast it into sets.

ar1_set=set(ar1)
ar2_set=set(ar2)
ar3_set=set(ar3)

# Join using intersection.

ar1_2 = ar1_set.intersection(ar2_set)
final_set=ar1_2.intersection(ar3_set)

# Again typecast final_set into fianl_list.

final_list=list(final_set)

print(final_list)
