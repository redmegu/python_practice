num = int(input("Check for factorial: "))
if num < 0:
    print("There is no factorial for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
        result = 1
        for x in range(1,num+1):
            result = result*x
            print("The factorial of " + str(x) + " is " + str(result))