#topic decorator

# def test(fun):
#     def test2():
#         print("first line of test2")
#         fun()
#         print("2nd line of test2")

#     return test2 
    
    
# যদি return test2 না লিখতে, তাহলে test() কোনো ফাংশন রিটার্ন করতো না (মানে None রিটার্ন করতো)।

# ফলে hello = test(hello) করার পর hello এর ভ্যালু হয়ে যেতো None, আর তুমি hello() কল করলে এরর পেতে।

# তাই return test2 দরকার, যাতে পুরানো ফাংশনকে নতুনভাবে মোড়ানো যায়।
#here we can also write like that 


# @test
# def hello():
#     print("hello world")

#hello=test(hello)
# hello()