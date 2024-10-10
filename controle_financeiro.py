from categoria import Categoria

class ControleFinanceiro:
    def __init__(self):
        self.categorias = {
        "Educação": Categoria("Educação"),
        "Energia": Categoria("Energia"),
        "Água": Categoria("Água"),
        "Internet": Categoria("Internet"),
        "Alimentação": Categoria("Alimentação"),
        "Transporte": Categoria("Transporte"),
        "Residência": Categoria("Residência"),
        "Entreterimento": Categoria("Entreterimento"),
        }

    def get_categoria(self, categoria):
        return self.categorias[categoria]
    
    def add_despensa_categoria(self, despesa, nome_categoria):
        self.categorias[nome_categoria].add_despesas(despesa)