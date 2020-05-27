print("SUM OF THE SERIES")
print()
def sum_series(num): 
    res = 0
    fact = 1
    for i in range(1, num+1): 
      fact=fact*i 
      res = res + (i/ fact) 
    print ("Sum of this series is:",res) 
n = int(input("Enter the value of N:"))
sum_series(n)