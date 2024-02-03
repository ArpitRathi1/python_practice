# Ques) Write a python program to find how many repeated words in the given sentence.
# string="my name is Arpit my city is indore"
# Solution-

string="my name is Arpit my city is indore"
lst=string.split()
value=0
dic = {}
dic=dict.fromkeys(lst,value)
print(dic)

for i in lst:
    #dic[i] = dic.get(i,0)+1
    if i in lst:
        dic[i]=dic[i]+1
print(dic)
