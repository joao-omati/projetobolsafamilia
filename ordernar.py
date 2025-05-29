import pandas as pd

# Define o caminho do arquivo CSV 
caminho_csv = r"C:\Users\jokin\OneDrive\Área de Trabalho\paralelismo\bolsa familia\BolsaFamilia_Consolidado_2021.csv"

# Lê o arquivo CSV (assumindo que a coluna de nomes se chama 'NOME FAVORECIDO' - comum no Bolsa Família)
try:
    df = pd.read_csv(caminho_csv, encoding='latin1', sep=';')  # Encoding comum em dados do governo
    if 'NOME FAVORECIDO' in df.columns:
        nomes = df['NOME FAVORECIDO'].dropna().unique()  # Remove duplicatas e valores vazios
        nomes_ordenados = sorted(nomes, key=lambda x: x.upper())  # Ordem alfabética (case-insensitive)
        
        # Salva em um arquivo .txt
        with open('nomes_ordenados_bolsa_familia.txt', 'w', encoding='utf-8') as f:
            for nome in nomes_ordenados:
                f.write(f"{nome}\n")
        
        print(f"✅ Lista de nomes salva em 'nomes_ordenados_bolsa_familia.txt'!")
    else:
        print("❌ Coluna 'NOME FAVORECIDO' não encontrada. Verifique o CSV.")
except FileNotFoundError:
    print("❌ Arquivo não encontrado. Verifique o caminho:", caminho_csv)
except Exception as e:
    print("❌ Erro:", e)
