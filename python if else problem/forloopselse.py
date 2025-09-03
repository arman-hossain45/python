for i in range(5):
    print(i)
else:
    print("sorry no i")
    print("this is the else block")

for j in range(5):
    print(j)

    if j == 4:
        break#here when we use else with  for in a python when each itteration 
    #when complete then print else other wise if we break the loop the else will not run iteration complete then run else 
else:
    print("sorry no j")
    print("this is the else block")
