import pyautogui
from time import sleep

# 1 - cadastrar nome, senha e acessar o app
pyautogui.click( 1070,1057, duration=2)
pyautogui.click(1260, 593, duration=2)
pyautogui.write("Bruno")
pyautogui.click(1280,566, duration=2)
pyautogui.write("123")
pyautogui.click(1260, 593, duration=2)

# 2- digitar cadastro e acessar
pyautogui.click(1285, 540, duration=2)
pyautogui.write("Bruno")
pyautogui.click(1280,566, duration=2)
pyautogui.write("123")
pyautogui.click(1190,599, duration=2)

# 3- extrair cada produto
with open("produtos.txt", "r") as arquivo:
    for linha in arquivo:
        produto = linha.split(",")[0]
        quantidade = linha.split(",")[1]
        preco = linha.split(",")[2]

# 4 - clicar e digitar produto
pyautogui.click(1033, 528, duration=2)
pyautogui.write(produto)
pyautogui.click(1024, 551, duration=2)
pyautogui.write(quantidade)
pyautogui.click(1032, 584, duration=2)
pyautogui.write(preco)