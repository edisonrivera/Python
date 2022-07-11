from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
#Conexion con Driver de Edge
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Accediendo a CEC - EPN
driver.maximize_window()
driver.get("https://aps.cec-epn.edu.ec/portal/index.php/ctrlwelcome")

#button2 = driver.find_element(By.ID, "id_GeneratePWD")

#Enviando usuario
user = driver.find_element(By.ID, "identification")
user.send_keys("17527743")
time.sleep(2)

#Enviando pass
password = driver.find_element(By.ID, "password")
password.send_keys("")
time.sleep(2)

#Entrar en la página
button = driver.find_element(By.CLASS_NAME, "btn-default")
button.click()
time.sleep(5)
#Click en el link de recuperar
#link = driver.find_element(By.LINK_TEXT, "Recuperar Contraseña")
#link.click()
#time.sleep(2)

#Enviando el correo para recuperar cuenta
#email = driver.find_element(By.ID, "email")
#email.send_keys("edison.rivera@epn.edu.ec")
#time.sleep(2)

#Clickear en la opcion de "estudiante" para recuperar
#check_studennt = driver.find_element(By.CLASS_NAME, "radioclass")
#check_studennt.click()
#time.sleep(2)

#button2.click()
#time.sleep(2)
#driver.quit()