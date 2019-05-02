#!/usr/bin/env python3
import datetime
import os
from . import USUARIOS
NEW_USER = 'Novo usuario: '
PASSWORD = 'Senha: '
VALIDITY = 'Validade: '
LIMIT = 'Limite: '
ERROR = 'Error: %s'
def _input(msg):
	try:
		data = input(msg)
	except KeyboardInterrupt:
		return False
	if data:
		return data
	return None
class CRIAR_USUARIO:
	def __init__(self):
		self.running = False
		self.data = USUARIOS()
	def __verify_user(self, user):
		for linha in open('/etc/passwd').readlines():
			if linha.split(':')[0] == user.lower():
				return True
	def __get_name(self):
		name = None
		while not name:
			name = _input(NEW_USER)
			if name is False: return
			if not name:
				print(ERROR % 'Nome invalido!')
			elif len(name) < 3:
				print(ERROR % 'Nome muito pequeno!')
				name = None
			elif not name.isalnum():
				print(ERROR % 'Use numeros e letras!')
				name = None
			elif self.__verify_user(name):
				print(ERROR % 'Usuario ja existe!')
				name = None
		return name
	def __get_password(self):
		password = None
		while not password:
			password = _input(PASSWORD)
			if password is False: return
			if not password:
				print(ERROR % 'Senha invalido!')
			elif len(password) < 3:
				print(ERROR % 'Senha muito pequena!')
				password = None
			elif not password.isalnum():
				print(ERROR % 'Use numeros e letras!')
				password = None
		return password
	def __get_expiration_date(self):
		validity = None
		while not validity:
			validity = _input(VALIDITY)
			if validity is False: return
			if validity.isnumeric():
				if int(validity) <= 0:
					print(ERROR % 'Use um valor maior que zero')
					validity = None
				else:
					hoje = datetime.datetime.now()
					futuro = datetime.timedelta(days=int(validity))
					return str(hoje + futuro).split()[0].split('-')
			else:
				print(ERROR % 'Use apenas numeros!')
				validity = None
	def __get_limit_connection(self):
		limit = None
		while not limit:
			limit = _input(LIMIT)
			if limit is False: return
			if limit.isnumeric():
				if int(limit) <= 0:
					print(ERROR % 'Use um valor maior que zero')
					limit = None
				else:
					return int(limit)
			else:
				print(ERROR % 'Use apenas numeros!')
				limit = None
	def criar(self):
		print('='*14 + '[MENU - CRIAR USUARIO]' + '='*14)
		print('='*50)
		nome = self.__get_name()
		if nome:
			senha = self.__get_password()
			if senha:
				validade = self.__get_expiration_date()
				if validade:
					limite = self.__get_limit_connection()
					data = self.data._open()
					data[nome] = {
						'senha': senha,
						'validade': '-'.join(validade),
						'limite': limite
					}
					self.data._write(data)
					cmd = 'useradd -M -s /bin/false %s -e %s;'
					cmd += '(echo %s; echo %s) | passwd %s 1>/dev/null 2>/dev/null'
					os.system(cmd % (
						nome, '-'.join(validade),
						senha, senha, nome
					))
					validade.reverse()
					print('='*40)
					print('-'*40)
					print('USUARIO CRIADO COM SUCESSO!')
					print('-'*40)
					print('Usuario: ' + nome)
					print('Senha: ' + senha)
					print('Validade: ' + '/'.join(validade))
					print('Limite: %02d' % limite)
					print('='*40)
					return True