#!/usr/bin/env python3
import os
import threading
import json
from ferramentas import USUARIOS
def set_pid():
	data = open('limiter/config.json').read()
	data = json.loads(data)
	data['pid'] = os.getpid()
	data['session'] = True
	with open('limiter/config.json', 'w') as e:
		e.write(json.dumps(data, indent=4))
	e.close()
def kill_pid(pid):
	os.kill(int(pid), 15)
def get_users():
	with open('/etc/passwd') as e:
		users = []
		for line in e.readlines():
			if int(line.split(':')[2]) >= 1000 and line.split(':')[0] != 'nobody':
				users.append(line.split(':')[0])
	e.close()
	return users
class LIMITER:
	def __init__(self):
		self.usuarios = get_users()
		self.lock = threading.Lock()
		self.info_usuarios = USUARIOS()
		self.running = False
	def __get_pid_user(self, user):
		cmd = 'ps -u %s' % user
		output = [line.split()[0] for line in os.popen(cmd).readlines()]
		return output[1:]
	def __verify_limite(self, user):
		data = self.info_usuarios._open()
		if data.get(user):
			limite = data[user]['limite']
			pids = self.__get_pid_user(user)
			if limite >= len(pids):
				return pids[-(len(pids) - limite):]
			else:
				return False
	def __chk_session(self):
		data = open('limiter/config.json')
		json_data = json.loads(data.read())
		if not json_data['session']:
			self.close()
	def run(self):
		self.running = True
		while self.running:
			for usuario in self.usuarios:
				saida = self.__verify_limite(usuario)
				if saida:
					try:
						self.lock.acquire()
						for pid in saida:
							kill_pid(pid)
					finally:
						self.lock.release()
			self.__chk_session()
	def close(self):
		self.running = False
def main():
	data = LIMITER()
	set_pid()
	data.run()
if __name__ == "__main__":
	main()