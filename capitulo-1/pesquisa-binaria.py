"""
Código de pesquisa binária em python
"""

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2,
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9]
lista_nomes = ['Ana', 'Bruno', 'Carlos', 'Daniel', 'Eduardo', 'Fernanda']

print(pesquisa_binaria(minha_lista, 9)) # => 4
print(pesquisa_binaria(minha_lista, -1)) # => None

print(pesquisa_binaria(lista_nomes, 'Carlos')) # => 2
print(pesquisa_binaria(lista_nomes, 'Zé')) # => None

# Fim