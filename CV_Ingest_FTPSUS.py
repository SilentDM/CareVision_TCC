from ftplib import FTP
import os

ftp = FTP("ftp.datasus.gov.br") #FTP de dados publicos
ftp.login()  
ftp.cwd("/dissemin/publicos/SIHSUS/200801_/Dados/")  #Diretorio dos arquivos
#ftp.dir()  # Imprime a lista de arquivos e diretórios no diretório atual
files = ftp.nlst()  # criando uma lista com os nomes dos arquivos no diretório atual
#print(len(files)) #quantos arquivos existem no diretorio

d_files = [down_file for down_file in files if down_file.startswith("SPSP25")]  # criando uma lista dos arquivos para baixar
base_dir = os.getcwd()  # Diretório atual do script
file_path = os.path.join(base_dir, "DadosFTPSUS")  # Caminho local para salvar os arquivos baixados

if not os.path.exists(file_path):  # Verifica se o diretório local existe
    os.makedirs(file_path)  # Cria o diretório local se não existir

for file_name in d_files:
    file_path_name = os.path.join(file_path, file_name)  # Caminho completo do arquivo local + nome do arquivo
    if os.path.exists(file_path_name):  # Verifica se o arquivo local já existe
        print(f"Arquivo {file_name} já existe. Pulando download.")  
        continue
    print(f"Baixando arquivo {file_name}...") 
    with open(file_path_name, "wb") as f:  # Abrindo o arquivo local em modo de escrita binária
        ftp.retrbinary("RETR " + file_name, f.write)  # Baixando o arquivo do servidor FTP e salvando no arquivo local
    print(f"Arquivo {file_name} baixado com sucesso.") 
ftp.quit()  # Encerra a conexão com o servidor FTP