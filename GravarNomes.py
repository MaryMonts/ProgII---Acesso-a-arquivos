#-*-coding:latin1-*-
#print ('******************************************************************')
#print ('******      Programação II - 2° Ciclo - Jogos Digitais      ******')
#print ('******      Nome: Mariana Montovani  RA: 1430961711032      ******')
#print ('******      Programa:  Listar nomes e gravar em arquivo     ******')
#print ('******************************************************************')

arquivo = open('texto.txt', 'w')
linha = ""
while (linha.lower() != "sair"):
    linha = raw_input("Digite um nome: ")
    arquivo.write(linha+ '\n')
    arquivo.flush()
arquivo.close()
