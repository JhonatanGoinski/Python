import pyautogui
import time

# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar -> pyautogui.hotkey
# scroll (rolar) -> pyautogui.scroll

# Damos a função para existir um pause de 1seg a cada comando 
pyautogui.PAUSE = 0.5   
# apertar a tecla do windows 
pyautogui.press("win")
# Digitar o nome do navegador "chrome"
pyautogui.write("chrome")
# apertar enter 
pyautogui.press("enter")
# digitar link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
# apertar enter 
pyautogui.press("enter")

# espera 3 segundos para continuar a execução 
time.sleep(3)

#login
#clicar para acessar o campo do e-mail 
pyautogui.click(x=3324, y=505)
#escrever o e-mail do login
pyautogui.write("jhonatan@gmail.com")
#passar de campo com o tab
pyautogui.press("tab")
#excrever senha 
pyautogui.write("senha")
#clicar no botão para logar 
pyautogui.click(x=3614, y=706)

# espera 3 segundos para continuar a execução 
time.sleep(3)

#Instalação da biblioteca Pandas para a obter dados BD
#pip install pandas numpy openpyxl
import pandas 

#ler base de dados e trazer para o python 

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: 
    #clicar para acessar o primeiro campo do cadastro
    pyautogui.click(x=3501, y=369)

    #preencher o campo com o dado fornecido
    #pegando a informção de cada linha
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #preencher o campo com o dado fornecido
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")


    #preencher o campo com o dado fornecido
    pyautogui.write(tabela.loc[linha, "tipo"])
    #seguir para o proximo campo 
    pyautogui.press("tab")
    #preencher o campo com o dado fornecido
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    #seguir para o proximo campo 
    pyautogui.press("tab")
    #preencher o campo com o dado fornecido
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    #seguir para o proximo campo 
    pyautogui.press("tab")
    #preencher o campo com o dado fornecido
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    #seguir para o proximo campo 
    pyautogui.press("tab") 

    #preencher o campo com o dado fornecido
    #pyautogui.write(str(tabela.loc[linha, "obs"]))
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
      pyautogui.write(obs)  
    #seguir para o proximo campo 
    pyautogui.press("tab")
    #Enviar Formulario
    pyautogui.press("enter")
    #Iniciar rolagem da pagina
    pyautogui.scroll(-1000)
    pyautogui.scroll(2000)