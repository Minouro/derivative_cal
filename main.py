import calculation.utils as utils

m = 0
while(int(m) != 8):
    m = utils.menu("\n1 - Inserir valores\n2 - Erro Padrão\n3 - Derivada Parcial\n4 - Método dos Mínimos Padrões\n5 - Média e Desvio Padrão\n6 - Gráfico\n7 - Carregar planilha\n8 - Sair\n\nEscolha: ", ["1", "2","3","4","5","6","7","8"])

    if (int(m) == 1):
        utils.newData()

    elif(int(m) == 2):
        utils.errorCal(utils.loadData())

    elif(int(m) == 3):
        utils.derivative(utils.loadData())

    elif(int(m) == 4):
        utils.minMethod(utils.loadData())

    elif(int(m) == 5):
        utils.Info(utils.loadData())
    
    elif(int(m) == 6):
        utils.loadGraph(utils.loadData())

    elif(int(m)) == 7:
        utils.loadData()