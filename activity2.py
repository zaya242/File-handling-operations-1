#create a new file
new_file3 = open('new_file3.txt','x')
new_file3.close()

#checking if a file exists
import os 
print("checking if my_file exists or not.....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")

#create a new if it doesn't    
my_file = open("my_file.txt","w")
my_file.write("Hi!I am penguin and I am 1 year old")
my_file.close()

#delete file named codingal
os.remove('codingal.txt')

#delete the folder
