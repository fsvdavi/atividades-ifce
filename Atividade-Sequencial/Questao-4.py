def cabecalho(txt):
    print('-' * 45)
    print(txt.center(42))
    print('-' * 45)

cabecalho("CONVERSOR CELSIUS E FAHRENHEIT")

while True:
    alternativa = int(input(
    "Digite o número da opção que deseja?\n"
    "1 - Celsius para Fahrenheit\n"
    "2 - Fahrenheit para Celsius\n"
    ))
    if alternativa == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")
    elif alternativa == 2:
        fahrenheit = float(input("\nDigite a temperatura em Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"\nA temperatura em Celsius é: {celsius:.2f}°C")
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")
        continue 

    continuar = input("Deseja continuar? (S/N): ")
    if continuar.upper() != "S":
        break
    