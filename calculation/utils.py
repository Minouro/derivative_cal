import pandas as pd
import matplotlib.pyplot as plt
from sympy import *
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
        label = input(f"\nDigite nome da {x+1}º icógnita: ")
        for y in range(n):
            measures.append(float(input(f"({label}) Digite o {y+1}° valor: ").replace(",",".")))
        variables[label] = measures
        print(f"{label} definido com sucesso!")
    return variables

def newData():
    v = int(input("Digite o n° de icógnitas: "))
    n = int(input("Digite o n° de valores: "))
    variables = values(n, v)
    createData(variables)
    derivative(variables)

def createData(variables):
    df = pd.DataFrame(data = variables)
    df.to_excel("planilha.xlsx", index=False)
    print(f"\n{df}\n")

def loadData():
    df = pd.read_excel("planilha.xlsx")
    print(f"\n{df}\n")
    derivative(df)

def loadGraph(x, y, x_label, y_label):
    plt.plot(x, y)
    plt.title(f"{y_label} VERSUS {x_label}")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def derivative(variables):
    s = []
    der = []
    res = []

    f = sympify(input("Digite a função: "))

    for x in variables:
        print(f"\nMédia ({x}): {fmean(variables[x])}")
        print(f"Desvio Padrão ({x}): {stdev(variables[x])}")
        s.append(Variable(x, fmean(variables[x])))

    for var in s:
        der.append(diff(f, var.name))
    
    for d in der:
        print(f"\nDerivada: {d}")
        for var in s:
            d = d.subs(var.name, var.value)
        res.append(d)
        print(f"Resultado: {d}")

    return der
class Variable:
    def __init__(self, name, value):
        self.name = symbols(name)
        self.value = value
    