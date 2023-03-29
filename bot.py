from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import random
import os


class InstagramBot:
    TEMPO_PUBLICAR = 3
    QTD_COMENTARIOS_DIA = 390

    def __init__(self, username: str, password: str, link_sorteio: str, list_time: list, qtd_users: int,
                 contador_global: int, list_users: list, test: bool):

        chrome_otions = webdriver.ChromeOptions()
        
        self.username = username
        self.password = password
        self.link_sorteio = 'https://www.instagram.com/p/{}/'.format(link_sorteio)
        self.list_time = list_time
        self.qtd_users = qtd_users
        self.contador_global = contador_global
        self.list_users = list_users
        self.test = test
        self.driver = webdriver.Chrome(
            executable_path=os.path.dirname(os.path.realpath(__file__)) + "/chromedriver.exe", chrome_options=chrome_otions)

    def login(self):
        driver = self.driver
        driver.get('https://instagram.com')
        time.sleep(1)
        field_user = driver.find_element_by_xpath("//input[@name='username']")
        field_pass = driver.find_element_by_xpath("//input[@name='password']")
        field_user.click()
        field_user.clear()
        self.digitando(self.username, field_user)
        field_pass.click()
        field_pass.clear()
        self.digitando(self.password, field_pass)
        field_pass.send_keys(Keys.RETURN)
        time.sleep(5)

        driver.get(self.link_sorteio)
        
        while self.contador_global < (self.QTD_COMENTARIOS_DIA + self.contador_global):
            self.comentar(self.link_sorteio)

    @staticmethod
    def digitando(frase, field_digitar):
        for letra in frase:
            field_digitar.send_keys(letra)
            time.sleep(random.randint(1, 10) / 30)

    def comentar(self, link_sorteio):
        driver = self.driver

        time.sleep(2)
        comentario = '{} {}'.format(self.comentario_users(self.list_users, self.qtd_users), self.contador_global)

        while True:
            try:
                driver.find_elements_by_class_name('Ypffh')[0].click()
                break
            except:
                print('Bloqueado')
                driver.get(link_sorteio)
                time.sleep(60)

        field = driver.find_elements_by_class_name('Ypffh')[0]
        field.clear()

        if self.test:
            self.digitando('teste {}'.format(self.contador_global), field)
        else:
            self.digitando(comentario, field)

        time.sleep(self.TEMPO_PUBLICAR)
        field.send_keys(Keys.RETURN)

        print('========================')
        print(' Número de comentarios: {}'.format(self.contador_global))
        print('========================')

        self.contador_global += 1

        time.sleep(random.choice(self.list_time))

    def comentario_users(self, list_users: list, quantidade: int) -> str:
        users = random.sample(list_users, quantidade)
        return ' '.join(users)
