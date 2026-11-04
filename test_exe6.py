from exe6 import atender_proximo_cliente
from unittest.mock import patch, Mock


def test_sucesso():
    mock_obter_proximo_cliente = Mock(return_value="Cliente 1")
    mock_registrar_atendimento = Mock(return_value=True)
    
    with patch('exe6.obter_proximo_cliente', mock_obter_proximo_cliente),patch('exe6.registrar_atendimento', mock_registrar_atendimento):
        resultado = atender_proximo_cliente()
        
        assert resultado == "Atendimento realizado"
        
def test_fila_vazia():
    mock_obter_proximo_cliente = Mock(return_value=None)
    
    with patch('exe6.obter_proximo_cliente', mock_obter_proximo_cliente):
        resultado = atender_proximo_cliente()
        
        assert resultado == "Fila vazia"
        
def test_falha_atendimento():
    mock_obter_proximo_cliente = Mock(return_value="Cliente 1")
    mock_registrar_atendimento = Mock(side_effect=Exception("Erro ao registrar atendimento"))
    
    with patch('exe6.obter_proximo_cliente', mock_obter_proximo_cliente),patch('exe6.registrar_atendimento', mock_registrar_atendimento):
        resultado = atender_proximo_cliente()
        
        assert resultado == "Falha no atendimento"
        
def test_obter_proximo_cliente_chamado():
    mock_obter_proximo_cliente = Mock(return_value="Cliente 1")
    mock_registrar_atendimento = Mock(return_value=True)
    
    with patch('exe6.obter_proximo_cliente', mock_obter_proximo_cliente),patch('exe6.registrar_atendimento', mock_registrar_atendimento):
        atender_proximo_cliente()
        
        assert mock_obter_proximo_cliente.called
        
def test_registrar_atendimento_chamado_cliente_correto():
    mock_obter_proximo_cliente = Mock(return_value="Cliente 1")
    mock_registrar_atendimento = Mock(return_value=True)

    with patch('exe6.obter_proximo_cliente', mock_obter_proximo_cliente),patch('exe6.registrar_atendimento', mock_registrar_atendimento):
        atender_proximo_cliente()

        mock_registrar_atendimento.assert_called_with("Cliente 1")
        
def test_registrar_atendimento_nao_chamado_fila_vazia():
    mock_obter_proximo_cliente = Mock(return_value=None)
    mock_registrar_atendimento = Mock(return_value=True)

    with patch('exe6.obter_proximo_cliente', mock_obter_proximo_cliente),patch('exe6.registrar_atendimento', mock_registrar_atendimento):
        atender_proximo_cliente()

        assert not mock_registrar_atendimento.called