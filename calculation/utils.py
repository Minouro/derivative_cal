import pandas as pd
import matplotlib.pyplot as plt
from statistics import fmean, stdev

def menu(message, options):
    m = 0
    while(m not in options):
        m = input(message)
    return int(m)

def values(n, v):
    variables = {}
    for x in range(v):
        measures = []
        label = input(f"\nDigite nome da {x+1}º variável: ")
        for y in range(n):
            measures.append(float(input(f"({label.upper()}) Digite o {y+1}° valor: ").replace(",",".")))
        variables[label.upper()] = measures
        print(f"{label.upper()} definido com sucesso!")
    return variables

def newData():
    n = int(input("Digite o n° de valores: "))
    v = int(input("Digite o n° de varíaveis: "))
    variables = values(n, v)
    
    df = pd.DataFrame(data = variables)
    for x in variables:
        df[f"MÉDIA ({x})"] = fmean(variables[x])
        df[f"DESVIO PADRÃO ({x})"] = stdev(variables[x])
    df.to_excel("planilha.xlsx", index=False)
    print(f"\n{df}\n")

def loadGraph(x, y, x_label, y_label):
    plt.plot(x, y)
    plt.title(f"{y_label} VERSUS {x_label}")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def loadData():
    df = pd.read_excel("planilha.xlsx")
    label_1 = df.columns[0]
    label_2 = df.columns[1]
    df[f"MÉDIA ({label_2})"] = fmean(df[label_2])
    df[f"DESVIO PADRÃO ({label_2})"] = stdev(df[label_2])
    df.to_excel("planilha.xlsx", index=False)
    print(f"\n{df}\n")
    loadGraph(df[label_1], df[label_2], label_1, label_2)

class Variable:
    def __init__(self, name, values):
        self.name = name
        self.values = values
    