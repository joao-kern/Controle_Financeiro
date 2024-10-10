from datetime import date

from despesa import Despesa
from controle_financeiro import ControleFinanceiro

class Sistema:
    def __init__(self):
        self.mes_anterior = []
        self.controle_financeiro = ControleFinanceiro()
        self.continuar = False
        self.operacoes = [
            self.add_despesa,
            self.set_limite_categoria,
            self.print_gasto_mes,
            self.print_diferenca_meses,
            self.exportar_pdf,
            self.fechar_mes,
            self.finalizar_programa
        ]
    
    def run(self):
        self.continuar = True
        
        while self.continuar:
            print("Controle Financeiro")
            print("Menu Operações")
            print("1 - Cadastro Despesa")
            print("2 - Definir Limite de uma Categoria")
            print("3 - Visualização Gastos Mês")
            print("4 - Comparar Gastos com Mês anterior")
            print("5 - Exportar Dados para PDF")
            print("6 - Fechar o Mês")
            print("7 - Finalizar Programa")

            op = self.input_int("Digite a operação: ")
            print("")
            self.operacoes[op - 1]()
    
    def add_despesa(self):
        print("Cadastro Despesa")
        descricao = self.input_str("Descrição: ")
        print("")
        print("Categorias")
        for key in self.controle_financeiro.categorias.keys():
            print(f"- {key}")
        print("")
        categoria = self.input_categoria()
        valor = self.input_float("Valor: R$ ")
        dia, mes, ano = self.input_data("Data (DD/MM/AAAA): ")
        data = date(ano, mes, dia)
        despesa = Despesa(descricao, categoria.get_nome(), valor, data)
        self.controle_financeiro.add_despensa_categoria(despesa, categoria.get_nome())
        categoria.set_limite_ultrapassado()
        print("Despesa cadastrada com sucesso!")
        print("")

    def set_limite_categoria(self):
        print("Definir Limite de uma Categoria")
        print("Categorias")
        for key in self.controle_financeiro.categorias.keys():
            print(f"- {key}")
        print("")
        categoria = self.input_categoria()
        limite = self.input_float("Limite: R$ ")
        categoria.set_limite(limite)
        print("Limite definido com sucesso!")
        print("")
    
    def print_gasto_mes(self):
        print("Gasto Mês Atual")
        print("")
        for values in self.controle_financeiro.categorias.values():
            values.print_categoria()
            for despesa in values.despesas:
                despesa.print_despesa()

    def print_diferenca_meses(self):
        if len(self.mes_anterior) != 0:
            print("Comparação Percentual Meses")
            print("")
            for keys in self.controle_financeiro.categorias.keys():
                percentual, valor_bruto = self.diferenca_categorias_meses(keys)
                print(keys)
                print(f"- Percentual: {percentual}")
                print(f"- Valor Bruto: {valor_bruto}")
                print("")
            
    def exportar_pdf(self):
        pass

    def fechar_mes(self):
        self.mes_anterior.clear()
        self.mes_anterior.append(self.controle_financeiro)
        self.controle_financeiro = ""
        self.controle_financeiro = ControleFinanceiro()
        print("Mês fechado com sucesso!")

    def finalizar_programa(self):
        print("Programa Finalizado")
        self.continuar = False

    def diferenca_categorias_meses(self, categoria):
        atual = self.controle_financeiro.categorias[categoria].get_valor_total()
        anterior = self.mes_anterior[0].categorias[categoria].get_valor_total()
        if anterior == 0:
            return "Sem gasto no mês anterior", "Sem gasto no mês anterior"
        if atual == 0:
            return "- 100%", "Sem gasto no mês atual"
        calc_percentual = (atual / anterior) * 100
        if calc_percentual < 100:
            percentual = f" - {100 - calc_percentual:.2f}%"
            valor_bruto = f" R$  - {anterior - atual:.2f}"
            return percentual, valor_bruto
        percentual = f" + {calc_percentual - 100:.2f} %"
        valor_bruto = f" R$ {atual - anterior:.2f}"
        return percentual, valor_bruto
    
    def input_str(self, text):
        while True:
            try:
                return input(text)
            except:
                print("*Valor não válido*")

    def input_int(self, text):
        while True:
            try:
                return int(input(text))
            except:
                print("*Valor não válido*")
    
    
    def input_float(self, text):
        while True:
            try:
                return float(input(text))
            except:
                print("*Valor não válido*")
    
    def input_data(self, text):
        while True:
            try:
                return (int(x) for x in (input(text).split("/")))
            except:
                print("*Valor não válido*")

    def input_categoria(self):
        while True:
            nome_categoria = self.input_str("Categoria: ").strip().title()
            categoria = self.controle_financeiro.get_categoria(nome_categoria)
            if categoria != None:
                return categoria