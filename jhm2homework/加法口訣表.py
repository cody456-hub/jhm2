size = int(input("Input Addition Table Size smaller 10："))

print("------------------------------------------------------------")

for b in range(size + 1):
    for c in range(size + 1):
        a = [f"{b} + {c} = { b + c }" for j in range(size + 1)]

        formatted_a = [f"{entry:<11}" for entry in a]



    print("".join(formatted_a))

print("------------------------------------------------------------")
