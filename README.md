## FAzer um site em flask que remova background

Requerimentos

*flask

*Pillow librar

*rembg modulo usado para remover background de imagens


##Interessante trabalhar com venv


 python -m venv removeback


ativar depende do sistema operacional, no windows pesquise

No linux tem que ter instalado o venv, caso esteja usando, acesse
o diretorio do projeto.

 cd removeback
 
 source bin\active


# Instalar o requerimentos

pip install flask

pip install Pillow

pip install rembg

# inicializar projeto

python3 exemplo.py

## Configuracao voce mudar como é acessado o projeto, ou seja

Mudar o ip, no padrao acima no localhost na porta :5000.
Voce pode alterar modificando a ultima linha do projeto
e colocanco o ip desejado.

Batar alterar esta linha, no exemplo ip


![EXEMPLO](exemplo.png)

 app.run(host='192.168.x.xxx')  

