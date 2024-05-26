#Uma agenda com funções de salvar, editar, deletar
#e marcar um contato como favorito

#Importa as funções utilizadas de um outro arquivo
from modulos import *

#Cria uma lista de contatos, vazia, e limpa a tela
contatos = []
limpa_tela()

#Bloco de repetição do programa
while True:

#Mostra o layout e opções de escolha para o úsuario
	print("-"*20 + "Agenda" + "-"*20)
	print("  1- Salvar contato")
	print("  2- Editar contato")
	print("  3- Deletar contato")
	print("  4- Marcar/Desmarcar favorito")
	print("  5- Visualizar contatos")
	print("  6- Sair da agenda")

#Armazena o resultado escolhido
	try:
		operacao = int(input("Qual operação deseja realizar: "))
	except ValueError:
		limpa_tela()
		print("Valor inválido!")
		continue

#Caso escolha a primeira opção
	if operacao == 1:

#Armazena as informações necessarias para criar um contato
		try:
			nome = input("Nome do contato: ")
			telef = int(input("Telefone: "))
			email = input("E-mail: ")
			salvar_contato(contatos, nome, telef, email)
		except ValueError:
			print("Digito inválido!")

#Caso escolha a segunda opção
	elif operacao == 2:

#Armazena os resultados para alterar o contato escolhido pelo índice
		visualiza_contato(contatos)
		try:
			index_atualiza = int(input("Número do contato que deseja atualiza: "))
			nome_novo = input("Nome: ")
			tel_novo = int(input("Telefone: "))
			email_novo = input("E-mail: ")
			editar_contato(contatos, index_atualiza,nome_novo, tel_novo, email_novo)
		except ValueError:
			print("Digito inválido!")

#Caso escolha a terceira opção
	elif operacao == 3:

#Armazena o índice e exclui o item deste
		visualiza_contato(contatos)
		try:
			index_atualiza = int(input("Número do contato que deseja deletar: "))
			deleta_contato(contatos, index_atualiza)
		except ValueError:
			print("Digito inválido")

#Caso escolha a quarta opção
	elif operacao == 4:

#Escolhe entre marcar ou desmarcar um contato favorito
		print("  1- Marcar favorito")
		print("  2- Desmarcar favorito")
		try:
			resposta = int(input("Escolha qual deseja: "))

#Armazena o índice e marca o contato como favorito
			if resposta == 1:
				visualiza_contato(contatos)
				index_atualiza = int(input("Número do contato que deseja tornar favorito: "))
				marca_favorito(contatos, index_atualiza)

#Armazena o índice e desmarca o contato de favorito
			elif resposta == 2:
				visualiza_contato_favorito(contatos)
				index_atualiza = int(input("Número do contato que deseja desfavoritar: "))
				desmarca_favorito(contatos, index_atualiza)
			else:
				print("Digito inválido!")
		except ValueError:
			print("Digito inválido!")
			pass
		except IndexError:
			print("Contato não encontrado!")
			pass

#Caso escolha a quinta opção
	elif operacao == 5:

#Escolha entra visualizar todos os contatos ou somente os favoritos
		print("  1- Visualizar todos os contatos")
		print("  2- Visualizar só favoritos")
		try:
			resposta = int(input("Escolha qual deseja: "))

#Mostra todos os contatos
			if resposta == 1:
				visualiza_contato(contatos)

#Mostra somente os contatos favoritos
			elif resposta == 2:
				visualiza_contato_favorito(contatos)
			else:
				print("Digito inválido!")
		except ValueError:
			print("Digito inválido!")

#Caso escolha a sexta opção
	elif operacao == 6:

#Para o loop, ou seja o programa encerra
		break

#Trata caso escolha uma opção não disponível
	else:
		limpa_tela()
		print("Opção inválida!")