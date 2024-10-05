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
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# servico = Service(ChromeDriverManager().install())
# navegador = webdriver.Chrome(service=servico)

unopar_cw = requests.get(
    "https://www.colaboraread.com.br/integracaoAlgetec/index?usuarioEmail=EADPR29%40GMAIL.COM&usuarioNome=NATAN+OGLIARI&disciplinaDescricao=&atividadeId=3501230&atividadeDescricao=CW2+-+PROCESSO+DA+CRIATIVIDADE&ofertaDisciplinaId=11474268&codigoMaterial=0&fornecedor=2&urlOrigem=http%3A%2F%2Fcm-kls-content.s3.amazonaws.com%2F201601%2FINTERATIVAS_2_0%2FPROCESSO_DA_CRIATIVIDADE%2FU2%2FS1%2Findex.html&isAluno=true"
)

# print(unopar_cw)

# https://www.hashtagtreinamentos.com/automacao-web-no-python


# navegador = webdriver.Firefox()
navegador = webdriver.Chrome()

# navegador = webdriver.Chrome("chromedriver")
navegador.get("https://www.colaboraread.com.br/login/auth")
username = "user"
password = "xxxx"
# Espera carregar o site
navegador.implicitly_wait(20)
navegador.find_element("id", "username").send_keys(username)
navegador.implicitly_wait(10)
navegador.find_element("id", "password").send_keys(password)
navegador.implicitly_wait(10)
# clica no botão de entrar
al = WebDriverWait(navegador, 30).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/button'))
)
al.click()
# Entra na trilha e carreira
al = WebDriverWait(navegador, 30).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@id="navbar-content-aluno-cursos"]/div/div[1]/div/div[3]/form/div[2]/button',
        )
    )
)
al.click()
input("Clique para seguir")

navegador.quit()
navegador.close()
