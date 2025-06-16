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

| Núcleos      | Tempo (ms) | Speedup | Eficiência |
|--------------|------------|---------|------------|
| Serial (1)   | 6409.3     | 1.00    | 100%       |
| 2 núcleos    | 1832.0     | 3.50    | 175%       |
| 4 núcleos    | 1094.44    | 5.86    | 146%       |
| 8 núcleos    | 868.7      | 7.38    | 92%        |
