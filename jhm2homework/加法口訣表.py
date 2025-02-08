size = int(input("Input Addition Table Size smaller 10:"))

print("------------------------------------------------------------")

for i in range(1, size + 1 ):
    for j in range(1, size + 1 ):
        sum = i + j        
        if sum < 10 :
            print(f"{i} + {j} = {sum}  ", end=" ")
        else:
            print(f"{i} + {j} = {sum} ", end=" ")
    print()

print("------------------------------------------------------------")