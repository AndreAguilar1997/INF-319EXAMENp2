# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 21:44:56 2021

@author: JHOSELIN
"""

from pyswip import Prolog
prolog=Prolog()
prolog.assetz("padre(Juan,Maria)")
prolog.assetz("padre(Pablo,Juan)")
prolog.assetz("padre(Pablo,Marcela)")
prolog.assetz("padre(Carlos,Debora)")
list(prolog.query("padre(juan,x)"))==[{'x':'maria'}]

for elemento in prolog.query("padre(X,Y)"):
    print(elemento["X"],"es el padre de", elemento["Y"])
list(prolog.query("padre(Pablo,x)"))==[{'x':'Juan'},{'x':'Marcela'}]
for elemento in prolog.query("padre(X,Y)"):
    print(elemento["X"],"es el padre de", elemento["Y"])
list(prolog.query("padre(Carlos,x)"))==[{'x':'debora'}]
for elemento in prolog.query("padre(X,Y)"):
    print(elemento["X"],"es el padre de", elemento["Y"])

prolog.assertz("hermano(juan,Marcela)")  
list(prolog.query("hermano(juan,x)"))==[{'x':'Marcela}]
for elemento in prolog.query("hermano(X,Y)"):
    print(elemento["X"],"es el hermano de", elemento["Y"]) 
prolog.assertz("abuelo(Pablo,Maria)")  
list(prolog.query("abuelo(Pablo,x)"))==[{'x':'Maria}]
for elemento in prolog.query("abuelo(X,Y)"):
    print(elemento["X"],"es el abuelo de", elemento["Y"]) 