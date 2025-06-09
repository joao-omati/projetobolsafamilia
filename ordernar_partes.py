import pandas as pd
from collections import Counter
import time
import os

# === CONFIGURAÇÕES ===
caminho_csv = r"C:\projeto\projetobolsafamilia\BolsaFamilia_Consolidado_2021.csv"
colunas = ['NOME FAVORECIDO', 'CPF FAVORECIDO']
arquivo_temp = 'nome_cpf_temp.txt'
arquivo_saida = 'duplicados_nome_cpf.txt'

# === INÍCIO DO TIMER ===
inicio = time.time()

try:
    print("🔄 Extraindo dados em partes...")

    # === ETAPA 1: Extrair nome + CPF e salvar em arquivo temporário ===
    with open(arquivo_temp, 'w', encoding='utf-8') as f_temp:
        chunk_size = 100_000
        for chunk in pd.read_csv(caminho_csv, encoding='latin1', sep=';', usecols=colunas, chunksize=chunk_size):
            chunk = chunk.dropna()
            for _, row in chunk.iterrows():
                nome = str(row['NOME FAVORECIDO']).strip().upper()
                cpf = str(row['CPF FAVORECIDO']).strip()
                f_temp.write(f"{cpf};{nome}\n")

    print("✅ Etapa 1 concluída: dados salvos em arquivo temporário.")

    # === ETAPA 2: Contar combinações CPF + Nome duplicadas ===
    print("🔍 Contando duplicatas com barra de progresso...")

    contador = Counter()

    # Conta total de linhas para cálculo da barra de progresso
    with open(arquivo_temp, 'r', encoding='utf-8') as f_temp:
        total_linhas = sum(1 for _ in f_temp)

    progresso_atual = 0
    proximo_marco = 10

    with open(arquivo_temp, 'r', encoding='utf-8') as f_temp:
        for i, linha in enumerate(f_temp, 1):
            chave = linha.strip()
            if chave:
                contador[chave] += 1

            progresso = (i / total_linhas) * 100
            if progresso >= proximo_marco:
                print(f"⏳ Progresso: {int(progresso)}%")
                proximo_marco += 10

    # Filtra apenas os que se repetem mais de uma vez
    duplicados = {chave: count for chave, count in contador.items() if count > 1}
    duplicados_ordenados = sorted(duplicados.items())

    # Salva resultado no arquivo de saída
    with open(arquivo_saida, 'w', encoding='utf-8') as f_out:
        for chave, count in duplicados_ordenados:
            cpf, nome = chave.split(';')
            f_out.write(f"{cpf} - {nome} - {count}\n")

    print(f"✅ {len(duplicados)} registros duplicados salvos em '{arquivo_saida}'.")

except FileNotFoundError:
    print("❌ Arquivo CSV não encontrado. Verifique o caminho:", caminho_csv)
except ValueError as e:
    print(f"❌ Erro ao ler colunas: {e}")
except Exception as e:
    print("❌ Erro geral:", e)

finally:
    fim = time.time()
    duracao = fim - inicio
    print(f"⏱️ Tempo total de execução: {duracao:.2f} segundos")
    print("🏁 Processamento finalizado.")
