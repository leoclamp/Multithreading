import concurrent.futures
import requests
import time
 
# Função que baixa o conteúdo de uma URL
def download_url(url):
   print(f"Baixando {url}...")
   response = requests.get(url)
   print(f"Download de {url} finalizado com {len(response.content)} bytes.")
   return response.content
 
# Lista de URLs para download
urls = [
    "http://example.com/file1",
    "http://example.com/file2",
    "http://example.com/file3",
    "http://example.com/file4",
    "http://example.com/file5",
    "http://example.com/file6"
]
 
# Função para executar os downloads com um número variável de threads
def download_with_threads(num_threads):
   print(f"\nExecutando com {num_threads} threads...\n")
   start_time = time.time()
 
   # Criação do ThreadPoolExecutor com o número de threads especificado
   with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
       executor.map(download_url, urls)
   end_time = time.time()
   print(f"Todos os downloads foram finalizados em {end_time - start_time:.2f} segundos com {num_threads} threads.\n")
 
 
# Testar com diferentes números de threads
for num_threads in [1, 2, 3, 4, 5,]:
   download_with_threads(num_threads)