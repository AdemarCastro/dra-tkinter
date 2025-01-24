from taxas import TAXAS_CONVERSAO

# Insira a variável para armazenar a lista de conversões realizadas
historico = []

def converter(valor, opcao):
    try:
        if opcao in TAXAS_CONVERSAO:
            resultado = valor * TAXAS_CONVERSAO[opcao]
            unidade = opcao.split()[-1]
            # Insira o código para adicionar a conversão realizada ao histórico
            historico.append(f'{valor:.2f} {unidade} = {resultado:.2f} {unidade}')
            return f"{resultado:.2f} {unidade}"
        else:
            return "Selecione uma opção válida."
    except ValueError:
        return "Por favor, insira um número válido."

# Insira a função get_historico
def get_historico():
    return historico