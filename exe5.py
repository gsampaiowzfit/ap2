def verificar_permissao(usuario: str) -> bool:
    pass

def acessar_sistema(usuario: str) -> str:
    permissao = verificar_permissao(usuario)
    
    return "Acesso autorizado" if permissao else "Acesso negado"