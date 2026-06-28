from dbfread import DBF
import os
import pandas

base_dir =os.path.join(os.getcwd(),"DadosFTPSUS")
dbf_files = [f for f in os.listdir(base_dir) if f.endswith(".dbf")]  # Lista todos os arquivos .dbf no diretório de dadosFTPSUS
#print(dbf_files[0])
file_path = os.path.join(base_dir, dbf_files[0])  # Caminho completo do primeiro arquivo .dbf encontrado
table = DBF(str(file_path), encoding='latin1')  # Lê o primeiro arquivo .dbf encontrado com codificação 'latin1'


for i, record in enumerate(table):
    if i>2:
        break
    print(f"Registro {i+1}: {record}\n")  # Imprime 3 registros do arquivo .dbf
