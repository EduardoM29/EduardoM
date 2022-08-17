import math


print("Cálculo da equação de segundo grau by Eduardo M")
A = float(input("Digite o valor de a: "))
B = float(input("Digite o valor de b: "))
C = float(input("Digite o valor de c: "))


d = (B ** 2 - 4 * A * C)

print("Delta:",d)

if d > 0 :
    r = math.sqrt(d)
    X1 = (-B + r)/(2*A)
    X2 = (-B - r)/(2*A)
    print("Valor das raízes reais:",X1,"e",X2)
elif d == 0:
    r = math.sqrt(d)
    X1 = (-B)/(2*A)
    print("Valor da raíz real:",X1)
elif d < 0:
    print("Não existe raíz real")
