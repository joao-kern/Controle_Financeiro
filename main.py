from datetime import date

from sistema import Sistema
from despesa import Despesa

mes = int("01")

despesa1 = Despesa("Escola", "Educação", 1000, date(2024, mes, 10))
despesa2 = Despesa("Conta de Luz", "Energia", 500, date(2024, mes, 10))
despesa3 = Despesa("Conta de Água", "Água", 300, date(2024, mes, 10))
despesa4 = Despesa("Aluguel", "Residência", 1500, date(2024, mes, 10))

sistema = Sistema()

sistema.controle_financeiro.add_despensa_categoria(despesa1, "Educação")
sistema.controle_financeiro.add_despensa_categoria(despesa2, "Energia")
sistema.controle_financeiro.add_despensa_categoria(despesa3, "Água")
sistema.controle_financeiro.add_despensa_categoria(despesa4, "Residência")

def main():
    sistema.run()

if __name__ == "__main__":
    main()
