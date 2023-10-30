file=open("input.txt","w")
w="hello\n"
file.writelines(["I am Rutuja_Hattikote\n","My Roll No is 5\n","I am student of DYPCET\n"])
print(file.write(w))

file=open("input.txt","r")
print(file.read())