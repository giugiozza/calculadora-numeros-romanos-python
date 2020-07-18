linhas = []
valor = 0
lista_de_materiais = []

class Material:
  def __init__(self, nome, romano, valor):
    self.nome = nome
    self.romano = romano
    self.valor = valor

def conversor_de_romanos_para_arabicos(romano):
    if(romano == "I"):
        return 1
    elif(romano == "V"):
        return 5
    elif(romano == "X"):
        return 10
    elif(romano == "L"):
        return 50
    elif(romano == "C"):
        return 100
    elif(romano == "D"):
        return 500
    elif(romano == "M"):
        return 1000
    else:
        return -1 #erro: não é romano

def calculadora_de_romanos(romano):
    valor = 0
    if(len(romano) == 1):
        valor = conversor_de_romanos_para_arabicos(romano.upper())
    #else:
        
    return valor

def calculadora_de_creditos(item):
    #TODO
    return 1

def calculadora_de_valores(item):
    #TODO
    return 1


print("Seja bem-vind@, Vendedor Interespacial!\n")

nome_arquivo_entrada = input("Por favor, digite o nome do arquivo (sem a extensão): ")
nome_arquivo_entrada = nome_arquivo_entrada + ".txt"

nome_arquivo_saida = input("Por favor, digite um nome de arquivo para armazenar as respostas (sem a extensão): ")
nome_arquivo_saida = nome_arquivo_saida + ".txt"

try:
    arquivo_entrada = open(nome_arquivo_entrada)
except:
    print("Arquivo de entrada não encontrado.")

try:
    arquivo_saida = open(nome_arquivo_saida, 'w+')
except:
    print("Erro ao criar/abrir rquivo de saída.")


linhas = arquivo_entrada.readlines()

#TODO cases que caem no else que não se sabe o que significa (colocar o tipo como "erro")
    # e valores negativos
for linha in linhas:
    linha = linha.rstrip()
    if not(linha.endswith("?")):
        if not(linha.endswith("créditos")):
            array_da_linha = linha.partition("representa")
            nome = array_da_linha[0].strip()
            romano = array_da_linha[2].strip()
            valor = calculadora_de_romanos(array_da_linha[2].strip())
            lista_de_materiais.append(Material(nome, romano, valor))
        elif (linha.endswith("créditos")):
            linha = linha.replace("créditos", "")
            array_da_linha = linha.partition("valem")
            quantidade_de_creditos = int(array_da_linha[0].strip())
            #dicionario_de_creditos[array_da_linha[2].strip()] = quantidade_de_creditos
    elif (linha.startswith("quanto vale")):
        linha = linha.replace('?', '')
        array_da_linha = linha.partition("vale")
        item = array_da_linha[2].strip()
        resposta = "{} vale {}\n"
        encontrou = False
        for i in lista_de_materiais:
            if item in i.nome:
                valor = i.valor
                material = i.nome
                arquivo_saida.write(resposta.format(material, valor))
                encontrou = True
        if not(encontrou):
                arquivo_saida.write("Nem ideia do que isto significa!")
        

        #TODO
        #<parametro para função calcula valor> = array_da_linha[2].strip()
    elif (linha.startswith("quantos créditos")):
        linha = linha.replace('?', '')
        array_da_linha = linha.partition("são")
        #dicionario_de_perguntas["credito"] = array_da_linha[2].strip()

        #TODO
        #<parametro para função calcula credito> = array_da_linha[2].strip()

# for tipo_de_pergunta, item in dicionario_de_perguntas.items():
#     if(tipo_de_pergunta == "credito"):
#         resposta = "{} custa {} créditos"
#         valor = calculadora_de_creditos(item)
#         print(resposta.format(item, valor))
#     elif(tipo_de_pergunta == "valor"):
#         resposta = "{} vale {}"
#         valor = calculadora_de_romanos(dicionario_de_unidades[item])
#         print(resposta.format(item, valor))
#     else:
#         print("Nem ideia do que isto significa!")


# FINAL #

try:
    arquivo_entrada.close()
except:
    print("Erro ao fechar o arquivo de entrada.")

try:
    arquivo_saida.close()
except:
    print("Erro ao fechar o arquivo de saída.")
