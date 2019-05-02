#!/usr/bin/env python3
import os
import datetime
from ferramentas import *
from proxy import GERENCIADOR
DIR_FILES = '/etc/sshiptv/'
#if not os.path.isdir(DIR_FILES): os.mkdir(DIR_FILES)
class MENU:
	def __init__(self):
		self.dados = None
		self.opcoes = {}
		self.running = False
	def __create_option(self, num=0, text=None):
		if not self.opcoes.get(num):
			self.opcoes[num] = text
		print('[%02d] - %s' % (num, text))
	def __view_banner(self):
		print('='*22 + '[MENU]' + '='*22)
		print('PROJECT: SSHIPTV           VERSION: 1.0')
		print('DATE CREATED: 21/04/2019   BY: @GlEmYsSoN')
		print('='*50)
	def __view_main(self):
		self.__create_option(1, 'GERENCIAR PROXY')
		self.__create_option(2, 'CRIAR USUARIO')
		self.__create_option(3, 'ALTERAR USUARIO')
		self.__create_option(4, 'DELETAR USUARIO')
		self.__create_option(5, 'MOSTRAR USUARIOS')
		self.__create_option(0, 'SAIR')
	def __get_input_option(self):
		if not self.running: self.running = True
		while self.running:
			try:
				option = int(input('Escolha uma opcao: '))
			except KeyboardInterrupt:
				self.running = False
				return
			except:
				print('Error: Esta opcao e invalida!')
				continue
			if option > len(self.opcoes):
				print('Error: Esta opcao e invalida!')
			else:
				self.running = False
		return option
	def __exec_option(self, option):
		if option == 0: return
		elif option == 1:
			gere = GERENCIADOR()
			return gere.run()
		elif option == 2:
			criar = CRIAR_USUARIO()
			return criar.criar()
		elif option == 3:
			alterar = ALTERAR_SENHA()
			return alterar.run()
		elif option == 4:
			deletar = DELETAR_USUARIOS()
			return deletar.run()
		elif option == 5:
			mostrar_usuarios()
			return True
	def __sleep(self):
		input('Enter para continuar...')
	def run(self):
		self.running = True
		while self.running:
			os.system('clear')
			self.__view_banner()
			self.__view_main()
			opcao = self.__get_input_option()
			if opcao is not None:
				self.running = True
				if self.__exec_option(opcao):
					self.__sleep()
				else:
					self.running = False
			else:
				self.running = False
def main():
	menu = MENU()
	menu.run()
if __name__ == "__main__":
	main()