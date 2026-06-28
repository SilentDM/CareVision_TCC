import importlib, sys, subprocess
import os
def ensure_package(import_name, pip_name=None): # certifica que os pacotes necessários estão instalados, caso contrário instala-os
    pip_name = pip_name or import_name
    try:
        importlib.import_module(import_name)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
ensure_package("dbfread", "dbfread")
ensure_package("datasus_dbc", "datasus-dbc")

#pip install datasus_dbc
import datasus_dbc #biblioteca do SUS para transformar os arquivos dbc em dbf e outros
#pip install dbfread
from dbfread import DBF #biblioteca do SUS para ler arquivos dbf


base_dir = os.getcwd()+'\\DadosFTPSUS'
dbc_files = [f for f in os.listdir(base_dir) if f.endswith(".dbc")]  # Lista todos os arquivos .dbc no diretório de dadosFTPSUS
#print (f"Arquivos DBC encontrados: {len(dbc_files)}")  # Imprime a quantidade de arquivos .dbc encontrados

for dbc_file in dbc_files:
    try:
        output_file = os.path.join(base_dir, dbc_file.replace(".dbc", ".dbf")) # Caminho do arquivo .dbf convertido
        datasus_dbc.decompress(os.path.join(base_dir, dbc_file), output_file)  # Converte o arquivo .dbc para .dbf
        print(f"Arquivo {dbc_file} convertido com sucesso para .dbf")  # Imprime mensagem de sucesso
    except Exception as e:
        print(f"Erro ao converter o arquivo {dbc_file}: {e}")  # Imprime mensagem de erro