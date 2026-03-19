import random
import time

def gerar_numeros(arquivo, quantidade, soma_desejada):
    soma = 0
    with open(arquivo, "w") as f:
        for i in range(quantidade - 1):
            numero = random.randint(-1000, 1000)
            soma += numero
            f.write(f"{numero}\n")
        # último número ajustado para garantir soma correta
        ultimo_numero = soma_desejada - soma
        f.write(f"{ultimo_numero}\n")
        soma += ultimo_numero
    return soma

if __name__ == "__main__":
    inicio = time.time()  # marca o início

    nome_arquivo = "numero2.txt"
    qtd = 10_000_000  # 10 milhões de linhas
    soma_desejada = 5384
    soma_total = gerar_numeros(nome_arquivo, qtd, soma_desejada)

    fim = time.time()  # marca o fim
    tempo_execucao = fim - inicio

    print(f"Arquivo gerado: {nome_arquivo}")
    print(f"Número de linhas: {qtd}")
    print(f"Soma total dos valores: {soma_total}")
    print(f"Tempo de execução: {tempo_execucao:.2f} segundos")
