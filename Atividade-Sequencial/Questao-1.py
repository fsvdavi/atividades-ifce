def cabecalho(txt):
  print('-' * 45)
  print(txt.center(42))
  print('-' * 45)

cabecalho("LOJA PORTAL ORGÂNICO")

while True:
  produto = float(input("Digite o valor do produto que deseja comprar.\n"))
  if produto <= 0:
      print("O valor não pode ser negativo ou nulo")
      continue
  parcelas = int(input("Agora digite em quantas parcelas deseja pagar por ele (máx 5).\n"))

  if parcelas > 5:
      print("Não é permitido parcelar em mais de 5 vezes")
      continue
  elif parcelas <= 0:
      print("A quantidade de parcelas não pode ser nula ou negativa")
      continue

  valor_parcela = float(produto / parcelas)

  print(f"O valor de cada de parcela será de R$ {valor_parcela:.2f} ")


  alternativa = input("Deseja continuar? (S/N)\n")
  if alternativa.upper() == "N":
    break
  elif alternativa.upper() == "S":
    continue




