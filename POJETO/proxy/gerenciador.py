#!/usr/bin/env python3
import os
import json
class GERENCIADOR:
	def __init__(self):
		self.info_session = self.__status_session()
		self.opcoes = {}
	def __write_data(self, data):
		with open('proxy/config.json', 'w') as e:
			e.write(json.dumps(data, indent=4))
		e.close()
	def __status_session(self):
		return json.loads(open('proxy/config.json').read())
	def __proxy_stop(self):
		if self.info_session['session']:
			try:
				os.kill(self.info_session['pid'], 7)
			except:
				pass
			self.info_session['session'] = False
			self.info_session['pid'] = None
			self.__write_data(self.info_session)
			return True
		else:
			return False
	def __proxy_start(self):
		if self.info_session['session']:
			return False
		else:
			cmd = 'screen -md python3 proxy/proxy.py 1>/dev/null 2>/dev/null'
			os.system(cmd)
			return True
	def __create_options(self):
		self.opcoes['01'] = '[01] - INICIAR PROXY'
		self.opcoes['02'] = '[02] - PARAR PROXY'
		self.opcoes['00'] = '[00] - VOLATR'
		print(self.opcoes['01'])
		print(self.opcoes['02'])
		print(self.opcoes['00'])
	def __input_option(self):
		while True:
			try:
				opcao = int(input('Escolha uma opcao: '))
				if opcao == 0: return None
				if opcao > len(self.opcoes):
					print('Error: Essa opcao e invalida')
				else:
					return opcao
			except KeyboardInterrupt: return False
	def __sleep(self):
		input('Enter pra continuar...')
	def __exec_option(self, opcao):
		if opcao == 1:
			if self.__proxy_start():
				print('Proxy iniciado com sucesso')
				self.__sleep()
			else:
				print('Proxy ja esta funcionando...')
				self.__sleep()
		elif opcao == 2:
			if self.__proxy_stop():
				print('Proxy parado com sucesso')
				self.__sleep()
			else:
				print('Proxy ja esta parado...')
				self.__sleep()
	def run(self):
		while True:
			os.system('clear')
			self.__create_options()
			opcao = self.__input_option()
			if opcao is None:
				return True
			elif opcao is False:
				return False
			else:
				self.__exec_option(opcao)
				self.info_session = self.__status_session()
