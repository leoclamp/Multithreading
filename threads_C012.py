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
   "http://example.com/file3"
]

# Array para armazenar os tempos de cada execução
tempos_threads = []

# Função para executar os downloads com um número variável de threads
def download_with_threads(num_threads):
    print(f"\nExecutando com {num_threads} threads...\n")
    start_time = time.time()

    # Criação do ThreadPoolExecutor com o número de threads especificado
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(download_url, urls)
    
    end_time = time.time()
    tempo_execucao = end_time - start_time
    tempos_threads.append((num_threads, tempo_execucao))
    print(f"Todos os downloads foram finalizados em {tempo_execucao:.2f} segundos com {num_threads} threads.\n")

# Testar com diferentes números de threads
for num_threads in [1, 2, 3, 4, 5]:
    download_with_threads(num_threads)

# Exibir os tempos de execução
print("Tempos de execução por número de threads:")
for num_threads, tempo in tempos_threads:
    print(f"{num_threads} threads: {tempo:.2f} segundos")
