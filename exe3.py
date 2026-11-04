def validar_documento(documento: str):
    documento_sem_formatacao = documento.replace(".", "").replace("-", "")
    
    if len(documento_sem_formatacao) != 11 or not documento_sem_formatacao.isdigit():
        return False
    else:
        return True
    