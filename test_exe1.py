from exe1 import classificar_produto

def test_classificar_produto_sem_estoque():
    assert classificar_produto(0) == "Sem estoque"

def test_classificar_produto_estoque_baixo():
    assert classificar_produto(3) == "Estoque baixo"

def test_classificar_produto_estoque_normal():
    assert classificar_produto(10) == "Estoque normal"

def test_classificar_produto_estoque_alto():
    assert classificar_produto(25) == "Estoque alto"

def test_classificar_produto_quantidade_invalida():
    assert classificar_produto(-1) == "Quantidade inválida"
