from dbfread import DBF
import os
import pandas
from pathlib import Path #pacote para lidar com caminhos de arquivos e diretórios de forma mais eficiente e legível


base_dir =os.path.join(os.getcwd(),"DadosFTPSUS")
dbf_files = [f for f in os.listdir(base_dir) if f.endswith(".dbf")]  # Lista todos os arquivos .dbf no diretório de dadosFTPSUS
#print(dbf_files[0])
file_path = os.path.join(base_dir, dbf_files[0])  # Caminho completo do primeiro arquivo .dbf encontrado

print(f"Imprimindo o primeiro registro de cada arquivo:\n")
for table in dbf_files:
    file_path = os.path.join(base_dir, table)
    table = DBF(str(file_path), encoding='latin1')
    file_name = Path(file_path).stem # Obtém o nome do arquivo sem a extensão e diretórios
    for i, record in enumerate(table):
        if i>0:
            break
        print (f"Arquivo: {file_name} - Registro {i+1}: {record}\n")  
        

