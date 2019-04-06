# Exercício 037
num = int(input('Informe o número para conversão: '))
base = int(input('Agora digite "1" para binário, "2" para octal e "3" para hexadecimal: '))
if base == 1:
    print(bin(num)[2:])
elif base == 2:
    print(oct(num)[2:])
elif base == 3:
    print(hex(num)[2:])
