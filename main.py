from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#abrir o navegador

driver = webdriver.Chrome()
driver.maximize_window()

#pesquisar o site

driver.get('https://demoqa.com/text-box')
sleep(2)

# 1 scroollar 400 pixels

driver_rolar400 = driver.execute_script("window.scrollBy(0, 400);")
sleep(2)

# 2 scrolar até o submit

# botao_submit = driver.find_element(By.ID, 'submit')
# driver_scrollar_botão = driver.execute_script("arguments[0].scrollIntoView();", botao_submit)
# sleep(2)

# preencher nome

barra_nome=driver.find_element(By.ID, 'userName')
barra_nome.click()
barra_nome.send_keys('Fulana da silva silvana')

sleep(2)
# preencher email

barra_email=driver.find_element(By.ID, 'userEmail')
barra_email.click()
barra_email.send_keys('fulano123@gmail.com')

sleep(2)
# preencher current adress

barra_currnt_adress=driver.find_element(By.ID, 'currentAddress')
barra_currnt_adress.click()
barra_currnt_adress.send_keys('Pindamonhangaba, Rua Tangamandapio, 2213')

sleep(2)
# preencher permanenet adress

barra_perm_adress=driver.find_element(By.ID, 'permanentAddress')
barra_perm_adress.click()
barra_perm_adress.send_keys('Xique xique, Bahia, Rua Sepetiba, 2213')

sleep(2)

# clicar no botao submit

barra_email=driver.find_element(By.ID, 'submit')
barra_email.click()


sleep(2)

# scrollar até o resultado

scroll_resultado = driver.execute_script("window.scrollBy(0, 300);")

sleep(2)


