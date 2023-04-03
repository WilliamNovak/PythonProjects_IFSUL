def calc(num1, num2, opera):
    
    if(opera == "+"):
        return num1 + num2
    elif(opera == "-"):
        return num1 - num2
    elif(opera == "x"):
        return num1 * num2
    elif(opera == "/"):
        return num1 / num2
    else:
        return "Operação inválida!"


print("Bem-vindo a minha calculadora!")

num1  = int(input("Informe o primeiro número: "))
num2  = int(input("Informe o segundo número: "))
opera = input("Informe uma operação: ")

result = calc(num1, num2, opera)

if(result == "Operação inválida!"):
    print(result)
else:
    print(f'{num1} {opera} {num2} = {result}')