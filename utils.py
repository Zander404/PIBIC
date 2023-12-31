from PyPDF2 import PdfReader
import re, json, unicodedata


def readPDF(file):
    """
    READ PDF: função para ler arquivos pdf e converter para texto(string)

    PARAMS: 
        file: PDF FILE = Arquivo PDF a ser lido.

    RETURN 
        clean_text: string = texto limpo limpo (sem escape keys)
        page_num: int = numero de páginas no arquivo
    """

    clean_text = []
    pdf_reader  = PdfReader(open(file, "rb"))
    for page_num in range(len(pdf_reader.pages)):
        text = pdf_reader.pages[page_num].extract_text()
        clean_text.append(text.strip().replace("\n", '').lower())
      

    return clean_text, len(pdf_reader.pages)


def readTXT(file, pattern):
    """
    READ TXT: função que vai ler o arquivo TXT e procurar se a palavra está presente no arquivo desejado

    PARAMS:
        file: TXT FILE = Arquivo Txt a ser analisado
        pattern: string = Palavra a ser verificada se existe dentro do arquivo

    RETURN:
        NULL
        Printar no console a palavra presente no documento
        
    """

    with open(file, "r", encoding="utf-8") as f:
        for _, line in enumerate(f, start=1):
            line = line.lower()
            if pattern in line:
                print(f"A palavra {pattern} esta no Documento")
                break

        f.close()


def readJSON(file, pattern: str):
    """
    DESCRIPTION:
        READ JSON: função que vai ler o arquivo JSON e procurar se a palavra está presente no arquivo desejado,
          retornando uma mensagem no Console, caso a palavra esteja presente.

    PARAMS:
        file: JSON FILE = Arquivo JSON a ser analisado
        pattern: string = Palavra a ser verificada se existe dentro do arquivo

    RETURN:
        NULL
        Printar no console a palavra presente no documento
    """

    f = open(file, "r", encoding="utf-8")
    data = json.load(f)
    data = str(data['data']).lower()
    if re.search(pattern, data):
        print(f"Tem a palavra {pattern} no documento")

    f.close()
        