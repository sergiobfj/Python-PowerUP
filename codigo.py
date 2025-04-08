import pyautogui # pyautogui permite controlar o mouse, teclado e tela
import time

pyautogui.PAUSE = 1 #Entre todos os comandos, ele vai pausar 1 segundo

# pyautogui.click
# pyautogui.press
# pyautogui.hotkey
# pyautogui.write

# Passo 1: Entrar no Sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login

# abrir o chrome
# digitar o site

pyautogui.press("win")
pyautogui.write("Navegador Opera GX")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Passo 2: Fazer login

#ir para email
pyautogui.press("tab")
pyautogui.write("sjunior1557@gmai.com")
time.sleep(0.5)

#ir para senha
pyautogui.press("tab")
pyautogui.write("123")
time.sleep(0.5)

#ir para login
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2.5) 

# Passo 3: Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
pyautogui.press("tab")


# Passo 4: Cadastrar 1 produto  

codigo = "MOLO000251"
pyautogui.write(codigo)    
pyautogui.press("tab")

marca = "Logitech"
pyautogui.write(marca)
pyautogui.press("tab")

tipo = "Mouse"
pyautogui.write(tipo)
pyautogui.press("tab")

categoria = "1"
pyautogui.write(categoria)
pyautogui.press("tab")

preco_unitario = "25.95"
pyautogui.write(preco_unitario)
pyautogui.press("tab")

custo = "6.50"
pyautogui.write(custo)
pyautogui.press("tab")

obs = ''
pyautogui.write(obs)
pyautogui.press("tab")

pyautogui.press("enter")
pyautogui.press("home")
pyautogui.click(x=200, y=200)

# Passo 5: Repetir para todos os produtos

for linha in tabela.index: # para cada linha da minha tabela...  
    time.sleep(0.5)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.press("home")
    pyautogui.click(x=200, y=200)
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)


