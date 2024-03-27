"""Ques) Write a program to read through the mbox-short.
txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer."""
# Solution-

file=open("mbox-short.txt", "r")
file_content=file.readlines()
file.close()
time_dictionary={}
for i in file_content:
	element=i.strip().split()
	if "From" in element:
		time=element[-2]
		time_list=time.split(":")
		time_dictionary[time_list[0]]=time_dictionary.get(time_list[0],0)+1
sorted_list=sorted(time_dictionary)
# print(time_dictionary)
values=[]
for i in sorted_list:
	print(i,"-->",time_dictionary[i])
