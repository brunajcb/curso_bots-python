# Iniciando o ambiente para construir um bot com Python

## Instalações
* Instalar a última versão do python
* Instalar o pip
    O _pip_ é o gerenciador de pacotes do python, com ele é possível instalar qualquer biblioteca disponível da Python.
* Instalar o virtualenv
    Através da virtualenv é possível isolar bibliotecas de projetos que estejam com versões do Python diferentes, evitando que cause conclitos e erros no sistema operacional

**[Clique aqui](http://blog.abraseucodigo.com.br/virtualenv-pip-pra-que-servem.html) para mais detalhes sobre os itens acima, bem como o passo a passo para instalação de cada um deles**

## Criando a virtualenv
* No terminal, selecionar o local do seu computador, por ex.: Desktop, onde você deseja criar a _virtualenv_
* Criar a _virtualenv_ através do comando `virtualenv env`. Esse comando criará a virtualenv dentro de uma pasta chamada "env" no local onde você selecionou_
* No terminal, acessar a pasta _env_: `cd env`. E em seguida, acessar a pasta _bin_: `cd bin`
* Uma vez dentro da pasta _bin_, rodar o comando `source activate`, para ativar a _virtualenv_
* Processo finalizado. A partir de agora já é possível iniciar o projeto do bot.
**_OBS.:_** A pasta do projeto do bot não deve ser dentro da pasta da _virtualenv_, crie-a onde você preferir.

## Executando um bot
>No terminal execute: `python <nome-do-arquivo.py>`

## Particularidades que precisam ser observadas
* No parâmaetro `import Keys`, para que funcione corretamente, _Keys_ deve ser escrito com "K" maiúsculo
* Se você vai capturar elementos que são únicos numa página, por ex.: `by_id` ou `by_name` o parâmetro deve ficar no singular `...find_element...`
* Se você vai capturar elementos que pertencenm a grupos numa página, por ex.: `by_class` o parâmetro deve ficar no plural `...find_elements...`
* Para que o Python reconheça a acentuação do Português Brasileiro, é necessário que seja inserido no início do arquivo `#coding: utf-8`

## Trabalhando com planilhas
* É necessário instalar a biblioteca _xlrd_: `pip install xlrd`
* E no arquivo, preciso importa essa biblioteca: `impor xlrd`
* `workbook = xlrd.open_workbook('<titulo-da-planilha>.xlsx')` - abre a planilha que é definida
* `sheet = workbook.sheet_by_index(0)` - acessa a folha que é indicada a primeira (sheet1) 0, a segunda 1...
* `print(sheet.cell_value(0,0))` - printa o valor de uma determinada célula, por isso preciso definir a posição dela na folha, linha e coluna: (0,0)
* `for linha in range(0,10)` - para percorrer um intervalo de linhas, da coluna que já foi definida anteriormente. Para isso é necessário definir a primeira e a última linha do intervalo a ser percorrida, nesse exemplo: `(0,10)` irá percorrer da linha 1 até a 10
* `print(sheet.cell_value(linha,0))` - vai printar a linha definida, na coluna definida: `(linha, coluna)`
