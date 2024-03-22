file=open("mbox-short.txt", "r")
file_content=file.readlines()
file.close()
email={}
for i in file_content:
	element=i.strip().split()
	if "From" in element :
		index_of_from=element.index("From")
		email[element[index_of_from+1]]=email.get(element[index_of_from+1],0)+1
print(email)