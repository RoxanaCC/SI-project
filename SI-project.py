import math
from pomegranate import *
import numpy

#Anul in care studentul se afla
recrut = DiscreteDistribution({'A1': 0.55, 'A2': 0.3, 'Ot': 0.15})

#Experienta big brother-ului
exbig = DiscreteDistribution({'No': 0.55, 'S1': 0.45})

#Daca recrutul activeaza este dependent de anul in care e si de big-ul pe care il are 
activity = ConditionalProbabilityTable(
        [[ 'A1', 'No', 'Ac', 0.33 ],
         [ 'A1', 'S1', 'Ac', 0.75 ],
         [ 'A2', 'No', 'Ac', 0.1 ],
         [ 'A2', 'S1', 'Ac', 0.25 ],
         [ 'Ot', 'No', 'Ac', 0.05 ],
         [ 'Ot', 'S1', 'Ac', 0.17 ]], [recrut, exbig])

s11 = State(recrut, name="recrut")
s12 = State(exbig, name="exbig")
s13 = State(activity, name="activity")

#Vremea de afara
vreme = DiscreteDistribution({'S': 0.55, 'R': 0.45})

#Dimensiune proiect
dimensiune = DiscreteDistribution({'Sml': 0.7, 'Big': 0.3})

#Locatie proiect
locatie = DiscreteDistribution({'In': 0.5, 'Out': 0.5})

#Epidemie coronavirus
covid = DiscreteDistribution({'False': 0.99, 'True': 0.01})

#Realizarea proiectului
proiect = ConditionalProbabilityTable(
        [[ 'S', 'In' , 'Big', 'False', 'Pr', 0.99 ],
		 [ 'S', 'In' , 'Big', 'True' , 'Pr', 0.001 ],
		 [ 'S', 'In' , 'Sml', 'False', 'Pr', 0.99 ],
		 [ 'S', 'In' , 'Sml', 'True' , 'Pr', 0.005 ],
		 [ 'S', 'Out', 'Big', 'False', 'Pr', 0.99 ],
		 [ 'S', 'Out', 'Big', 'True' , 'Pr', 0.003 ],
		 [ 'S', 'Out', 'Sml', 'False', 'Pr', 0.99 ],
		 [ 'S', 'Out', 'Sml', 'True' , 'Pr', 0.007 ],
		 [ 'R', 'In' , 'Big', 'False', 'Pr', 0.99 ],
		 [ 'R', 'In' , 'Big', 'True' , 'Pr', 0.001 ],
		 [ 'R', 'In' , 'Sml', 'False', 'Pr', 0.99 ],
		 [ 'R', 'In' , 'Sml', 'True' , 'Pr', 0.005 ],
		 [ 'R', 'Out', 'Big', 'False', 'Pr', 0.005 ],
		 [ 'R', 'Out', 'Big', 'True' , 'Pr', 0.003 ],
		 [ 'R', 'Out', 'Sml', 'False', 'Pr', 0.01 ],
		 [ 'R', 'Out', 'Sml', 'True' , 'Pr', 0.007 ],
         ], [recrut, exbig])

s21 = State(vreme, name="vreme")
s22 = State(dimensiune, name="dimensiune")
s23 = State(locatie, name="locatie")
s24 = State(covid, name="covid")
s25 = State(proiect, name="proiect")

activitate = BayesianNetwork("Activitate noi recruti")

activitate.add_states(s11, s12, s13)

activitate.add_edge(s11, s13)
activitate.add_edge(s12, s13)

realizarep = BayesianNetwork("Realizarea proiect")

realizarep.add_states(s21, s22, s23, s24, s25)

realizarep.add_edge(s21, s25)
realizarep.add_edge(s22, s25)
realizarep.add_edge(s23, s25)
realizarep.add_edge(s24, s25)

activitate.bake()
realizarep.bake()
