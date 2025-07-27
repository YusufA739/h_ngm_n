filename=input("input file name")
file=open(filename+".txt","r")
filedata=file.readlines()
file.close()
new_data=""
for carrier in filedata:
    new_data+=carrier.strip("\n")+" "
file=open("newfile.txt","w")
file.write(new_data)
file.close()
