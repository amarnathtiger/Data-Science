x, y = map(int, input("Enter X,Y: ").split(","))
result = [[i * j for j in range(y)] for i in range(x)]
print(result)
