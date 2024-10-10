class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.limite = "Não definido"
        self.valor_total = 0
        self.despesas = []

    def get_nome(self):
        return self.nome
    
    def get_limite(self):
        return self.limite
    
    def get_valor_total(self):
        return self.valor_total
    
    def get_despesas(self):
        return self.despesas
    
    def set_limite(self, limite):
        self.limite = limite

    def add_despesas(self, despesa):
        self.despesas.append(despesa)
        self.valor_total += despesa.get_valor()
    
    def print_categoria(self):
        print(f'{self.nome}')
        print('')
        print(f'Limite: R$ {self.limite}')
        print(f'Valor Total: R$ {self.valor_total}')
        print(f'Despesas: ')
        print('')
        