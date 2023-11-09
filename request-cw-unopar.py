#####	NOME:				request-cw-unopar.py
#####	VERSÃO:				0.1
#####	DESCRIÇÃO:			Realiza progressões nos conteudos web
#####	DATA DA CRIAÇÃO:	09/11/2023
#####	ESCRITO POR:		Natan Ogliari
#####	E-MAIL:				natanogliari@gmail.com
#####	DISTRO:				Ubuntu GNU/Linux 22.04
#####	LICENÇA:			MIT license
#####	PROJETO:			https://github.com/OgliariNatan/-request-cw-unopar

import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


#servico = Service(ChromeDriverManager().install())
#navegador = webdriver.Chrome(service=servico)

unopar_cw = requests.get('https://www.colaboraread.com.br/integracaoAlgetec/index?usuarioEmail=EADPR29%40GMAIL.COM&usuarioNome=NATAN+OGLIARI&disciplinaDescricao=&atividadeId=3501230&atividadeDescricao=CW2+-+PROCESSO+DA+CRIATIVIDADE&ofertaDisciplinaId=11474268&codigoMaterial=0&fornecedor=2&urlOrigem=http%3A%2F%2Fcm-kls-content.s3.amazonaws.com%2F201601%2FINTERATIVAS_2_0%2FPROCESSO_DA_CRIATIVIDADE%2FU2%2FS1%2Findex.html&isAluno=true')

print(unopar_cw)

#https://www.hashtagtreinamentos.com/automacao-web-no-python


#navegador = webdriver.Firefox()
navegador = webdriver.Chrome()

#navegador = webdriver.Chrome("chromedriver")
navegador.get('https://www.colaboraread.com.br/login/auth')
username = '0hjjjm4960'
password = 'yfjg'
navegador.find_element('id', 'username').send_keys(username)

navegador.find_element('id', 'password').send_keys(password)
time=3000
#navegador.find_element('name', 'Entrar').click()
navegador.find_element_by_xpath('//*[@id="loginForm"]/button')
#Falta o clique no botão entrar css
#navegador.find_element_by_css_selector('btnbtn-primarybtn-lgbtn-blockmb-10')


#navegador.find_element_by_xpath('//*[@id="username"]').click()
#navegador.find_element_by_xpath('//*[@id="playbarBkGrnd"]/canvas[2]').click()

time=3000

navegador.close()