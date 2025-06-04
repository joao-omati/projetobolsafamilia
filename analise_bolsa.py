import pandas as pd
import os

# Caminho completo fornecido
CAMINHO_CSV = r"C:\Users\jokin\OneDrive\Área de Trabalho\paralelismo\bolsa familia\202102_BolsaFamilia_Pagamentos.csv"

def verificar_arquivo(caminho):
    """Verifica se o arquivo existe e é válido"""
    if not os.path.exists(caminho):
        print(f"❌ Arquivo não encontrado: {caminho}")
        print("\nPossíveis soluções:")
        print("1. Verifique se o caminho está exatamente igual")
        print("2. Confira se o arquivo não foi movido/renomeado")
        print("3. Arquivos disponíveis na pasta:")
        [print(f" - {f}") for f in os.listdir(os.path.dirname(caminho)) if f.endswith('.csv')]
        return False
    
    if os.path.getsize(caminho) == 0:
        print("❌ Arquivo vazio!")
        return False
        
    return True

def processar_dados(caminho):
    try:
        # Mostra os nomes das colunas reais no arquivo
        temp = pd.read_csv(caminho, sep=';', encoding='utf-8', nrows=0)
        print("\n🧾 Colunas disponíveis no CSV:")
        for col in temp.columns:
            print(repr(col))  # Usa repr para mostrar espaços invisíveis ou erros de acento

        # Agora você pode copiar o nome correto daqui e substituir abaixo
        colunas = ['NIS FAVORECIDO', 'VALOR PARCELA', 'NOME MUNICÍPIO', 'UF']  # Ajuste se necessário

        # Carrega os dados
        df = pd.read_csv(
            caminho,
            sep=';',
            encoding='utf-8',
            usecols=colunas,
            dtype={'NIS FAVORECIDO': 'str', 'UF': 'category'}
        )
        
        # Pré-processamento
        df['VALOR'] = (
            df['VALOR PARCELA']
            .str.replace(',', '.', regex=False)
            .astype(float)
        )
        
        # Remove duplicatas e valores inválidos
        df = df.drop_duplicates('NIS FAVORECIDO')
        df = df[df['VALOR'] > 0]
        
        # Cálculos
        stats = {
            'arquivo': os.path.basename(caminho),
            'data': 'Fevereiro/2021',
            'total_beneficiarios': len(df),
            'valor_total': df['VALOR'].sum(),
            'media': df['VALOR'].mean(),
            'media_por_uf': df.groupby('UF')['VALOR'].mean().sort_values(ascending=False),
            'top_municipios': df.groupby(['NOME MUNICÍPIO', 'UF'])['VALOR'].mean().nlargest(5)
        }
        
        return stats
        
    except Exception as e:
        print(f"\n❌ Erro no processamento: {str(e)}")
        print("\nDica: Verifique se:")
        print("- O arquivo não está corrompido")
        print("- O delimitador é ';'")
        print("- A codificação é 'utf-8'")
        return None

def mostrar_resultados(resultados):
    """Exibe os resultados formatados"""
    print(f"\n📊 ANÁLISE: {resultados['data']} ({resultados['arquivo']})")
    print("═" * 50)
    print(f"👥 Beneficiários únicos: {resultados['total_beneficiarios']:,}")
    print(f"💰 Valor total distribuído: R$ {resultados['valor_total']:,.2f}")
    print(f"📌 Média por beneficiário: R$ {resultados['media']:,.2f}")
    
    print("\n🏙 Média por Estado:")
    print(resultados['media_por_uf'].to_markdown(floatfmt=".2f"))
    
    print("\n🏆 Top 5 municípios com maior valor médio:")
    print(resultados['top_municipios'].to_markdown(floatfmt=".2f"))

if __name__ == "__main__":
    print("\n🔍 Iniciando análise do Bolsa Família")
    if verificar_arquivo(CAMINHO_CSV):
        resultados = processar_dados(CAMINHO_CSV)
        if resultados:
            mostrar_resultados(resultados)
    
    input("\nPressione Enter para sair...")
