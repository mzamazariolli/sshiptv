#!/usr/bin/env python3
import json
class USUARIOS:
	def __init__(self):
		self.file = '/etc/usuarios/usuarios.json'
		self.data = {
		}
	def _open(self):
		try:
			with open(self.file) as e:
				data = e.read()
				if data:
					self.data = json.loads(data)
			e.close()
			return self.data
		except:
			return None
	def _write(self, data=None):
		if data is None:
			data = self.data
		try:
			with open(self.file, 'w') as e:
				e.write(json.dumps(data, indent=4))
			e.close()
		except:
			return False
from .alterar_senha import *
from .criar_usuarios import *
from .deletar_usuarios import *
from .mostrar_usuarios import mostrar_usuarios