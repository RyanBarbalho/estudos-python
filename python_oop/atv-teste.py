# Criar um programa onde terá classes onde cada uma que fará leitura de um arquivo específico (json, csv, xml).
# O programa deve identificar automaticamente a extensão do arquivo
# , ler utilizando a classe correspondente e imprimir o conteúdo do arquivo na tela.

import csv
import json
import os
import xml.etree.ElementTree as ET


class Leitor:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def ler(self):
        pass


class LerJson(Leitor):
    def ler(self):
        with open(self.arquivo) as f:
            data = json.load(f)
            print(data)


class LerCsv(Leitor):
    def ler(self):
        with open(self.arquivo) as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)


class LerXml(Leitor):
    def ler(self):
        arvore = ET.parse(self.arquivo)
        raiz = arvore.getroot()
        for child in raiz:
            print(child.tag, child.attrib)
            for subchild in child:
                print(subchild.tag, subchild.attrib)


def main():
    try:
        arquivo = input("digite o nome do arquivo: ")
        trecho = os.path.splitext(arquivo)[1]

        if trecho == ".json":
            leitor = LerJson(arquivo)
            leitor.ler()
        elif trecho == ".csv":
            leitor = LerCsv(arquivo)
            leitor.ler()
        elif trecho == ".xml":
            leitor = LerXml(arquivo)
            leitor.ler()
        else:
            print("Arquivo não suportado")
            exit(1)
    except Exception as e:
        print("Erro: ", e)


if __name__ == "__main__":
    main()
