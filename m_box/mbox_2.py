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