# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

#calcula el factorial de un número
def factorial(x):
    if x==0:
        return 1
    return x*factorial(x-1)

#Prueba
for i in range(10):
    print (i, factorial(i))
    
#Calcula el coeficiente binomial, n=número de lanzamientos, k= el número de éxitos
def coef(n,k):
    if n>=k: 
        return factorial(n)/(factorial(k)*factorial(n-k))
    else:
        print (malo)
    
#Prueba    
print (coef(33,18))
    
    
#Función que calcula la probabilidad de distribución binomial para un x dado.
    # n=n° de votos, lanzamientos o personas  k= n° de éxitos p=probabilidad de éxito
def Probbin(n,k,p):
    return coef(n,k)*p**(k)*(1-p)**(n-k)
    
    
#Prueba
print (Probbin(33,18,0.5))
#simula una muestra con distribución binomial de f elementos con probabilidad p y 
#

#-------------------------------------------------------
#P(X=18/r=0.5) ejer 2 parte b
#probabilidad que salga 18 quedarse en 1000 juegos
print (sum(np.random.binomial(33, 0.5, 1000) == 18)/1000)

#-------------------------------------------------------------
#ejer2c
#integral de la probabilidad total con r variando de 0 a 1
#1.-creo una lista de 2001 números.Delta intervalo
r=[]

for i in range(2001):
    r.append(i/2000)
    
print (r[0],r[2000])

#integral de probabilidad total (cont)
#import sympy
#x = sympy.Symbol('x')
#cont=sympy.integrate(Probbin(33,18,x),(x,0,1))
#print(cont)


#Probabilidad total
suma=[]
for i in range(2001):
    suma.append(Probbin(33,18,r[i]))
cont=sum(suma)
#PDF puntos
pdf=[]
for i in range(2001):
    pdf.append(Probbin(33,18,r[i])/cont)

#Gráfica PDF
plt.plot(r,pdf)
plt.show()


#Gráfica de la CDF
cdf=[]
for i in range(2001):
    if i==0:
        cdf.append(pdf[i])
    else:
        cdf.append(pdf[i]+cdf[i-1])
        
plt.plot(r,cdf)
plt.show()

#Verificar que integra 1 en el rango[0,1] 
sum(pdf)  

#maximo de la pdf
max(pdf)
for i in range(2000):
    if pdf[i]==max(pdf):
        r[i]

#-------------------------------------------------------------------------
#2d

#R>0.5
pdfmayor=[]
for i in range(1001):
    pdfmayor.append(Probbin(33,18,r[i])/cont)
p=[]

for i in range(1001):
    p.append(i/2000)
#Gráfica PDF menor a 0.5
plt.plot(p,pdfmayor)
plt.show()

#R<0.5
pdfmenor=[]
for i in range(1000,2001):
    pdfmenor.append(Probbin(33,18,r[i])/cont)

m=[]

for i in range(1000,2001):
    m.append(i/2000)
#Gráfica PDF mayor a 0.5
plt.plot(m,pdfmenor)
plt.show()



 



    


