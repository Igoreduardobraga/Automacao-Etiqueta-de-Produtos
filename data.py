import pyautogui
from datetime import datetime, timedelta
arquivofinal = open('produtos.txt', 'w')
from time import sleep

pyautogui.keyDown('alt')
pyautogui.press(['tab'])
pyautogui.keyUp('alt')

# left
xlnome = 837
ylnome = 275

xlcodigo = 829
ylcodigo = 290

xlprecoG = 825
ylprecoG = 305

xlprecoKG = 879
ylprecoKG = 305

xlvalidade = 881
ylvalidade = 291

# right
xrnome = 1050
yrnome = 275

xrcodigo = 1043
yrcodigo = 290

xrprecoG = 1038
yrprecoG = 305

xrprecoKG = 1093
yrprecoKG = 305

xrvalidade = 1093
yrvalidade = 291

for i in range(10):
    for k in range(8):
        pyautogui.click(xlnome,ylnome,duration=0.2)
        pyautogui.click(xlcodigo,ylcodigo,duration=0.2)
        pyautogui.click(xlprecoG,ylprecoG,duration=0.2)
        pyautogui.click(xlprecoKG,ylprecoKG,duration=0.2)
        pyautogui.click(xlvalidade,ylvalidade,duration=0.2)
        ylnome += 74
        ylcodigo += 75
        ylprecoG += 75
        ylprecoKG += 75
        ylvalidade += 75
        pyautogui.click(xrnome,yrnome,duration=0.2)
        pyautogui.click(xrcodigo,yrcodigo,duration=0.2)
        pyautogui.click(xrprecoG,yrprecoG,duration=0.2)
        pyautogui.click(xrprecoKG,yrprecoKG,duration=0.2)
        pyautogui.click(xrvalidade,yrvalidade,duration=0.2)
        yrnome += 74
        yrcodigo += 75
        yrprecoG += 75
        yrprecoKG += 75
        yrvalidade += 75
    pyautogui.keyDown('ctrl')
    pyautogui.press(['pgdn'])
    pyautogui.keyUp('ctrl')
    ylnome = 410
    ylcodigo = 424
    ylprecoG = 441
    ylprecoKG = 441
    ylvalidade = 425
    yrnome = 411
    yrcodigo = 424
    yrprecoG = 441
    yrprecoKG = 441
    yrvalidade = 425


# for linha in range(2):

    # init = 326
    # for linha in range(5):
    #     pyautogui.click(727,init,duration=2)
    #     init += 150
    #     print(init)

    # init = 326
    # for linha in range(3):
    #     pyautogui.click(727,init,duration=2)
    #     init += 150
    #     print(init)


# with open('teste.txt', 'r', encoding='UTF-16') as arquivo:
#     for linha in arquivo:
#         codigo = linha.split(',')[0].replace('"', '').lstrip('0')
#         nome = linha.split(',')[1].replace('"', '')
#         oldData = linha.split(',')[2].replace('"', '')
#         if oldData == '':
#             oldData = '0'
#         hoje = datetime.today()
#         futuro = hoje + timedelta(days=int(oldData))
#         newData = futuro.strftime("%d-%m-%Y")
#         preco = linha.split(',')[3].replace('"', '')
#         pyautogui.click(1032,326, duration=1)
#         pyautogui.write(nome)
#         pyautogui.write(codigo)
        

# arquivofinal.close()
# arquivo.close()
