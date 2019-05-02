#!/usr/bin/env python3
class CRIAR_BARRA:
    def __init__(self, size=60, colorText=1, colorBar=2):
        self.size = size
        self.cores = ['\033[1;3%dm' % x for x in range(0, 8)]
        self.colorText = colorText
        self.colorBar = colorBar
    def criar(self, text):
        bar = '=' * int((self.size - len(text)) / 2 - 2)
        barra = '{bar}{text}{bar}'.format(
            bar=self.cores[self.colorBar] + bar,
            text='%s[%s]' % (
                self.cores[self.colorText],
                text
            )
        )
        print(barra + self.cores[7])
class CRIAR_OPCOES:
    def __init__(self):
        self.crlf = '\r\n'
        self.seq = 0
        self.objs = []
        self.funcoes = {}
    def addFun(self, funcName, opcao):
        self.funcoes[opcao] = funcName
    def exec_option(self, option):
        eval(self.funcoes[option])()
    def addText(self, text):
        self.seq += 1
        self.objs.append('[%02d] - %s' % (
            self.seq, text
        ))
    def total(self):
        return len(self.objs)
    def view(self):
        print(self.crlf.join(self.objs))
def print_nome():
    nome = input('Qual seu nome? ')
    print(nome)
CRIAR_BARRA().criar('MENU')
cr = CRIAR_OPCOES()
cr.addFun('print_nome', 1)
cr.addText('NOME')
cr.view()
op = int(input('Escolha uma opcao: '))
if op == 1: cr.exec_option(op)