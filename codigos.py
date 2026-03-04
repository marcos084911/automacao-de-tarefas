import pyautogui
import time

# pyautogui.click > clica
# pyautogui.write > escreve um texto
# pyautogui.press > aperta uma tecla
# pyautogui.hotkey > aperta um atalho

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.PAUSE = 1

# passo 1: entra no sistema
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.write(link)
pyautogui.press('enter')

# fazer uma pausa pro site
time.sleep(2)

# passo 2: fazer login
pyautogui.click(x=1303, y=344)
pyautogui.write('texte0012@gmail.com')
pyautogui.press('tab')
pyautogui.write('1234')
pyautogui.press('tab')
pyautogui.press('enter')

# fazer uma pausa pro site
time.sleep(2)

# passo 3: abrir a base de dados
import pandas

tabela = pandas.read_csv(r'C:\Users\Markim\Documents\projetos-py\automacoes-de-tarefaas\produtos.csv')
print(tabela)

# passo 4: cadastrar todos os produto
for linha in tabela.index:
    #codigo
    pyautogui.click(x=1220, y=251)
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    #marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')

    #tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')

    #categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    #preco_unitario
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    #custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    #obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')

    #voltar para o inicio
    pyautogui.scroll(1000)

    #c\