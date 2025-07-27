#imports
import random

#main program
filename=input("This is the random selector program. input file name to continue > ")
file=open(filename+".txt","r")
filedata=file.readlines()
file.close()
new_data=""
removed=1
index=random.randint(0,len(filedata)-removed)
for carrier in range(10):
    index=random.randint(0,len(filedata)-removed)
    new_data+=str(filedata[index])+" "
    filedata.remove(filedata[index])
    removed+=1
new_data=new_data.strip(" ")
file=open(filename+" editied copy.txt","w")
file.write(new_data)
file.close()
