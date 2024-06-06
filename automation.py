import yfinance
import pyautogui
# import pyperclip
import webbrowser
import time

destianatario = "tassio50000@gmail.com"
assunto = "testando email"
mensagem = "marcao lindao"

# ticker = input("Digite o codigo da ação: ")

dataYf = yfinance.Ticker("PETR4.SA").history(start="2023-01-01", end=("2023-12-31"))
fechamento =dataYf.Close

cotacaoMaxima = round(fechamento.max(), 2)
cotacaoMinima = round(fechamento.min(), 2)
media = round(fechamento.mean(), 2)

webbrowser.open("www.gmail.com")
time.sleep(3)

pyautogui.click(x=2023, y=225)
time.sleep(10)

clicar = pyautogui.position()



print(cotacaoMaxima)
print(cotacaoMinima)
print(media)
print(clicar)


