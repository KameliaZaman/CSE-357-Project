n = int(input("Enter an integer:"))
fact = 1
for factor in range(n, 1, -1):
    fact = fact * factor
print("The Factor is: ", fact)
