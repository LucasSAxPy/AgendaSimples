#Limpa a tela do cmd, quando executado
from os import system, name

#Limpa a tela do cmd, quando executado
def limpa_tela():
	if name == "nt":
		_ = system('cls')
	else:
		_ = system('clear')

#Grava os contatos na lista de contatos
def salvar_contato(contatos, contato, telefone, email):
	contato_novo =  {"contato": contato, "telefone": telefone,\
									 "email": email, "favorito": False}
	contatos.append(contato_novo)
	limpa_tela()
	print(f"Foi adicionado o contato {contato}, com número {telefone}, email: {email}")

#Mostra os contatos que estão armazenados
def visualiza_contato(contatos):
	limpa_tela()
	print("\nSeus Contatos:")
	for index, contato in enumerate(contatos, start=1):
		favorito_mostrar = "★" if contato["favorito"] else " "
		nome_mostrar = contato["contato"]
		telefone_mostrar = contato["telefone"]
		email_mostrar = contato["email"]
		print(f"{index}. nome: {nome_mostrar} telefone: {telefone_mostrar} e-mail: {email_mostrar} {favorito_mostrar}")
	print("\n")

#Mostra os contatos que estão marcados como favoritos
def visualiza_contato_favorito(contatos):
	limpa_tela()
	print('Contatos favoritos:')
	for index, contato in enumerate(contatos, start=1):
		if contato['favorito']:
			favorito_mostrar = "★" if contato["favorito"] else " "
			nome_mostrar = contato["contato"]
			telefone_mostrar = contato["telefone"]
			email_mostrar = contato["email"]
			print(f"{index}. nome: {nome_mostrar} telefone: {telefone_mostrar} e-mail: {email_mostrar} {favorito_mostrar}")
		else:
			pass
	print("\n")

#Altera as informações de um contato selecionado
def editar_contato(contatos, index, nome, tel, email):
	index_verdadeiro = index - 1
	try:
		contatos[index_verdadeiro]["contato"] = nome
		contatos[index_verdadeiro]["telefone"] = tel
		contatos[index_verdadeiro]["email"] = email
		limpa_tela()
		print(f"O nome é {nome} telefone é {tel}, email é {email}")
	except IndexError:
		print("Contato não encontrado!")

#Torna um contato favorito
def marca_favorito(contatos, index):
	index_verdadeiro = index - 1
	contatos[index_verdadeiro]['favorito'] = True
	limpa_tela()
	print("O contato se tornou favorito.")

#Desmarca um contato que estiver como favorito
def desmarca_favorito(contatos, index):
	index_verdadeiro = index - 1
	contatos[index_verdadeiro]['favorito'] = False
	limpa_tela()
	print("O contato foi desfavoritado.")

#Exclui um contato através do índice
def deleta_contato(contatos, index):
	index_verdadeiro = index - 1
	try:
		contatos.remove(contatos[index_verdadeiro])
		print("Contato foi deletado com sucesso!")
	except IndexError:
		print("Contato não encontrado!")