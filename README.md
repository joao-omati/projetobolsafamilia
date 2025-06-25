**Notebook usado: Avell Ion A65i**
# Especificações do Produto
**Placa de Vídeo
GeForce® RTX 4060**  
- Memória: 8GB GDDR6
**Processador
Intel® Core™ i9-13900HX**  
- Cache Intel® Smart Cache: 36 MB  
- Frequência Base: 2.2 GHz  
- Frequência Turbo Max: até 5.4 GHz
## Memória RAM
**32GB DDR5 (5600 MHz)**  
- Configuração: 4x 8GB em Dual Channel
## Armazenamento
**SSD M.2 NVME 1TB**  
- Geração: 4  
- Velocidade de leitura: 5.000 MB/s
**Sistema Operacional
- Windows 11 Home Single Language
- Versão Original

OBS:Tentamos rodar em um notebook com ryzenn 7 e 8gb de ram mas devido ao baixo nivel de memoria ram não foi possivel completar os testes pois a ram mata o processo quando ela lota 

o projeto envolve pegar todos os dados do bolsa familia de janeiro a novembro de 2021 e classificar os mesmos como base em nome,quantidades de vezes que o nome aparece e o valor total recebido pela pessoa
Primeiro se baixa todos os csv pelo site https://portaldatransparencia.gov.br/download-de-dados/bolsa-familia-pagamentos onde foi feito o download dos arquivos de janeiro a novembro em  formato de csv e juntamos ele usando as bibliotecas import pandas, os, tqdm e usando uma função para agrupar os arquivos usando tqdm e ordenando usando pandas e o os para criar um arquivo novo,depois do csv principal com todos os dados estar completo a gente ordenar por nomes e pelo pedaço de cpf que o govervo oferece para evitar que nomes iguais sejam um só,nisso depois de cada nome vai aparecer as vezes que a pessoa recebeu e do lado o valor monetario total

## Pontos importantes do código utlizado
**1. Verificação de arquivo (verificar_arquivo)**
Confere se o caminho existe com os.path.exists.
Mostra sugestões caso o caminho esteja errado.
Mostra arquivos .csv da pasta como ajuda.
Verifica se o arquivo está vazio com os.path.getsize.
👉 Isso é excelente para evitar que o programa trave por arquivo ausente ou incorreto.

**2. Leitura robusta do CSV**
Primeiro lê somente o cabeçalho (nrows=0) para listar as colunas reais.
Usa repr(col) para revelar problemas de acentuação ou espaços invisíveis.
Lê apenas colunas relevantes com usecols.
👉 Esse cuidado evita bugs ao tentar ler colunas com nomes mal formatados ou ausentes.

**3. Pré-processamento inteligente**
Troca vírgula por ponto nos valores (problema comum em arquivos brasileiros).
Converte para float.
Remove duplicatas baseando-se no NIS.
Filtra valores inválidos (≤ 0).
👉 Você garante integridade estatística dos dados.

**4. Estatísticas com pandas**
Calcula totais, médias, médias por estado (UF).
Usa nlargest(5) para o top 5 municípios com maior valor médio.
Utiliza .to_markdown() para exibição tabular elegante no terminal.

## Bibliotecas utilizadas e análise
**Panda**
Biblioteca para análise e manipulação de dados estruturados.
**Pontos Positivos:**
Altíssimo desempenho para leitura e filtragem de dados.
Muito expressivo: poucas linhas para tarefas complexas.
Ótimo suporte a CSV, Excel, banco de dados etc.
Permite uso direto de estatísticas com groupby, mean, sum, etc.

**Pontos Negativos:**
Pode consumir muita memória com arquivos grandes.
Erros difíceis de entender se os dados estiverem mal formatados.
Não é ideal para manipular arquivos linha por linha (muito grandes) — aí o ideal seria csv.reader.

**OS**
Biblioteca padrão do Python para manipulação do sistema operacional.
**Pontos Positivos:**
Permite manipular caminhos, arquivos, diretórios, tamanhos de arquivo, etc.
Funciona multiplataforma (Windows, Linux, macOS).
Simples e leve — ideal para verificação de existência de arquivos, listar diretórios etc.

**Pontos Negativos:**
Não oferece suporte direto para paths avançados (melhor usar pathlib para isso).
Pode ser perigoso se usado para apagar/mover arquivos sem cuidado.

## Tabela de Speedup ou Eficiência Paralela

| Núcleos       | Tempo (ms) | Speedup | Eficiência |
|---------------|------------|---------|------------|
| Serial (1)    | 6409.3     | 1.00    | 100%       |
| 2 núcleos     | 1832.0     | 3.50    | 175%       |
| 3 núcleos     | 1331.81    | 4.81    | 160.3%     |
| 4 núcleos     | 1094.44    | 5.86    | 146%       |
| 8 núcleos     | 868.7      | 7.38    | 92%        |
| 10 núcleos    | 1038.65    | 6.17    | 61.7%      |
