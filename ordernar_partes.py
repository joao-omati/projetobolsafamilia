import pandas as pd
from collections import Counter, defaultdict
import time
import os
from multiprocessing import Pool, cpu_count
import re

# === CONFIGURAÇÕES ===
caminho_csv = r"C:\Users\jokin\OneDrive\Área de Trabalho\paralelismo\projetobolsafamilia\BolsaFamilia_Consolidado_2021.csv"
colunas = ['NOME FAVORECIDO', 'CPF FAVORECIDO', 'VALOR PARCELA']
arquivo_temp = 'nome_cpf_temp.txt'
arquivo_saida = 'duplicados_nome_cpf.txt'
num_processos = ()  # Usa todos os núcleos disponíveis

# === FUNÇÃO PARA PROCESSAR UM CHUNK EM PARALELO ===
def processar_chunk(chunk):
    chunk_local = chunk.dropna()
    dados_chunk = []
    valor_por_chave_local = defaultdict(float)
    
    for _, row in chunk_local.iterrows():
        nome = str(row['NOME FAVORECIDO']).strip().upper()
        cpf = str(row['CPF FAVORECIDO']).strip()
        valor = str(row['VALOR PARCELA']).replace('R$', '').replace('.', '').replace(',', '.').strip()
        
        try:
            valor = float(valor)
        except ValueError:
            valor = 0.0
        
        chave = f"{cpf};{nome}"
        dados_chunk.append(chave)
        valor_por_chave_local[chave] += valor
    
    return dados_chunk, valor_por_chave_local

# === FUNÇÃO PRINCIPAL ===
if __name__ == '__main__':
    inicio = time.time()

    try:
        print(f"🔄 Iniciando processamento paralelo com {num_processos} núcleos...")

        # ETAPA 1: Processar o CSV em chunks paralelamente
        chunks = pd.read_csv(caminho_csv, encoding='latin1', sep=';', usecols=colunas, chunksize=100_000)
        
        # Pool de processos para paralelização
        with Pool(num_processos) as pool:
            resultados = pool.map(processar_chunk, chunks)
        
        # Consolidar resultados dos processos
        todas_chaves = []
        valor_por_chave = defaultdict(float)
        
        for chaves_chunk, valores_chunk in resultados:
            todas_chaves.extend(chaves_chunk)
            for chave, valor in valores_chunk.items():
                valor_por_chave[chave] += valor
        
        print("✅ Dados consolidados. Contando duplicatas...")

        # ETAPA 2: Contar duplicatas (ainda em paralelo, se necessário)
        contador = Counter(todas_chaves)
        duplicados = {chave: count for chave, count in contador.items() if count > 1}
        duplicados_ordenados = sorted(duplicados.items())

        # Salvar resultados
        with open(arquivo_saida, 'w', encoding='utf-8') as f_out:
            for chave, count in duplicados_ordenados:
                cpf, nome = chave.split(';')
                total_valor = valor_por_chave.get(chave, 0.0)
                f_out.write(f"{cpf} - {nome} - {count} vezes - R$ {total_valor:,.2f}\n")

        print(f"✅ {len(duplicados)} registros duplicados salvos em '{arquivo_saida}'.")

    except Exception as e:
        print(f"❌ Erro: {e}")

    finally:
        fim = time.time()
        duracao = fim - inicio
        print(f"⏱️ Tempo total (paralelizado): {duracao:.2f} segundos")
