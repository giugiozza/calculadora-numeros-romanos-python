linhas = []
dicionario_de_unidades = {}
dicionario_de_creditos = {}

print("Seja bem-vind@, Vendedor Interespacial!\n")

nome_arquivo = input("Por favor, digite o nome do arquivo (sem a extensão): ")
nome_arquivo = nome_arquivo + ".txt"

try:
    arquivo = open(nome_arquivo)
    print("Arquivo aberto com sucesso.\n")
except:
    print("Arquivo não encontrado.")

linhas = arquivo.readlines()
for linha in linhas:
    linha = linha.rstrip()
    if not(linha.endswith("?")):
        if not(linha.endswith("créditos")):
            array_da_linha = linha.partition("representa")
            dicionario_de_unidades[array_da_linha[0].strip()] = array_da_linha[2].strip()
        elif (linha.endswith("créditos")):
            linha.replace('créditos', '')
            array_da_linha = linha.partition("valem")
            dicionario_de_creditos[array_da_linha[0].strip()] = array_da_linha[2].strip()
    elif (linha.startswith("quanto vale")):
        linha.replace('?', '')
        array_da_linha = linha.partition("são")
        #TODO
        #<função calcula valor> = array_da_linha[2].strip()
    elif (linha.startswith("quantos créditos")):
        linha.replace('?', '')
        array_da_linha = linha.partition("são")
        #TODO
        #<função calcula credito> = array_da_linha[2].strip()
'''
print(len(linhas))
print("\n" + linhas[-1]+"\n")
print(linhas[-1].endswith("?"))
'''


# FINAL #

try:
    arquivo.close()
except:
    print("Erro ao fechar o arquivo.")

