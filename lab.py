num = int(input("Enter a table number: "))
limit = int(input("Enter a limit: "))

for i in range(1, limit + 1):
    print(f"{num} x {i} = {num * i}")