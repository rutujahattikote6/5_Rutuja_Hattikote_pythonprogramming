#Using split function
file=open("input.txt","r")
data=file.readlines()
for line in data:
    word=line.split()
    print(word)
