
#I/O SYSTEM IN PYTHON
#write
#reading
#append
#first we create a file in this folder named myfile.txt
#then we read the file
# f=open("myfile.txt","r")#if we use w and change the file name then it create a new file
# text=f.read()
# print(text)
# f.close()

f=open("myfile.txt","w")#we write into the file if we "a" then it will append the text again  hello i a
#am writing into myfile.txthello i am writing into myfile.txt
f.write("hello i am writing into myfile.txt")
f.close()

#here we use multiple time  f.close() but if we use 
# with open("myfile.txt","r") as f:then we dont need to use f.close()