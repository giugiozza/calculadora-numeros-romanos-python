linhas = []
dicionario_de_unidades = {}
dicionario_de_creditos = {}
quantidade_de_creditos = 0

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
            linha = linha.replace("créditos", "")
            array_da_linha = linha.partition("valem")
            quantidade_de_creditos = int(array_da_linha[2].strip())
            dicionario_de_creditos[array_da_linha[0].strip()] = quantidade_de_creditos
    elif (linha.startswith("quanto vale")):
        linha = linha.replace('?', '')
        array_da_linha = linha.partition("são")
        #TODO
        #<parametro para função calcula valor> = array_da_linha[2].strip()
    elif (linha.startswith("quantos créditos")):
        linha = linha.replace('?', ' ')
        array_da_linha = linha.partition("são")
        #TODO
        #<parametro para função calcula credito> = array_da_linha[2].strip()
print(dicionario_de_unidades)
print(dicionario_de_creditos)

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

