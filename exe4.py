def gerar_codigo():
    pass    

def criar_identificacao(nome: str) -> str:
    codigo = gerar_codigo()
    
    return f"Usuário {nome} cadastrado com o código {codigo}."