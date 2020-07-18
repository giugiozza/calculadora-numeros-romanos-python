print("Seja bem-vind@, Vendedor Interespacial!\n")

nome_arquivo = input("Por favor, digite o nome do arquivo (sem a extensão): ")
nome_arquivo = nome_arquivo + ".txt"

try:
    arquivo = open(nome_arquivo)
except:
    print("Arquivo não encontrado.")


