import os
import re

path = os.getcwd()
path = os.chdir(path+'/arquivos/')

list_archives = os.listdir()
# print("lista arquivos:",list_archives)


def obter_extensao_arquivo(nome_arquivo):
   #pega extensão do arquivo
     extensao =  nome_arquivo.split('.')[-1]
     return extensao
def obter_nome_arquivo(nome_arquivo):
     #retorna o nome do arquivo e substitui espaço por " _ "
     nome = nome_arquivo.split('.')[0]
     nome = re.sub(" ","_",nome)
     return nome
#input texto para ser incrementado
text_add = input('Qual texto concatenar?')    
# renomeia cada arquivo com o texto e substituindo espaço por underline
for nome_arquivo in list_archives :
    nome = obter_nome_arquivo(nome_arquivo)
    extensao = obter_extensao_arquivo(nome_arquivo)
    novo_nome = nome + text_add +"."+ extensao 
    os.rename(nome_arquivo,novo_nome)
