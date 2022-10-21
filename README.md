# Como rodar

O código pode ser executado duas formas:

## Local

Para rodar o código localmente, siga o passo a passo:
1. Ter python 3 instalado. 
2. Instalar pip
``` 
python -m pip install --upgrade pip
```
3. Instalar ortools
```
python -m pip install --upgrade --user ortools
```
4. Clonar o repositório na máquina local
5. Entrar na pasta do repositório local
6. Rodar o código
```
python3 questão1.py
python3 questão2.py
```

## Github Actions

Para evitar o trabalho de rodar localmente, é possível rodar o código através do Github Actions. Para isso:
1. Clique na aba 'Actions' no github
2. Clique em 'Roda trabalho' na lista de Actions do lado esquerdo
3. Clique em 'Run workflows' no lado direito e confirme
4. Clique no novo action que apareceu com nome 'Roda trabalho'
5. Clique em build
6. Espere o terminar o funcionamento, depois clique nos passos 'Run Questão 1' e 'Run Questão 2' para ver o resultado que foi gerado.
