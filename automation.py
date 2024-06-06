import yfinance
import pyautogui
import pyperclip
import webbrowser
import time


ticker = input("Digite o codigo da ação: ")

dataYf = yfinance.Ticker(ticker).history(start="2023-01-01", end=("2023-12-31"))
fechamento =dataYf.Close

cotacaoMaxima = round(fechamento.max(), 2)
cotacaoMinima = round(fechamento.min(), 2)
media = round(fechamento.mean(), 2)

destianatario = input("Digite o E-mail do destinatario: ")
assunto = "testando email"
mensagem = f"""
Aqui estão os dados q vc me pediu,

Cotações da ação:{ticker}

Cotaçao maxima:    R${cotacaoMaxima}
Cotaçõa minima:    R${cotacaoMinima}
Media de Cotações :R${media}

tmj.
"""

webbrowser.open("www.gmail.com")
time.sleep(3)

# config uma pausa de 3 segundos
pyautogui.PAUSE = 3

pyautogui.click(x=2023, y=225)


# ecolher o destinatario
pyperclip.copy(destianatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar o assunto
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar a msg
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# clicar no botão enviar
pyautogui.click(x=3220, y=1050)

# fechar  aba do email
pyautogui.hotkey("ctrl", "f4")

print("Email enviado corretamente")


# achar as coordenadas da tela
# time.sleep(2)
# clicar = pyautogui.position()



# print(cotacaoMaxima)
# print(cotacaoMinima)
# print(media)
# print(clicar)


