from categoria import Categoria

class ControleFinanceiro:
    def __init__(self):
        self.categorias = {
        "Educação": Categoria('Educação'),
        "Energia": Categoria('Energia'),
        "Água": Categoria('Água'),
        "Internet": Categoria('Internet'),
        "Alimentação": Categoria('Alimentação'),
        "Transporte": Categoria('Transporte'),
        "Residencia": Categoria('Residência'),
        "Entreterimento": Categoria('Entreterimento'),
        }

    def get_categoria(self, categoria):
        self.categorias.get()
        return self.categorias[categoria]
    
    def add_despensa_categoria(self, despesa, categoria):
        for key in self.categorias.keys():
            if categoria == key:
                categoria.add_despesas(despesa)