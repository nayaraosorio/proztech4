def calculadora():
    while True:

        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")
        print("Digite o número da operação que deseja realizar: ")
        oper = input()

        if oper == '0':
            print("Calculadora encerrada;")
            break
        elif oper == '1':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(num1, "+", num2, "=", num1+num2)
        elif oper == '2':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(num1, "-", num2, "=", num1-num2)
        elif oper == '3':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(num1, "*", num2, "=", num1 * num2)
        elif oper == '4':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if num2 != 0:
                print(num1, "/", num2, "=", num1 / num2)
            else:
                print("Não é realizar esta operação!")
        else:
            print("Essa opção não existe!")


calculadora()