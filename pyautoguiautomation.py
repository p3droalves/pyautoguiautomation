#!/usr/bin/env python
# coding: utf-8

# # Automação de Sistemas e Processos com Python
# 
# ### Desafio:
# 
# Para controle de custos, todos os dias, seu chefe pede um relatório com todas as compras de mercadorias da empresa.
# O seu trabalho, como analista, é enviar um e-mail para ele, assim que começar a trabalhar, com o total gasto, a quantidade de produtos compradas e o preço médio dos produtos.
# 
# E-mail do seu chefe: para o nosso exercício, coloque um e-mail seu como sendo o e-mail do seu chefe<br>
# Link de acesso ao sistema da empresa: https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema
# 
# Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado

# In[96]:


#!pip install pyautogui


# In[97]:


import pyautogui
import time

pyautogui.PAUSE = 0.5

#PASSO 1: ENTRAR NO SISTEMA DA EMPRESA

pyautogui.hotkey ("ctrl", "t")

#___________________________________________________
pyautogui.write ("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema") 

#___________________________________________________
pyautogui.press("enter")
#___________________________________________________

#PASSO 2: FAZER LOGIN

#___________________________________________________
pyautogui.click(x=875, y=375)

#___________________________________________________
pyautogui.write("meulogin")

#___________________________________________________
pyautogui.click(x=921, y=452)

#___________________________________________________
pyautogui.write("minhasenha")

#___________________________________________________
pyautogui.click(x=939, y=523)

time.sleep(1.5)


#PASSO 3: EXPORTAR BASE DE DADOS
pyautogui.click(x=407, y=389)
time.sleep(2)

pyautogui.click(x=1717, y=181)

pyautogui.click(x=1477, y=589)

time.sleep(3)








# In[98]:


import time
#time.sleep(3)
#print(pyautogui.position())


# In[99]:


#PASSO 4: CALCULAR OS INDICADORES
import pandas

tabela = pandas.read_csv(r"C:\Users\pedro\OneDrive\Documentos\Estudos\Intensivo de Python/Compras.csv" , sep=";")
display(tabela)

#
total_gasto = tabela["ValorFinal"].sum()
# 
quantidade = tabela["Quantidade"].sum() 
#
preco_medio = total_gasto/quantidade

print(total_gasto)
print(quantidade)
print(preco_medio)


# In[100]:


#PASSO 5: ENVIAR UM EMAIL PARA MEU CHEFE
import pyautogui
import pyperclip
#
pyautogui.PAUSE = 0.5
#

pyautogui.hotkey("ctrl", "t")
#
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
#
pyautogui.press("enter")
time.sleep(2)
#

#CLICAR EM "ESCREVER NOVO EMAIL"
pyautogui.click(x=60, y=195)
#
pyautogui.write("pedroalloureiro@gmail.com")
#
pyautogui.press("tab") #escolher destinatário
#
pyautogui.press("tab") #passar para campo assunto
#
pyperclip.copy("--Relatório de Vendas--") #Caracteres especiais n existem no pyautogui
pyautogui.hotkey("ctrl", "v")
#


pyautogui.press("tab") #passar para o corpo do email
#

#Colocar texto em variável

texto = f"""
Prezado chefe,
Segue o relatório de compras abaixo:
------------------------------------------------------
TOTAL GASTO:R${total_gasto:,.2f}
------------------------------------------------------
QUANTIDADE DE PRODUTOS:R${quantidade:,.2f}
------------------------------------------------------
PREÇO MÉDIO:R${preco_medio:,.2f}
------------------------------------------------------

Qualquer dúvida, basta me contatar.
Att., Pedro Alves Loureiro
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")



#Enviar
pyautogui.hotkey("ctrl", "enter")


# In[ ]:




