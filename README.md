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

## Pontos importantes do código utilizado

### 1. Verificação de arquivo (`verificar_arquivo`)
- Confere se o caminho existe com `os.path.exists`.
- Mostra sugestões caso o caminho esteja errado.
- Lista os arquivos `.csv` da pasta para ajudar na identificação.
- Verifica se o arquivo está vazio com `os.path.getsize`.

Observação: Isso evita que o programa trave por causa de arquivos ausentes ou inválidos.

---

### 2. Leitura robusta do CSV
- Lê somente o cabeçalho (`nrows=0`) para listar os nomes reais das colunas.
- Usa `repr(col)` para revelar espaços ou acentos ocultos.
- Lê apenas colunas relevantes com `usecols`.

Observação: Evita erros causados por colunas mal formatadas ou nomes incorretos.

---

### 3. Pré-processamento inteligente
- Converte valores de `R$` com vírgula para ponto decimal.
- Transforma os valores em `float`.
- Remove duplicatas com base no `NIS FAVORECIDO`.
- Elimina registros com valores inválidos (≤ 0).

Observação: Garante integridade estatística e evita distorções.

---

### 4. Estatísticas com `pandas`
- Calcula total de beneficiários, valor total distribuído e média.
- Usa `groupby` para média por estado (UF).
- Aplica `nlargest(5)` para destacar os 5 municípios com maior valor médio.
- Utiliza `.to_markdown()` para uma exibição tabular limpa no terminal.

---

## Bibliotecas utilizadas e análise

### pandas
Biblioteca para análise e manipulação de dados estruturados.

**Pontos Positivos:**
- Alto desempenho na leitura e filtragem de dados.
- Sintaxe expressiva e poderosa.
- Suporte amplo a CSV, Excel e banco de dados.
- Permite uso direto de estatísticas com `groupby`, `mean`, `sum` etc.

**Pontos Negativos:**
- Pode consumir muita memória com grandes volumes de dados.
- Erros podem ser difíceis de entender com dados mal formatados.
- Não é ideal para leitura linha a linha em arquivos muito grandes (melhor usar `csv.reader`).

---

### os
Biblioteca padrão do Python para manipulação do sistema operacional.

**Pontos Positivos:**
- Manipulação de caminhos, arquivos e diretórios.
- Funciona bem em Windows, Linux e macOS.
- Leve e simples — ideal para verificações básicas.

**Pontos Negativos:**
- Não oferece suporte moderno a caminhos (como o `pathlib`).
- Pode ser perigoso se usado incorretamente para apagar ou mover arquivos.

## Tabela de Speedup ou Eficiência Paralela

| Núcleos       | Tempo (ms) | Speedup | Eficiência |
|---------------|------------|---------|------------|
| Serial (1)    | 6409.3     | 1.00    | 100%       |
| 2 núcleos     | 1832.0     | 3.50    | 175%       |
| 3 núcleos     | 1331.81    | 4.81    | 160.3%     |
| 4 núcleos     | 1094.44    | 5.86    | 146%       |
| 8 núcleos     | 868.7      | 7.38    | 92%        |
| 10 núcleos    | 1038.65    | 6.17    | 61.7%      |
