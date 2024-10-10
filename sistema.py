from datetime import date

from despesa import Despesa
from controle_financeiro import ControleFinanceiro


class Sistema:
    def __init__(self):
        self.mes_anterior = []
        self.controle_financeiro = ControleFinanceiro()
        self.operacoes = [

        ]
    
    def run(self):
        flags = True
        
        while flags:
            print('Controle Financeiro')
            print('Menu Operações')
            print('1 - Cadastro Despesa')
            print('2 - Definir Limite de uma Categoria')
            print('3 - Visualização Gastos Mês')
            print('4 - Comparar Gastos com Mês anterior')
            print('5 - Exportar Dados para PDF')
            print('6 - Terminar o Mês')
            print('7 - Finalizar Programa')

        op = self.input_int('Digite a operação: ')
        print('')
        self.operacoes[op]()
    
    def add_despesa(self):
        print('Cadastro Despesa')
        descricao = self.input_str('Descrição: ')
        print('')
        print('Categorias')
        for key in self.controle_financeiro.categorias.keys():
            print(f'- {key}')
        print('')
        categoria = self.input_categoria()
        valor = self.input_float('Valor: R$ ')
        dia, mes, ano = self.input_str('Data (DD/MM/AAAA): ').split('/')
        data = date(ano, mes, dia)
        despesa = Despesa(descricao, categoria.get_nome(), valor, data)
        self.controle_financeiro.add_despensa_categoria(despesa, categoria)
        print('Despesa cadastrada com sucesso!')

    def set_limite_categoria(self):
        print('Definir Limite de uma Categoria')
        for key in self.controle_financeiro.categorias.keys():
            print(f'{key}')
        print('')
        categoria = self.input_categoria()
        limite = self.input_float('Limite: R$ ')
        categoria.set_limite(limite)
        print('Limite definido com sucesso!')
    
    def print_gasto_mes(self):
        print('Gasto Mês Atual')
        print('')

    def input_str(self, text):
        while True:
            try:
                return input(text)
            except:
                print('*Valor não válido*')

    def input_int(self, text):
        while True:
            try:
                return int(input(text))
            except:
                print('*Valor não válido*')
    
    def input_float(self, text):
        while True:
            try:
                return float(input(text))
            except:
                print('*Valor não válido*')
    
    def input_categoria(self):
        while True:
            nome_categoria = self.input_str('Categoria: ').strip().title()
            categoria = self.controle_financeiro.get_categoria(nome_categoria)
            if categoria != None:
                return categoria