class Despesa:
    def __init__(self, descrição, categoria, valor, data):
        self.descricao = descrição
        self.categoria = categoria
        self.valor = valor
        self.data = data
        

    def get_categoria(self):
        return self.categoria
    
    def get_valor(self):
        return self.valor
    
    def get_data(self):
        return self.data.strftime("%d/%m/%y")

    def get_descricao(self):
        return self.descricao

    def print_despesa(self):
        print(f"- Descrição: {self.descricao}")
        print(f"- Valor: R$ {self.valor}")
        print(f"- Data: {self.data.strftime("%d/%m/%y")}")
        print("")