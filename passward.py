print("Create a Password: ")
cp = input()

print("\nEnter Two Numbers to Add: ")
numOne = int(input())
numTwo = int(input())

print("\nEnter Password to Display the Result: ")
ep = input()

if cp == ep:
    sum = numOne + numTwo
    print("\nResult = ", sum)
else:
    print("\nWrong Password!")