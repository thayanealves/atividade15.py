# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.

num1 = float(input("digite o primeiro número"))
num2 = float(input("digite o segundo número"))

operaçao = input("digite a operação que deseja ultilizar; soma, multiplicação, subtração, divisão")

if operaçao == "soma":
    print(num1 + num2)
elif operaçao == "multiplicação":
    print(num1 * num2)
elif operaçao == "subtração":
    print(num1 - num2)
if operaçao == "divisão":
    print(num1 / num2)   