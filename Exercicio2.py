def verificar_categoria_habilitacao(rodas, peso, pessoas):
    if rodas == 2 or rodas == 3:
        return "Categoria A"
    elif rodas == 4 and pessoas <= 8 and peso <= 3500:
        return "Categoria B"
    elif 4 <= rodas and peso > 3500 and peso <= 6000:
        return "Categoria C"
    elif 4 <= rodas and pessoas > 8:
        return "Categoria D"
    elif 4 <= rodas and peso > 6000:
        return "Categoria E"
    else:
        return "Categoria não encontrada"

# Informações do veículo
quantidade_rodas = int(input("Informe a quantidade de rodas do veículo: "))
peso_bruto = float(input("Informe o peso bruto em quilogramas do veículo: "))
quantidade_pessoas = int(input("Informe a quantidade de pessoas no veículo: "))

# Verificar categoria de habilitação
categoria = verificar_categoria_habilitacao(quantidade_rodas, peso_bruto, quantidade_pessoas)
print("A categoria de habilitação para este veículo é:", categoria)
