from unittest.mock import Mock, patch
from exe4 import criar_identificacao

def test_criar_identificacao_mensagem_correta():
    mock_gerar_codigo = Mock(return_value="123456")

    with patch("exe4.gerar_codigo", mock_gerar_codigo):
        resultado = criar_identificacao("João")

    assert resultado == "Usuário João cadastrado com o código 123456."
    
def test_gerar_codigo_chamado():
    mock_gerar_codigo = Mock(return_value="ABC123")

    with patch("exe4.gerar_codigo", mock_gerar_codigo):
        criar_identificacao("Maria")

    assert mock_gerar_codigo.call_count > 0
    
def test_gerar_codigo_uma_vez():
    mock_gerar_codigo = Mock(return_value="ABC123")
    
    with patch("exe4.gerar_codigo", mock_gerar_codigo):
        criar_identificacao("Maria")

    assert mock_gerar_codigo.call_count == 1
    
def test_nomes_diferentes():
    mock_gerar_codigo = Mock(return_value="ABC123")
    
    with patch("exe4.gerar_codigo", mock_gerar_codigo):
        resultado = criar_identificacao("Maria")

    assert resultado == "Usuário Maria cadastrado com o código ABC123."
    
    with patch("exe4.gerar_codigo", mock_gerar_codigo):
        resultado = criar_identificacao("João")

    assert resultado == "Usuário João cadastrado com o código ABC123."

