# Simulador de Downloads com Multithreading

Este projeto demonstra o uso de multithreading para realizar downloads simultâneos de arquivos e comparar o desempenho com diferentes números de threads.

## Descrição

O script realiza o download de arquivos de uma lista de URLs e mede o tempo necessário para completar todos os downloads com diferentes quantidades de threads. O objetivo é mostrar como a utilização de múltiplas threads pode impactar o tempo total de execução para operações de download.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `requests`
  - `concurrent.futures` (incluída na biblioteca padrão do Python)
  
Para instalar a biblioteca `requests`, você pode usar o seguinte comando:

```
pip install requests
```