print("PALINDROME NUMBER")
print()
def palindrome(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        print(temp,"is a palindrome number!")
    else:
        print(temp,"is not a palindrome number!")
num=int(input("Enter number:"))
palindrome(num)