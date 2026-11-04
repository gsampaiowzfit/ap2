from exe2 import inverter_palavras

def test_inverter_varias_palavras():
   assert inverter_palavras("Olá mundo, estamos na aula de teste") == "teste de aula na estamos mundo, Olá" 
   
def test_inverter_uma_palavra():
   assert inverter_palavras("Olá") == "Olá"
   
def test_inverter_frase_vazia():
    assert inverter_palavras("") == "A frase não pode ser vazia ou nula."
    
def test_inverter_frase_espacos_extras():
    assert inverter_palavras("   Olá mundo   ") == "   mundo Olá   "
    
def test_inverter_frase_numeros_letras():
    assert inverter_palavras("123 abc 456") == "456 abc 123"