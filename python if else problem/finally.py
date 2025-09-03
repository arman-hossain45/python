def func():
    try:
        k=[1,2,3,4,5,56]
        i=int(input("Enter a index: "))
        print(k[i])
        return 1
    except ValueError:
        print("some error occure .")
        return 0
    finally:
        print("This will always execute.")#finally block always execute whether there is an error or not
        print("End of the program.")
x=func()
print(x)
