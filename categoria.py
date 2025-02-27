class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.limite = "Não definido"
        self.valor_total = 0
        self.limite_ultrapassado = "Não"
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
        self.set_limite_ultrapassado()

    def set_limite_ultrapassado(self):
        if self.limite != "Não definido":
            if self.valor_total > self.limite:
                self.limite_ultrapassado = "SIM!"

    def add_despesas(self, despesa):
        self.despesas.append(despesa)
        self.valor_total += despesa.get_valor()
    
    def print_categoria(self):
        print(f"{self.nome}")
        print("")
        print(f"Limite: R$ {self.limite}")
        print(f"Valor Total: R$ {self.valor_total:.2f}")
        print(f"Limite Ultrapassado: {self.limite_ultrapassado}")
        print(f"Despesas: ")
        print("")
        