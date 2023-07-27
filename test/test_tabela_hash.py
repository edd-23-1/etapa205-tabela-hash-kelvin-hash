# ATENÇÃO: Não altere o código desse arquivo
import os.path
import sys
from tabela_hash import TabelaHashEnderecamentoAberto

#Constantes
OCUPADO = 1
VAZIO = -1
LIBERADO = -2

# ---- INÍCIO: teste dos métodos insert() e get()

def test_insert_get_sem_colisao(): # 3pts
    try:
        exists = os.path.exists("tabela_hash.py")
        assert exists == True
    except:
        sys.exit()

    tabela_hash = TabelaHashEnderecamentoAberto(7)

    result = tabela_hash.insert(1,"valor1")
    result = tabela_hash.insert(2,"valor2")
    result = tabela_hash.insert(3,"valor3")
    result = tabela_hash.insert(4,"valor4")

    expected = True
    assert result == expected

    result = tabela_hash.get(1).dado
    tabela_hash.display()
    expected = "valor1"
    assert result == expected   

    result = tabela_hash.get(2).dado
    expected = "valor2"
    assert result == expected

    result = tabela_hash.get(3).dado
    expected = "valor3"
    assert result == expected

    result = tabela_hash.get(4).dado
    expected = "valor4"
    assert result == expected

def test_insert_get_com_colisao1(): # 4pts

    try:
        exists = os.path.exists("tabela_hash.py")
        assert exists == True
    except:
        sys.exit()

    tabela_hash = TabelaHashEnderecamentoAberto(7)

    result = tabela_hash.insert(74,"valor1")
    result = tabela_hash.insert(92,"valor2")
    result = tabela_hash.insert(32,"valor3")
    result = tabela_hash.insert(70,"valor4")
    result = tabela_hash.insert(47,"valor5")

    expected = True
    assert result == expected

    result = tabela_hash.get(74).dado
    expected = "valor1" 
    assert result == expected

    result = tabela_hash.get(92).dado
    expected = "valor2"
    assert result == expected

    result = tabela_hash.get(32).dado
    expected = "valor3"
    assert result == expected

    result = tabela_hash.get(70).dado
    expected = "valor4"
    assert result == expected

    result = tabela_hash.get(47).dado
    expected = "valor5"
    assert result == expected

def test_insert_get_com_colisao2_e_sobrescrita(): # 4pts
    try:
        exists = os.path.exists("tabela_hash.py")
        assert exists == True
    except:
        sys.exit()

    tabela_hash = TabelaHashEnderecamentoAberto(7)

    result = tabela_hash.insert(74,"valor1")
    result = tabela_hash.insert(92,"valor2")
    result = tabela_hash.insert(32,"valor3")
    result = tabela_hash.insert(70,"valor4")
    result = tabela_hash.insert(32,"valor5")

    tabela_hash.display()

    expected = True
    assert result == expected

    result = tabela_hash.get(32).dado
    expected = "valor5"
    assert result == expected

# ---- FIM: teste dos métodos insert() e get()



# ---- INÍCIO: teste método get e chave inválida() - 1pt

def test_get_com_chave_invalida():

    try:
        exists = os.path.exists("tabela_hash.py")
        assert exists == True
    except:
        sys.exit()

    tabela_hash = TabelaHashEnderecamentoAberto(1)
    
    tabela_hash.insert(1,"valor1")
    tabela_hash.insert(2,"valor2")
    tabela_hash.insert(3,"valor3")
    
    result = tabela_hash.get(4)
    expected = None

    assert result == expected

# ---- FIM: teste método get e chave inválida()



# ---- INÍCIO: teste método remove() - 6pts

def test_remove_true():

    try:
        exists = os.path.exists("tabela_hash.py")
        assert exists == True
    except:
        sys.exit()

    tabela_hash = TabelaHashEnderecamentoAberto(7)

    tabela_hash.insert(1,"valor1")
    tabela_hash.insert(2,"valor2")
    tabela_hash.insert(3,"valor3")
    tabela_hash.insert(4,"valor4")

    result = tabela_hash.remove(1)

    expected = True
    assert result == expected

def test_remove_chave_invalida():

    try:
        exists = os.path.exists("tabela_hash.py")
        assert exists == True
    except:
        sys.exit()

    tabela_hash = TabelaHashEnderecamentoAberto(7)

    tabela_hash.insert(1,"valor1")
    tabela_hash.insert(2,"valor2")
    tabela_hash.insert(3,"valor3")
    tabela_hash.insert(4,"valor4")

    result = tabela_hash.remove(10)

    expected = False
    assert result == expected

# ---- FIM: teste método remove()



# ---- INÍCIO: teste método display() - 2pts

def test_display_com_elementos_string():
    try:
        exists = os.path.exists("tabela_hash.py")
        assert exists == True
    except:
        sys.exit()

    tabela_hash = TabelaHashEnderecamentoAberto(7)

    tabela_hash.insert(1,"valor1")
    tabela_hash.insert(2,"valor2")
    tabela_hash.insert(3,"valor3")

    result = tabela_hash.display()

    expected = [
        (None, None, VAZIO),
        (1, "valor1", OCUPADO),
        (2, "valor2", OCUPADO),
        (3, "valor3", OCUPADO),
        (None, None, VAZIO),
        (None, None, VAZIO),
        (None, None, VAZIO),
    ]

    assert result == expected

def test_display_com_elementos_int():
    try:
        exists = os.path.exists("tabela_hash.py")
        assert exists == True
    except:
        sys.exit()

    tabela_hash = TabelaHashEnderecamentoAberto(7)

    tabela_hash.insert(1, 3)
    tabela_hash.insert(2, 2)
    tabela_hash.insert(3, 1)

    result = tabela_hash.display()
    expected = [
        (None, None, VAZIO),
        (1, 3, OCUPADO),
        (2, 2, OCUPADO),
        (3, 1, OCUPADO),
        (None, None, VAZIO),
        (None, None, VAZIO),
        (None, None, VAZIO),
    ]

    assert result == expected

def test_display_com_pos_liberada():
    try:
        exists = os.path.exists("tabela_hash.py")
        assert exists == True
    except:
        sys.exit()

    tabela_hash = TabelaHashEnderecamentoAberto(7)

    tabela_hash.insert(1, 3)
    tabela_hash.insert(2, 2)
    tabela_hash.insert(3, 1)
    tabela_hash.remove(2)

    result = tabela_hash.display()
    expected = [
        (None, None, VAZIO),
        (1, 3, OCUPADO),
        (2, 2, LIBERADO),
        (3, 1, OCUPADO),
        (None, None, VAZIO),
        (None, None, VAZIO),
        (None, None, VAZIO),
    ]

    assert result == expected

def test_display_com_tabela_vazia():
    try:
        exists = os.path.exists("tabela_hash.py")
        assert exists == True
    except:
        sys.exit()

    tabela_hash = TabelaHashEnderecamentoAberto(7)

    result = tabela_hash.display()
    expected = []

    assert result == expected

# ---- FIM: teste método display()


