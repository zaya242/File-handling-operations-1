#program to merge two files into a third files


#reading data from file1
with open('codingal.txt') as fp:
    data1 = fp.read()

#reading data from file2
with open('new_file.txt') as fp:
    data2 = fp.read()


#merging 2 files
#to add the data of file2
#from next line
data1 += "\n"
data1 += data2
print("Merging two files.....")
with open('mergerdfile.txt','w') as fp:
    fp.write(data1)