def disponivel(estoque, titulo):
    return estoque.get(titulo, 0) > 0