from exe5 import acessar_sistema
from unittest.mock import Mock, patch

def test_permissao_autorizada():
    mock_verificar_permissao = Mock(return_value=True)

    with patch("exe5.verificar_permissao", mock_verificar_permissao):
        resultado = acessar_sistema("João")

    assert resultado == "Acesso autorizado"
    
def test_permissao_negada():
    mock_verificar_permissao = Mock(return_value=False)

    with patch("exe5.verificar_permissao", mock_verificar_permissao):
        resultado = acessar_sistema("Maria")

    assert resultado == "Acesso negado"
    
def test_verificar_permissao_chamado():
    mock_verificar_permissao = Mock(return_value=True)

    with patch("exe5.verificar_permissao", mock_verificar_permissao):
        acessar_sistema("João")

    assert mock_verificar_permissao.call_count > 0
    
def test_verificar_usuario_correto():
    mock_verificar_permissao = Mock(return_value=True)

    with patch("exe5.verificar_permissao", mock_verificar_permissao):
        acessar_sistema("Maria")

    mock_verificar_permissao.assert_called_with("Maria")
    
def test_verificar_dois_cenarios():
    mock_verificar_permissao = Mock(side_effect=[True, False])

    with patch("exe5.verificar_permissao", mock_verificar_permissao):
        resultado1 = acessar_sistema("João")
        resultado2 = acessar_sistema("Maria")

    assert resultado1 == "Acesso autorizado"
    assert resultado2 == "Acesso negado"
