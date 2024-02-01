with open('../docs/produtos.txt', 'r', encoding='UTF-8') as arquivo:
    conteudo = arquivo.read()

separaString = []

with open('../docs/PRODUTOS-PARA-RESUMIR.txt', 'r', encoding='UTF-8' ) as arquivoNomes:
    for linha in arquivoNomes:
        separaString.append(linha.strip().split(' - '))

novo_conteudo = conteudo

for index, string in enumerate(separaString):
    novo_conteudo = novo_conteudo.replace(separaString[index][0], separaString[index][1])

with open('../docs/produtos_nomeResumido.txt', 'w', encoding='UTF-8') as arquivoEscrita:
    arquivoEscrita.write(novo_conteudo)