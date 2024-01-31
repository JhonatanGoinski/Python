# 1 - Indicar caminho para e-mail (passo a passo) 
# 2 - Indicar o link para o direcionamento do navegador 
# 3 - Indicar caminho para escrever novo e-mail 
# 4 - Indicar os dados da tabela para excutar na função 
# 5 - Indicar os campos e associar com as informações corretas da tabela

import pyautogui
import time

pyautogui.PAUSE = 0.2

#Indicação para o navegador 
pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

#Indicação do link (e-mial)
time.sleep(1)
link = "https://mail.google.com/mail/u/0/#inbox"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(4)
# pyautogui.click(x=4744, y=191)
# pyautogui.click(x=4438, y=559)

import pandas 

lista = pandas.read_csv("lista.csv")
for linha in lista.index:
    #Indicação para um criação de um novo e-mail
    pyautogui.click(x=2435, y=263)
    time.sleep(2)
    #Colocando informações para o envio do e-mail
    pyautogui.write(lista.loc[linha,"email"])
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.write(lista.loc[linha,"assunto"])
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.write(lista.loc[linha, "descricao"])
    pyautogui.press("tab")
    #enviar e-mail  
    pyautogui.press("enter")
    #Indicando retorno do scroll para um novo e-mail
    pyautogui.scroll(20000)

