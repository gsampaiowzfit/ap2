def inverter_palavras(frase: str):
    
    if frase is None or frase.strip() == "":
        return "A frase não pode ser vazia ou nula."

    palavras = frase.split(" ")
    
    palavras.reverse()
    
    frase_invertida = " ".join(palavras)
    
    return frase_invertida