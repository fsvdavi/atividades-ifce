def cabecalho(txt):
    print('-' * 45)
    print(txt.center(42))
    print('-' * 45)

cabecalho("Calculo de tempo e velocidade")

distancia = float(input("Digite a distancia percorrida:(em km) \n"))
velocidade = float(input("Digite a velocidade média:(em km/h) \n"))

cabecalho("Tempo médio e conversão pra m/s")

tempo = distancia / velocidade
velocidade2 = velocidade / 3.6

print(f"O tempo médio de viagem foi de {tempo:.2f}h\n e a velocidade em m/s foi de {velocidade2:.2f}m/s")




