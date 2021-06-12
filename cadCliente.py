# Objective: read VGLGui workflow file and load content into memory
# File type: structure.txt

#
import re
import os
import string
from collections import defaultdict

class Cliente(object):

    def __init__(self, nome, cpf, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def setTelefone(self, telefone):
        self.telefone = telefone

    def getTelefone(self):
        return self.telefone

    def setEndereco(self, endereco):
        self.Endereco = endereco

    def getEndereco(self):
        return self.endereco

    def getCPF(self):
        return self.cpf

class Venda(object):
    def __init__(self, cliente, plano, valor):
        self.cliente = cliente
        self.plano = plano
        self.valor = valor

    def getCliente(self):
        return self.cliente

    def setCliente(self, cliente):
        self.cliente = cliente

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def getPlano(self):
        return self.plano

    def setPlano(self, plano):
        self.plano = plano

def cadastrar(lista):
    nome = input('Informe o nome: ')
    cpf = input('Informe o cpf: ')
    endereco = input('Informe o endereço: ')
    telefone = input('Informe o telefone: ')
    cli = Cliente(nome, int(cpf), endereco, int(telefone))
    lista.append(cli)

def exibir(lista):
    for cli in lista:
        print('Nome: ' + cli.getNome())
        print('Endereço: ' + cli.getEndereco())
        print('Telfone: ' + str(cli.getTelefone()))
        print('CPF: ' + str(cli.getCPF()))

def alterar(lista, cpf):
    cont = 0
    for cli in lista:
        if cli.getCPF() == int(cpf):
            print('Nome: ' + cli.getNome())
            print('Endereço: ' + cli.getEndereco())
            print('Telfone: ' + str(cli.getTelefone()))
            print('CPF: ' + str(cli.getCPF()))
            confirmacao = input('Confirma Alteração [S/N] ')
        if confirmacao.upper() == 'S':
            nome = input('Informe o nome: ')
            cpf = input('Informe o cpf: ')
            endereco = input('Informe o endereço: ')
            telefone = input('Informe o telefone: ')
            cli = Cliente(nome, int(cpf), endereco, int(telefone))
            lista[cont] = cli
            cont = cont +1

def excluir(lista, cpf):
    for cli in lista:
        if cli.getCPF() == int(cpf):
            print('Nome: ' + cli.getNome())
            print('Endereço: ' + cli.getEndereco())
            print('Telfone: ' + str(cli.getTelefone()))
            print('CPF: ' + str(cli.getCPF()))
            confirmacao = input('Confirma Exclusão [S/N]? ')
            if confirmacao.upper() == 'S':
                lista.remove(cli)

def menu():
    print('1- Cadastrar Cliente')
    print('2- Exibir Cliente')
    print('3- Alterar Cliente')
    print('4- Excluir Cliente')
    print('5- Realizar Venda')
    print('6- Exibir Venda')
    print('7- Sair')
    opcao = input('')
    return opcao

def consultarCliente(listaCliente, cpf):
    for cli in listaCliente:
        if cli.getCPF() == int(cpf):
            return cli
        return None

def realizarVenda(listaCliente,listaVenda):
    plano = input('Informe o Plano: ')
    val = input('Informe o Valor: ')
    cpf= input('Informe CPF: ')
    cliente = consultarCliente(listaCliente, cpf)
    if cliente != None:
        venda = Venda(cliente, plano, val)
        listaVenda.append(venda)
    else:
        print('Cliente Inválido!')

def exibirVenda(listaVenda):
    for venda in listaVenda:
        print('Plano: ' + venda.getPlano())
        print('Valor: ' + venda.getValor())
        print('Nome do CLiente: ' + venda.getCliente().getNome())

# programa principal

op = 0
listaCliente = []
listaVenda = []
while op != '7':
    op = menu()
    if op == '1':
        cadastrar(listaCliente)
    elif op == '2':
        exibir(listaCliente)
    elif op == '3':
        cpf = input('Informe CPF: ')
        alterar(listaCliente, cpf)
    elif op == '4':
        cpf = input('Informe CPF: ')
        excluir(listaCliente, cpf)
    elif op == '5':
        realizarVenda(listaCliente, listaVenda)
    elif op == '6':
        exibirVenda(listaVenda)
    elif op =='7':
        print('Saindo …')
    else:
        print('Opção Inválida!')