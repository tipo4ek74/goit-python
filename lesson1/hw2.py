a = float(input("a "))
b = float(input("b "))
c = float(input("c "))

D = (b ** 2 - 4 * a * c)

x1 = (-b + D ** 0.5) / (2 * a)
x2 = (-b - D ** 0.5) / (2 * a)

print("Дискриминант D : ", + float(D))
print("x1 = ", float(x1))
print("x2 = ", float(x2))