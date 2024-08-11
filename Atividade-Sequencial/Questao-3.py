def cabecalho(txt):
    print('-' * 45)
    print(txt.center(42))
    print('-' * 45)

cabecalho("CÁLCULO DE IMC")

massa = float(input("Digite a massa corporal da pessoa a ser medida: \n"))
altura = float(input("Agora, digite a altura da pessoa: \n"))

imc = massa / (altura ** 2)

print("O IMC da pessoa é: {:.2f}".format(imc))