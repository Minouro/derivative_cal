# derivative_cal
Utilizando Python 3.12<br>
<i>Instruções especiais para o Heber</i><br>

## 🐍Criando ambiente virtual
No Prompt de Comando, selecione a pasta em que baixou o arquivo com `cd Insira\Local\Do\Arquivo\Aqui`<br>
`python -m venv .venv`<br>
`.venv\Scripts\activate`<br>
`pip install -r requirements.txt`<br>

## 😎Executando o código 
Sempre inicie o ambiente virtual com `.venv\Scripts\activate` antes de executar `python main.py`<br>

## 🤩Como usar 
1º Digite o número de variáveis<br>
2º Digite o número de valores<br>
3° Digite a icógnita (devem ser as mesmas usadas nas fórmulas!)<br>
4° Digite os valores de cada icógnita<br>
5º Digite a fórmula (em notação python)<br>
Exemplo: `x**3+2*y**2` é igual a escrever x^3 + 2y^2<br><br>

O código retorna as derivadas em função de cada variável, com o resultado substituindo a variável pela média.<br>
No final é gerado uma planilha excel. Use ela para editar os valores e carrega-los na opção `2 - Nova Planilha`.<br>
Caso não exista uma planilha, provavelmente terá um erro 🤫<br>
