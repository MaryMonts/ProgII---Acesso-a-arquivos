#-*-coding:latin1-*-
#print ('******************************************************************')
#print ('******      Programa��o II - 2� Ciclo - Jogos Digitais      ******')
#print ('******      Nome: Mariana Montovani  RA: 1430961711032      ******')
#print ('******      Programa: Leitura, Ordena��o e Escrita          ******')
#print ('******************************************************************')

arquivo = open('C:/Windows/WindowsUpdate.log', 'r')
conteudo = arquivo.readlines()


conteudo.sort(key=len, reverse=True)


arquivo = open('Ordenado.txt', 'w')
arquivo.writelines( conteudo )
arquivo.close()
