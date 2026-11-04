def obter_proximo_cliente():
    # Lógica para obter o próximo cliente
    pass

def registrar_atendimento(cliente):
    # Lógica para registrar o atendimento do cliente
    pass

def atender_proximo_cliente():
    try:
        cliente = obter_proximo_cliente()
    
        if cliente:
            atendimento = registrar_atendimento(cliente)
            
            if atendimento:
                return "Atendimento realizado"
        else:
            return "Fila vazia"
            
    except:
        return "Falha no atendimento"