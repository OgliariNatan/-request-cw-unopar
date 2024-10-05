#####	NOME:				request-cw-unopar.py
#####	VERSÃO:				0.1
#####	DESCRIÇÃO:			Realiza progressões nos conteudos web
#####	DATA DA CRIAÇÃO:	10/11/2023
#####	ESCRITO POR:		Natan Ogliari
#####	E-MAIL:				natanogliari@gmail.com
#####	DISTRO:				Ubuntu GNU/Linux 22.04
#####	LICENÇA:			MIT license
#####	PROJETO:			https://github.com/OgliariNatan/-request-cw-unopar

import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# servico = Service(ChromeDriverManager().install())
# navegador = webdriver.Chrome(service=servico)
unopar_cw = webdriver.Chrome()
url = "https://www.colaboraread.com.br/integracaoAlgetec/index?usuarioEmail=EADPR29%40GMAIL.COM&usuarioNome=NATAN+OGLIARI&disciplinaDescricao=&atividadeId=3684159&atividadeDescricao=CW1+-+TECNOLOGIAS+DE+INFORMA%C3%87%C3%83O+APLICADAS+AO+DIREITO&ofertaDisciplinaId=12293439&codigoMaterial=0&fornecedor=2&urlOrigem=http%3A%2F%2Fcm-kls-content.s3.amazonaws.com%2F201802%2FINTERATIVAS_2_0%2FTECNOLOGIAS_DE_INFORMACAO_APLICADAS_AO_DIREITO%2FU1%2FS1%2Findex.html&isAluno=true"
unopar_cw.get(url)
unopar_cw = requests.get(url)
unopar_cw.implicitly_wait(20)
print(unopar_cw)


# clica no botão de entrar
al = WebDriverWait(unopar_cw, 30).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="navegacao"]/a'))
)
al.click()


unopar_cw.quit()
# unopar_cw.close()
