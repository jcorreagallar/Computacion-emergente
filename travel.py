#Travel salesman problem
#Datos de entrada: "n" ciudades (datos cartesianos)
#Ciudades: A(2,4), B(6,2), C(6,6), D(11,6), E(8,8), F(16,13), G(17,5), H(13,10), I(6,11)
#Combinaciones Parte 1) A-I Parte 2) D-H

import random

A = [2,4]
B = [6,2]
C = [6,6]
D = [11,6]
E = [8,8]
F = [16,13]
G = [17,5]
H = [13,10]
I = [6,11]

ciudades = [A,B,C,D,E,F,G,H,I]
pop_size = 100

#Init

def genetica():
    chromosome = list()

    for i in range(len(ciudades)):
        genes = [0]*len(ciudades)
        chromosome.append(genes)


    position = list(range(9))


    aux = 0

    adn = list ()

    for i in chromosome:
        if aux == 0:
            i[0] = 1
            aux = aux + 1
            adn.append(0)
        elif aux > 0 and aux < len(chromosome)-1:
            aux = aux + 1
            check = random.choice(position[1:-1])
            position.pop(position.index(check))
            i[check] = 1
            adn.append(check)
        else:
            i[-1] = 1
            adn.append(len(chromosome)-1)
        #for j in i:
            #print(j, end=" ")
        #print("\n")
    return adn 

def distancia(P0,P1):
    D = ((P1[0]-P0[0])**2+(P1[1]-P0[1])**2)**(1/2)
    return D

def sumDistancia(listaaux):
    suma = 0
    for i in range(len(listaaux)):
        if i < len(listaaux)-1:
            suma = suma + distancia(listaaux[i],listaaux[i+1])
    return suma

def fitness(x):
    for i in population:
        listaaux = []
        for j in i:
            listaaux.append(clave.get(j))
        sumDistancia(listaaux)

clave = dict(zip(range(len(ciudades)),ciudades))
population = [genetica() for i in range(pop_size)]


# Select

population = sorted(population, key=fitness)
best = population[0]
best_fit = fitness(best)





        

