import pyautogui
from datetime import datetime, timedelta
import re
import math
import pyperclip

# left
xlnome = 837
ylnome = 275

xlcodigo = 829
ylcodigo = 290

xlprecoG = 824
ylprecoG = 320

# right
xrnome = 1050
yrnome = 275

xrcodigo = 1043
yrcodigo = 290

xrprecoG = 1037
yrprecoG = 320

vetorNome = []
vetorCodigo = []
vetorData = []
vetorprecoKG = []
vetorPrecoG = []

num_linhas_arquivo = 0

pyautogui.keyDown('alt')
pyautogui.press(['tab'])
pyautogui.keyUp('alt')


def transformarData(oldData):
    if oldData == '':
        oldData = '0'
    hoje = datetime.today()
    futuro = hoje + timedelta(days=int(oldData))
    newData = futuro.strftime("%d-%m-%Y")
    return newData


def transformarGrama(preco):
    return preco/10


def formatPreco(preco):
    return "{:.2f}".format(preco)


def reiniciarXY():
    global ylnome, ylcodigo, ylprecoG, yrnome, yrcodigo, yrprecoG
    ylnome = 275
    ylcodigo = 290
    ylprecoG = 320
    yrnome = 275
    yrcodigo = 290
    yrprecoG = 320

    
def _workaround_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    pyperclip.copy('')


with open('../docs/produtos_nomeResumido.txt', 'r', encoding='UTF-8') as arquivo:
    for linha in arquivo:
        codigo = linha.split(',')[0].replace('"', '').lstrip('0')
        nome = re.sub(r'\b(A GRANEL|ABSOLUT|GRANEL)\b', '',
                      linha.split(',')[1].replace('"', ''))
        oldData = linha.split(',')[2].replace('"', '')
        newData = transformarData(oldData)
        precoKG = linha.split(',')[3].replace('"', '').rstrip('\n')
        precoKG = float(precoKG)
        precoG = transformarGrama(precoKG)
        vetorCodigo.append(codigo)
        vetorNome.append(nome)
        vetorData.append(newData)
        vetorPrecoG.append(formatPreco(precoG))
        vetorprecoKG.append(formatPreco(precoKG))
        num_linhas_arquivo += 1

it = 0

for i in range(math.ceil(num_linhas_arquivo/14)):
    for j in range(7):
        pyautogui.click(xlnome, ylnome, duration=0.1)
        _workaround_write(vetorNome[it])
        pyautogui.click(xlcodigo, ylcodigo, duration=0.1)
        _workaround_write(vetorCodigo[it])
        pyautogui.click(xlprecoG, ylprecoG, duration=0.1)
        _workaround_write(vetorPrecoG[it])
        for k in range(8):
            pyautogui.press('right')
        _workaround_write(vetorprecoKG[it])
        pyautogui.press('up')
        _workaround_write(vetorData[it])
        ylnome += 90
        ylcodigo += 90
        ylprecoG += 90

        it += 1
        # Definindo valores para o próximo produto
        pyautogui.click(xrnome, yrnome, duration=0.1)
        _workaround_write(vetorNome[it])
        pyautogui.click(xrcodigo, yrcodigo, duration=0.1)
        _workaround_write(vetorCodigo[it])
        pyautogui.click(xrprecoG, yrprecoG, duration=0.1)
        _workaround_write(vetorPrecoG[it])
        for k in range(8):
            pyautogui.press('right')
        _workaround_write(vetorprecoKG[it])
        pyautogui.press('up')
        _workaround_write(vetorData[it])
        yrnome += 90
        yrcodigo += 90
        yrprecoG += 90
        it += 1
    pyautogui.press(['pgdn'])
    reiniciarXY()


for linha in range(2):

    init = 326
    for linha in range(5):
        pyautogui.click(727, init, duration=0.1)
        init += 150
        print(init)

    init = 326
    for linha in range(3):
        pyautogui.click(727, init, duration=0.1)
        init += 150
        print(init)

arquivo.close()
