o projeto envolve pegar todos os dados do bolsa familia de janeiro a novembro de 2021 e classificar os mesmos como base em nome,quantidades de vezes que o nome aparece e o valor total recebido pela pessoa
Primeiro se baixa todos os csv pelo site https://portaldatransparencia.gov.br/download-de-dados/bolsa-familia-pagamentos onde foi feito o download dos arquivos de janeiro a novembro em  formato de csv e juntamos ele usando as bibliotecas import pandas, os, tqdm e usando uma função para agrupar os arquivos usando tqdm e ordenando usando pandas e o os para criar um arquivo novo,depois do csv principal com todos os dados estar completo a gente ordenar por nomes e pelo pedaço de cpf que o govervo oferece para evitar que nomes iguais sejam um só,nisso depois de cada nome vai aparecer as vezes que a pessoa recebeu e do lado o valor monetario total

Serial (1 núcleo)	6409.3	1.00 (base)	100%
2 núcleos	1832.0	6409.3 / 1832 ≈ 3.50	3.50 / 2 ≈ 175%
4 núcleos	1094.44	6409.3 / 1094.44 ≈ 5.86	5.86 / 4 ≈ 146%
8 núcleos	868.7	6409.3 / 868.7 ≈ 7.38	7.38 / 8 ≈ 92%
