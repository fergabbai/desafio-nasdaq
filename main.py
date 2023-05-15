import csv
import sqlite3
import os

conn = sqlite3.connect('teste_dois.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Nasdaq (
                    Date date,
                    Low float,
                    Open float,
                    Volume float,
                    High float,
                    Close float,
                    Adjusted_close float
                )''')

pasta = 'C:\\Users\\Pessoal\\Documents\\Nasdaq\\csv'
arquivos_csv = [arquivo for arquivo in os.listdir(pasta) if arquivo.endswith('.csv')]

for arquivo in arquivos_csv:
    with open(os.path.join(pasta, arquivo), newline='') as csvfile:
        leitor_csv = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(leitor_csv)

        for linha in leitor_csv:
            if len(linha) >= 7:
                coluna1 = linha[0]
                coluna2 = linha[1]
                coluna3 = linha[2]
                coluna4 = linha[3]
                coluna5 = linha[4]
                coluna6 = linha[5]
                coluna7 = linha[6]
            else:
                coluna1 = None
                coluna2 = None
                coluna3 = None
                coluna4 = None
                coluna5 = None
                coluna6 = None
                coluna7 = None


            cursor.execute('''INSERT INTO Nasdaq (Date, Low, Open, Volume, High, Close, Adjusted_close) 
                            VALUES (?, ?, ?, ?, ?, ?, ?)''', (coluna1, coluna2, coluna3, coluna4, coluna5, coluna6, coluna7))

conn.commit()
conn.close()
