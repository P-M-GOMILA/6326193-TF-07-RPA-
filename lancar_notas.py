import pyautogui
import time
import pandas as pd

# Lê os dados da planilha CSV
dados = pd.read_csv("notas.csv", sep=";")

for index, aluno in dados.iterrows():
    nome = aluno['Nome']
    ra = aluno['RA']
    nota1 = aluno['Nota01']
    tf1 = aluno['TF01']
    nota2 = aluno['Nota02']
    tf2 = aluno['TF02']

    print(f"Lançando notas de {nome} (RA {ra})...")

    # Campo Nome
    pyautogui.click(772, 297)   # coordenada do campo Nome
    time.sleep(0.5)
    pyautogui.typewrite(str(nome))
     

    # Campo RA
    pyautogui.click(772, 390)   # coordenada do campo RA
    time.sleep(0.5)
    pyautogui.typewrite(str(ra))
    

    # Campo Nota 1
    pyautogui.click(772, 490)   # coordenada do campo Nota 1
    time.sleep(0.5)
    pyautogui.typewrite(str(nota1))
       
    
    # Campo TF 1
    pyautogui.click(772, 595)   # coordenada do campo TF 1
    time.sleep(0.5)
    pyautogui.typewrite(str(tf1))
    

    # Campo Nota 2
    pyautogui.click(771, 700)   # coordenada do campo Nota 2
    time.sleep(0.5)
    pyautogui.typewrite(str(nota2))
    

    # Campo TF 2
    pyautogui.click(772, 800)   # coordenada do campo TF 2
    time.sleep(0.5)
    pyautogui.typewrite(str(tf2))

    # Botão Enviar
    pyautogui.click(772, 849)   # coordenada do botão Enviar
    time.sleep(5)               # espera o envio acontecer
     
    # Botão "Enviar outra resposta"
    pyautogui.click(803, 190)   # coordenada do botão Enviar outra resposta
    time.sleep(5)               # espera carregar o novo formulário
     
