import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from math import sqrt
from statistics import fmean, stdev

def menu(message, options):
    m = 0
    while(m not in options):
        m = input(message)
    return m

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
    v = int(input("\nDigite o n° de icógnitas: "))
    n = int(input("Digite o n° de valores: "))
    variables = values(n, v)
    createData(variables)

def createData(variables):
    df = pd.DataFrame(data = variables)
    df.to_excel("planilha.xlsx", index=False)
    print(f"\n{df}\n")

def loadData():
    df = pd.read_excel("planilha.xlsx")
    print(f"\n{df}")
    return df

def loadGraph(variables):
    x, y = plotAxis(variables)
    plt.plot(variables[x], variables[y])
    plt.plot(variables[x], variables[y], "bo")
    plt.title(f"{y.upper()} VERSUS {x.upper()}")
    plt.xlabel(x.upper())
    plt.ylabel(y.upper())
    plt.grid()
    plt.show()

def derivative(variables):
    s = []
    der = []
    res = []

    f = sympify(input("\nDigite a função: "))

    for x in variables:
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

def Info(variables):
    for x in variables:
        print(f"\nMédia ({x}): {fmean(variables[x])}")
        print(f"Desvio Padrão ({x}): {stdev(variables[x])}")

def errorCal(variables):
    errors = {}
    result = {}
    
    for x in variables:
        errors[x]= float(input(f"Digite o erro ({x}): ").replace(",","."))

    print("")

    for x in errors:
        result[x] = sqrt(stdev(variables[x])**2+errors[x]**2)
        print(f"\n√({stdev(variables[x])}^2 + {errors[x]}^2)\nErro ({x}) = {result[x]}")

def minMethod(variables):
    x, y = plotAxis(variables)
    
    arrayX = np.array(variables[x])
    arrayY = np.array(variables[y])

    mean_x = fmean(arrayX)
    mean_y = fmean(arrayY)
    sxx = fmean(np.power(arrayX, 2))
    sxy = fmean(np.multiply(arrayX, arrayY))

    a0 = (sxx*mean_y - mean_x*sxy)/(sxx - mean_x**2)
    a1 = (sxy - mean_x*mean_y)/(sxx - mean_x**2)

    print(f"\na0 = {a0}")
    print(f"a1 = {a1}")

    points = []
    for v in variables[x]:
        points.append(a1+a0*v)
    plt.plot(variables[x], points)
    plt.plot(variables[x] , variables[y], "bo")
    plt.show()

def plotAxis(variables):
    options = []
    print("\nEscolha os eixos do gráfico.\nDigite a icógnita correspondende",end=" / ")
    for v in variables:
        options.append(v)
        print(v, end=" / ")

    x = menu("\nEixo X: ", options)
    y = menu("Eixo Y: ", options)

    return x, y

class Variable:
    def __init__(self, name, value):
        self.name = symbols(name)
        self.value = value
    