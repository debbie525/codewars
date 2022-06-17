# Count the number of divisors of a positive integer n.

# Random tests go up to n = 500000.

n = int(input("Please input a postive integer:"))

count = 0
for divisor in range (1,n+1):
    if n% divisor ==0:
        count+=1

print(f"number of divisor: {count}")