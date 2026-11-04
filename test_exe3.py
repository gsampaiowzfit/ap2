from exe3 import validar_documento

def test_validar_documento_11digitos():
    assert validar_documento("12345678901") == True

def test_validar_documento_formatado():
    assert validar_documento("123.456.789-01") == True

def test_validar_documento_menos_11digitos():
    assert validar_documento("1234567890") == False

def test_validar_documento_mais_11digitos():
    assert validar_documento("123456789012") == False

def test_validar_documento_com_letras():
    assert validar_documento("1234567890a") == False
    
def test_validar_documento_vazio():
    assert validar_documento("") == False