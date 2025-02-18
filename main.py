from datetime import date

from sistema import Sistema
from despesa import Despesa

mes = int("01")

despesa1 = Despesa("Escola", "Educação", 1000, date(2024, mes, 10))
despesa2 = Despesa("Conta de Luz", "Energia", 500, date(2024, mes, 10))
despesa3 = Despesa("Conta de Água", "Água", 300, date(2024, mes, 10))
despesa4 = Despesa("Aluguel", "Residência", 1500, date(2024, mes, 10))
despesa5 = Despesa("Plano de Celular", "Internet", 80, date(2024, mes, 10))
despesa6 = Despesa("Compra do Mês", "Alimentação", 1500, date(2024, mes, 10))
despesa7 = Despesa("Gasolina", "Transporte", 300, date(2024, mes, 10))
despesa8 = Despesa("Ingresso para jogo de Futebol", "Entreterimento", 100, date(2024, mes, 10))

sistema = Sistema()

sistema.get_controle_financeiro().add_despensa_categoria(despesa1, "Educação")
sistema.get_controle_financeiro().add_despensa_categoria(despesa2, "Energia")
sistema.get_controle_financeiro().add_despensa_categoria(despesa3, "Água")
sistema.get_controle_financeiro().add_despensa_categoria(despesa4, "Residência")
sistema.get_controle_financeiro().add_despensa_categoria(despesa5, "Internet")
sistema.get_controle_financeiro().add_despensa_categoria(despesa6, "Alimentação")
sistema.get_controle_financeiro().add_despensa_categoria(despesa7, "Transporte")
sistema.get_controle_financeiro().add_despensa_categoria(despesa8, "Entreterimento")

def main():
    sistema.run()

if __name__ == "__main__":
    main()
