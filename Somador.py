print("Digite valores terminados em zero para ser somados")

soma = 0
valor = 1

while valor != 0:
    valor = int(input("Digite o próximo número a ser somado: "))
    soma = soma + valor 
print("A soma dos números é:",soma)