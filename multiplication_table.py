num = int(input("Enter a number: "))

print("\nMultiplication Table of", num)

for i in range(1, 11):
    print(f"{num} × {i} = {num * i}")