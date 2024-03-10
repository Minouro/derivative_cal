import calculation.utils as utils

m = utils.menu("\n1 - Inserir valores\n2 - Carregar planilha\nEscolha: ", ["1", "2"])

if (int(m) == 1):
    utils.newData()
else:
    utils.loadData()