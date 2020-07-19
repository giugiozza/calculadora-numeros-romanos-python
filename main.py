linhas = []
lista_de_materiais = []

class Contador:
    def __init__(self, simbolo, quantidade):
        self.simbolo = simbolo
        self.quantidade = quantidade

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
    romano = romano.upper()
    total = 0
    simbolo_atual = ""
    simbolo_anterior = ""
    valor_atual = 0
    valor_anterior = 0
    atual_foi_calculado = False
    contador = Contador("", 1)

    if (len(romano) == 1):
        total = conversor_de_romanos_para_arabicos(romano)
        
    else:
        for i in reversed(range(len(romano))): # leitura reversa do número, caractere a caractere
            
                simbolo_atual = romano[i:i+1]
                valor_atual = conversor_de_romanos_para_arabicos(simbolo_atual)
                if (valor_atual == -1):
                    return -1
                if(simbolo_atual != contador.simbolo):
                    contador = Contador("", 1)
                if(i == 0): #quando chegar no primeiro caractere
                    if(not atual_foi_calculado):
                        total = total + valor_atual
                    break

                simbolo_anterior = romano[i-1:i]
                valor_anterior = conversor_de_romanos_para_arabicos(simbolo_anterior)
                if (valor_anterior == -1):
                    return -1
                
                #3 casos para os valores do atual e anterior: <, >, ==
                if(valor_anterior < valor_atual):
                    if(simbolo_anterior == "I"):
                        if(simbolo_atual == "V" or simbolo_atual == "X"):
                            if(not atual_foi_calculado):
                                total = total + (valor_atual - valor_anterior)
                                atual_foi_calculado = True

                    elif(simbolo_anterior == "X"):
                        if(simbolo_atual == "L" or simbolo_atual == "C"):
                            if(not atual_foi_calculado):
                                total = total + (valor_atual - valor_anterior)
                                atual_foi_calculado = True

                    elif(simbolo_anterior == "C"):
                        if(simbolo_atual == "D" or simbolo_atual == "M"):
                            if(not atual_foi_calculado):
                                total = total + (valor_atual - valor_anterior)
                                atual_foi_calculado = True
                            
                    else:
                        return -1
                    
                elif(valor_anterior > valor_atual):
                    if(not atual_foi_calculado):
                        total = total + valor_atual
                    atual_foi_calculado = False

                elif(valor_anterior == valor_atual):
                    if(simbolo_atual == "D" or simbolo_atual == "L" or simbolo_atual == "V"):
                        return -1

                    contador.simbolo = simbolo_atual
                    contador.quantidade = contador.quantidade + 1
                    if(contador.quantidade > 3):
                        return -1
                    elif(not atual_foi_calculado):
                        total = total + valor_atual
                    atual_foi_calculado = False
                                
    return total

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
    valor = 0
    if not(linha.endswith("?")):
        if not(linha.endswith("créditos")):
            array_da_linha = linha.partition("representa")
            nome = array_da_linha[0].strip()
            romano = array_da_linha[2].strip()
            valor = calculadora_de_romanos(romano)
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
            if (item == i.nome):
                encontrou = True
                valor = i.valor
                if (valor == -1):
                    arquivo_saida.write("Nem ideia do que isto significa!\n")
                else:
                    material = i.nome
                    arquivo_saida.write(resposta.format(material, valor))
        if not(encontrou):
                arquivo_saida.write("Nem ideia do que isto significa!\n")
        

        #TODO
        #<parametro para função calcula valor> = array_da_linha[2].strip()
    elif (linha.startswith("quantos créditos")):
        linha = linha.replace('?', '')
        array_da_linha = linha.partition("são")
        #dicionario_de_perguntas["credito"] = array_da_linha[2].strip()

        #TODO
        #<parametro para função calcula credito> = array_da_linha[2].strip()

# FINAL #

try:
    arquivo_entrada.close()
except:
    print("Erro ao fechar o arquivo de entrada.")

try:
    arquivo_saida.close()
except:
    print("Erro ao fechar o arquivo de saída.")
