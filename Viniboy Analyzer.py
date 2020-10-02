#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ap.py
#  
#  Copyright 2020 Rafael <Rafael@DESKTOP-KEP74PC>
#  

import os

def limpaTela():
	# Limpa a tela do terminal
	
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
		
def ehInteiro(num):
	# True: Número inteiro / False: Número decimal
	
	return (num // 1) == num
		

def processaDados(linha, cantos):
	# Calcula total de cantos de cada time, média, além de 
	# over, under e push com relação à linha apresentada
	
	over = 0
	under = 0
	push = 0
	
	total = sum(cantos)
	media = total / len(cantos)
	
	for num in cantos:
		if num > linha:
			over = over + 1
		elif num < linha:
			under = under + 1
		else:
			push = push + 1
			
	return (media, over, under, push, total)
	

def verificaTendencia(linha, cantos_casa, cantos_fora):
	media_casa, over_casa, under_casa, push_casa, total_casa = processaDados(linha, cantos_casa)
	media_fora, over_fora, under_fora, push_fora, total_fora = processaDados(linha, cantos_fora)
	
	if media_casa > linha and media_fora > linha:
		if over_casa > under_casa and over_fora > under_fora:
			c1 = (over_casa + over_fora) / (len(cantos_casa) + len(cantos_fora)) >= 0.6
			c2 = (over_casa / len(cantos_casa) >= 0.7) or (over_fora / len(cantos_fora) >= 0.7)
			c3 = (under_casa / len(cantos_casa) <= 0.3) and (under_fora / len(cantos_fora) <= 0.3)
			if c1 or c2 or c3:
				return "Over"
				
	elif media_casa < linha and media_fora < linha:
		if under_casa > over_casa and under_fora > over_fora:
			c1 = (under_casa + under_fora) / (len(cantos_casa) + len(cantos_fora)) >= 0.6
			c2 = (under_casa / len(cantos_casa) >= 0.7) or (under_fora / len(cantos_fora) >= 0.7)
			c3 = (over_casa / len(cantos_casa) <= 0.3) and (over_fora / len(cantos_fora) <= 0.3)
			if c1 or c2 or c3:
				return "Under"
	
	return "Nenhum"
	
	
def imprimeRelatorio(jogo, linha, cantos_casa, cantos_fora):
	# Faz a impressão formatada dos dados na tela do terminal ao final
	# do processamento de cada jogo
	
	media_casa, over_casa, under_casa, push_casa, total_casa = processaDados(linha, cantos_casa)
	media_fora, over_fora, under_fora, push_fora, total_fora = processaDados(linha, cantos_fora)
	
	print("\nJogo: " + jogo)
	print("Linha: %.1f" % linha)
	
	print("\nTime mandante: ")
	print("Média cantos/jogo: {:.2f}".format(media_casa))
	print("Over {}: {}/{} ({:.1f}%)".format(linha, over_casa, len(cantos_casa), (over_casa/len(cantos_casa))*100))
	print("Under {}: {}/{} ({:.1f}%)".format(linha, under_casa, len(cantos_casa), (under_casa/len(cantos_casa))*100))
	if ehInteiro(linha):
		print("Push {}: {}/{} ({:.1f}%)".format(linha, push_casa, len(cantos_casa), (push_casa/len(cantos_casa))*100))
	
	print("\nTime visitante: ")
	print("Média cantos/jogo: {:.2f}".format(media_fora))
	print("Over {}: {}/{} ({:.1f}%)".format(linha, over_fora, len(cantos_fora), (over_fora/len(cantos_fora))*100))
	print("Under {}: {}/{} ({:.1f}%)".format(linha, under_fora, len(cantos_fora), (under_fora/len(cantos_fora))*100))
	if ehInteiro(linha):
		print("Push {}: {}/{} ({:.1f}%)\n".format(linha, push_fora, len(cantos_fora), (push_fora/len(cantos_fora))*100))
	
	print("\nAmbos times: ")
	print("Média cantos/jogo: {:.2f}".format((total_casa + total_fora) / (len(cantos_casa) + len(cantos_fora))))
	print("Over {}: {}/{} ({:.1f}%)".format(linha, over_casa + over_fora, len(cantos_casa) + len(cantos_fora), ((over_casa + over_fora) / (len(cantos_casa) + len(cantos_fora)))*100))
	print("Under {}: {}/{} ({:.1f}%)".format(linha, under_casa + under_fora, len(cantos_casa) + len(cantos_fora), ((under_casa + under_fora) / (len(cantos_casa) + len(cantos_fora)))*100))
	if ehInteiro(linha):
		print("Push {}: {}/{} ({:.1f}%)".format(linha, push_casa + push_fora, len(cantos_casa) + len(cantos_fora), ((push_casa + push_fora) / (len(cantos_casa) + len(cantos_fora)))*100))
	else:
		print()
	

def salvaRelatorio(jogo, linha, cantos_casa, cantos_fora):
	# Salva o relatório de cada jogo no arquivo .txt indicado
	
	media_casa, over_casa, under_casa, push_casa, total_casa = processaDados(linha, cantos_casa)
	media_fora, over_fora, under_fora, push_fora, total_fora = processaDados(linha, cantos_fora)
	
	tendencia = verificaTendencia(linha, cantos_casa, cantos_fora)
	
	if tendencia != "Nenhum":
		arq = open("Jogos prováveis.txt", "a")
	else:
		arq = open("Outros jogos.txt", "a")

	arq.write("Jogo: " + jogo)
	arq.write("\nLinha: %.1f" % linha)
	
	arq.write("\n\nTime mandante: ")
	arq.write("\nMédia cantos/jogo: {:.2f}".format(media_casa))
	arq.write("\nOver {}: {}/{} ({:.1f}%)".format(linha, over_casa, len(cantos_casa), (over_casa/len(cantos_casa))*100))
	arq.write("\nUnder {}: {}/{} ({:.1f}%)".format(linha, under_casa, len(cantos_casa), (under_casa/len(cantos_casa))*100))
	if ehInteiro(linha):
		arq.write("\nPush {}: {}/{} ({:.1f}%)".format(linha, push_casa, len(cantos_casa), (push_casa/len(cantos_casa))*100))
	
	arq.write("\n\nTime visitante: ")
	arq.write("\nMédia cantos/jogo: {:.2f}".format(media_fora))
	arq.write("\nOver {}: {}/{} ({:.1f}%)".format(linha, over_fora, len(cantos_fora), (over_fora/len(cantos_fora))*100))
	arq.write("\nUnder {}: {}/{} ({:.1f}%)".format(linha, under_fora, len(cantos_fora), (under_fora/len(cantos_fora))*100))
	if ehInteiro(linha):
		arq.write("\nPush {}: {}/{} ({:.1f}%)\n".format(linha, push_fora, len(cantos_fora), (push_fora/len(cantos_fora))*100))
		
	arq.write("\n\nAmbos times: ")
	arq.write("\nMédia cantos/jogo: {:.2f}".format((total_casa + total_fora) / (len(cantos_casa) + len(cantos_fora))))
	arq.write("\nOver {}: {}/{} ({:.1f}%)".format(linha, over_casa + over_fora, len(cantos_casa) + len(cantos_fora), ((over_casa + over_fora) / (len(cantos_casa) + len(cantos_fora)))*100))
	arq.write("\nUnder {}: {}/{} ({:.1f}%)".format(linha, under_casa + under_fora, len(cantos_casa) + len(cantos_fora), ((under_casa + under_fora) / (len(cantos_casa) + len(cantos_fora)))*100))
	if ehInteiro(linha):
		arq.write("\nPush {}: {}/{} ({:.1f}%)".format(linha, push_casa + push_fora, len(cantos_casa) + len(cantos_fora), ((push_casa + push_fora) / (len(cantos_casa) + len(cantos_fora)))*100))
	else:
		arq.write("\n")

	arq.write("\n-----------------------------------------------------------------------\n\n")
	arq.close()

def main(args):
	print("Viniboy Analyzer v1.3\n")
	
	jogo = input("Jogo: ")
	
	while jogo != "":
		cantos_casa = []
		cantos_fora = []
		n = -1
		i = 1
		
		linha = float(input("Linha: "))
	
		print("\nTime mandante: \n")
		while n != 0:
			n = int(input("Cantos no jogo " + str(i) + ": "))
			if n != 0:
				cantos_casa.append(n)
			i = i+1
			
		n = -1
		i = 1
		print("\nTime visitante: \n")
		while n != 0:
			n = int(input("Cantos no jogo " + str(i) + ": "))
			if n != 0:
				cantos_fora.append(n)
			i = i+1
			
		
		imprimeRelatorio(jogo, linha, cantos_casa, cantos_fora)
		salvaRelatorio(jogo, linha, cantos_casa, cantos_fora)
		
		os.system("pause")
		limpaTela()
		jogo = input("Jogo: ")

	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
