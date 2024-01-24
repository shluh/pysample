# https://algoritmosempython.com.br/cursos/algoritmos-python/estruturas-dados/arvores/
# https://pythonhelp.wordpress.com/2015/01/19/arvore-binaria-de-busca-em-python/
class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        print('self esquerda',self.esquerda)
        print('self esquerda chave',self.esquerda.chave)
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave ,
                                    self.chave,
                                    self.direita and self.direita.chave)
    

raiz = NodoArvore(3)
raiz.esquerda = NodoArvore(5)
raiz.direita  = NodoArvore(1)
print(raiz)