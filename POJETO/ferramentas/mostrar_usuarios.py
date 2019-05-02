#!/usr/bin/env python3
from . import USUARIOS
LINHA_INFO = '===============[INFO. USUARIOS]==================\n'
LINHA_INFO += 'USUARIO       SENHA         VALIDADE     LIMITE'
LINHA_INFO += '\n-------------------------------------------------'
LINHA_LOG = '%-13s %-13s %-13s %-13s'
USUARIOS_ATUAL = set([
    line.split(':')[0] if int(line.split(':')[2]) >= 1000 and line.split(':')[0] != 'nobody'\
    else '' \
    for line in open('/etc/passwd').readlines()
])
def mostrar_usuarios():
    dados = USUARIOS()._open()
    print(LINHA_INFO)
    for key in dados.keys():
        info = dados[key]
        v = info['validade'].split('-')
        v.reverse()
        print(LINHA_LOG % (
            key, info['senha'],
            '/'.join(v), info['limite']
        ))
    print('-------------------------------------------------')
    return True