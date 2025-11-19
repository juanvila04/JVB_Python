altura = int(input("Introduce la altura de la figura"))

print(" " * altura, end="")
print("*")

for i in range (1, altura + 1):
    print(" " * (altura - i), end="")
    print("*", end="")
    print(" " * (i - 1), end="")
    print("*")

print(" " * altura, end="")
print("*")



print("*" + " " * (altura - 1) + "*")
for i in range(altura - 1, 0, -1):
    print(" " * (altura - i) + "*" + " " * (i - 1) + "*")
print(" " * altura + "*")
