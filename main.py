# Power of 2 Check (BitWise)

n = 32

result = n & (n - 1)

if result == 0:
    print("Power of 2") 
else:
    print("Not a power of 2")