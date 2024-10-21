from datetime import date

from despesa import Despesa
from controle_financeiro import ControleFinanceiro
from fpdf import FPDF

class Sistema:
    def __init__(self):
        self._mes_anterior = []
        self._controle_financeiro = ControleFinanceiro()
        self._continuar = False
        self._operacoes = [
            self.add_despesa,
            self.set_limite_categoria,
            self.print_gasto_mes,
            self.print_diferenca_meses,
            self.gerar_pdf_gasto_mes,
            self.fechar_mes,
            self.finalizar_programa
        ]
    
    def run(self):
        self._continuar = True
        
        while self._continuar:
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
            self._operacoes[op - 1]()
    
    def add_despesa(self):
        print("Cadastro Despesa")
        descricao = self.input_str("Descrição: ")
        print("")
        print("Categorias")
        for key in self._controle_financeiro.categorias.keys():
            print(f"- {key}")
        print("")
        categoria = self.input_categoria()
        valor = self.input_float("Valor: R$ ")
        dia, mes, ano = self.input_data("Data (DD/MM/AAAA): ")
        data = date(ano, mes, dia)
        despesa = Despesa(descricao, categoria.get_nome(), valor, data)
        self._controle_financeiro.add_despensa_categoria(despesa, categoria.get_nome())
        categoria.set_limite_ultrapassado()
        print("Despesa cadastrada com sucesso!")
        print("")

    def set_limite_categoria(self):
        print("Definir Limite de uma Categoria")
        print("Categorias")
        for key in self._controle_financeiro.categorias.keys():
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
        for values in self._controle_financeiro.categorias.values():
            values.print_categoria()
            for despesa in values.despesas:
                despesa.print_despesa()
        print("")

    def print_diferenca_meses(self):
        if len(self._mes_anterior) != 0:
            print("Comparação Percentual Meses")
            print("")
            for keys in self._controle_financeiro.categorias.keys():
                percentual, valor_bruto = self.diferenca_categorias_meses(keys)
                print(keys)
                print(f"- Percentual: {percentual}")
                print(f"- Valor Bruto: {valor_bruto}")
                print("")
            
    def gerar_pdf_gasto_mes(self):
        pdf = FPDF()
        
        pdf.compress = False
        pdf.add_page()
        pdf.set_font("Arial", "", 30)
        pdf.write(5, "Controle Financeiro Mês") 
        for categorias in self._controle_financeiro.categorias.values():
            pdf.ln(20)
            pdf.set_font("Arial", "", 20)
            pdf.write(5, f"{categorias.get_nome()}")
            pdf.ln(10)
            pdf.set_font("Arial", "", 15)
            pdf.write(5, f"- Gasto Total: R$ {categorias.get_valor_total():.2f}")
            pdf.ln(10)
            pdf.write(5, "- Despesas:")
            for despesas in categorias.get_despesas():
                pdf.ln(10)
                pdf.set_font("Arial", "", 14)
                pdf.write(5, f"=> {despesas.get_descricao()}: R$ {despesas.get_valor():.2f} ({despesas.get_data()})")

        pdf.add_page()
        pdf.set_font("Arial", "", 30)
        pdf.write(5, "Comparação Percentual Meses") 
        for keys in self._controle_financeiro.categorias.keys():
                pdf.ln(20)
                percentual, valor_bruto = self.diferenca_categorias_meses(keys)
                pdf.set_font("Arial", "", 20)
                pdf.write(5, f"{keys}")
                pdf.ln(10)
                pdf.set_font("Arial", "", 15)
                pdf.write(5, f"- Percentual: {percentual}")
                pdf.ln(8)
                pdf.write(5, f"- Valor Bruto: {valor_bruto}")

        pdf.output("controle_financeiro.pdf", "")
        print("PDF gerado com sucesso!")
        print("")

    def fechar_mes(self):
        self._mes_anterior.clear()
        self._mes_anterior.append(self._controle_financeiro)
        self._controle_financeiro = ""
        self._controle_financeiro = ControleFinanceiro()
        print("Mês fechado com sucesso!")
        print("")

    def finalizar_programa(self):
        print("Programa Finalizado")
        
        self._continuar = False

    def diferenca_categorias_meses(self, categoria):
        atual = self._controle_financeiro.categorias[categoria].get_valor_total()
        if len(self._mes_anterior) == 0:
            return "Sem informações sobre o mês anterior", "Sem informações sobre o mês anterior"
        anterior = self._mes_anterior[0].categorias[categoria].get_valor_total()
        if anterior == 0:
            return "Sem gasto no mês anterior", "Sem gasto no mês anterior"
        if atual == 0:
            return "- 100%", "Sem gasto no mês atual"
        calc_percentual = (atual / anterior) * 100
        if calc_percentual < 100:
            percentual = f" - {100 - calc_percentual:.2f}%"
            valor_bruto = f" R$ - {anterior - atual:.2f}"
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
            categoria = self._controle_financeiro.get_categoria(nome_categoria)
            if categoria != None:
                return categoria
            
    def get_controle_financeiro(self):
        return self._controle_financeiro
    