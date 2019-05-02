#!/usr/bin/env python3
import os
from . import USUARIOS
class DELETAR_USUARIOS:
	def __init__(self):
		self.usuarios = self.__get_users()
		self.opcoes = {}
		self.running = False
		self.data = USUARIOS()
	def __get_users(self):
		users = []
		for line in open('/etc/passwd').readlines():
			if int(line.split(':')[2]) >= 1000 and line.split(':')[0] != 'nobody':
				users.append(line.split(':')[0])
		return users
	def __view_banner(self):
		print('='*13 + '[MENU - DELETAR USUARIO]' + '='*13)
		print('TOTAL: %02d                      BY: @GlEmYsSoN' % (len(self.usuarios)))
		print('='*50)
	def __create_option(self):
		num = 0
		for user in self.usuarios:
			num += 1
			self.opcoes[num] = user
			print('[%02d] - %s' % (num, user))
		print('[00] - VOLTAR')
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
			if option > len(self.usuarios):
				print('Error: Esta opcao e invalida!')
			else:
				self.running = False
		return option
	def __kill_pid(self, user):
		cmd = 'ps -u %s' % user
		for linha in os.popen(cmd).readlines():
			pid = linha.split()[0]
			if pid != 'PID':
				os.kill(int(pid), 15)
	def __exec_option(self, option):
		user = self.opcoes[option]
		data = self.data._open()
		if data.get(user):
			data.pop(user)
			self.data._write(data)
		self.__kill_pid(user)
		cmd = 'userdel --force %s' % user
		os.system(cmd)
		print('Usuario %s deletado!' % user)
		self.usuarios = self.__get_users()
		self.opcoes.pop(option)
		return True
	def __sleep(self):
		input('Enter para continuar...')
	def run(self):
		while True:
			os.system('clear')
			self.__view_banner()
			self.__create_option()
			opcao = self.__get_input_option()
			if opcao == 0: return True
			if opcao is None: return
			if self.__exec_option(opcao): self.__sleep()