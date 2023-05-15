import os
import csv

pasta = 'C:\\Users\\Pessoal\\Documents\\Nasdaq\\csv'
arquivos_csv = [arquivo for arquivo in os.listdir(pasta) if arquivo.endswith('.csv')]

for arquivo in arquivos_csv:
    with open(os.path.join(pasta, arquivo), newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for linha in reader:
            print(', '.join(linha))