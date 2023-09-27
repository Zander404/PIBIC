import utils
import re
from unidecode import unidecode


arquivo = open("word_bag.txt", 'r',encoding="utf-8")
words = []
tipo = "txt" 




for linha in arquivo:
    words.append(re.sub('\n', '', unidecode(linha.lower())))


# tipo = str(input("Qual o tipo de arquivo  ()")).lower()    

if tipo == "pdf":
    documento, number_pages = utils.readPDF("Teste.pdf")

    for key in words:
        for page in range(number_pages):
            
            if re.search(key, documento[page]):
                print(f"A Palavra: {key} está no documento \n na pagina {page}")

if tipo == "txt":
    for word in words:
        utils.readTXT("registro.txt", word)
  
if tipo == "json":
    for word in words:
        utils.readJSON("json.json", word)