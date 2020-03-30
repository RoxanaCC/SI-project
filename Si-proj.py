import math
from pomegranate import *
import numpy

#Anul in care studentul se afla
recrut = DiscreteDistribution({'A1': 0.81, 'A2': 0.158, 'A3': 0.03,'A4': 0.002})

#Experienta big brother-ului
exbig = DiscreteDistribution({'No': 0.5, 'S1': 0.28, 'S2': 0.22})

#Sememstrul din anul Universitar
sem = DiscreteDistribution({'S1': 0.5, 'S2': 0.5})

#Recrutul aplica din nou
retry = ConditionalProbabilityTable(
        [[ 'S1', 'T', 0.001 ],
         [ 'S1', 'F', 0.999 ],
		 [ 'S2', 'T', 0.4 ],
         [ 'S2', 'F', 0.6 ]], [sem])

#Daca recrutul activeaza este dependent de anul in care e si de big-ul pe care il are 
activity = ConditionalProbabilityTable(
        [[ 'A1', 'T', 'No', 'T', 0.45 ],
		 [ 'A1', 'T', 'S1', 'T', 0.86 ],
		 [ 'A1', 'T', 'S2', 'T', 0.88 ],
		 [ 'A1', 'F', 'No', 'T', 0.33 ],
		 [ 'A1', 'F', 'S1', 'T', 0.75 ],
		 [ 'A1', 'F', 'S2', 'T', 0.77 ],
		 [ 'A2', 'T', 'No', 'T', 0.15 ],
		 [ 'A2', 'T', 'S1', 'T', 0.31 ],
		 [ 'A2', 'T', 'S2', 'T', 0.33 ],
		 [ 'A2', 'F', 'No', 'T', 0.1 ],
		 [ 'A2', 'F', 'S1', 'T', 0.25 ],
		 [ 'A2', 'F', 'S2', 'T', 0.26 ],
		 [ 'A3', 'T', 'No', 'T', 0.1 ],
		 [ 'A3', 'T', 'S1', 'T', 0.3 ],
		 [ 'A3', 'T', 'S2', 'T', 0.31 ],
		 [ 'A3', 'F', 'No', 'T', 0.05 ],
		 [ 'A3', 'F', 'S1', 'T', 0.17 ],
		 [ 'A3', 'F', 'S2', 'T', 0.18 ],
		 [ 'A4', 'T', 'No', 'T', 0.01 ],
		 [ 'A4', 'T', 'S1', 'T', 0.015 ],
		 [ 'A4', 'T', 'S2', 'T', 0.018 ],
		 [ 'A4', 'F', 'No', 'T', 0.001 ],
		 [ 'A4', 'F', 'S1', 'T', 0.007 ],
		 [ 'A4', 'F', 'S2', 'T', 0.007 ],
		 [ 'A1', 'T', 'No', 'F', 0.55 ],
		 [ 'A1', 'T', 'S1', 'F', 0.14 ],
		 [ 'A1', 'T', 'S2', 'F', 0.12 ],
		 [ 'A1', 'F', 'No', 'F', 0.67 ],
		 [ 'A1', 'F', 'S1', 'F', 0.25 ],
		 [ 'A1', 'F', 'S2', 'F', 0.23 ],
		 [ 'A2', 'T', 'No', 'F', 0.85 ],
		 [ 'A2', 'T', 'S1', 'F', 0.69 ],
		 [ 'A2', 'T', 'S2', 'F', 0.67 ],
		 [ 'A2', 'F', 'No', 'F', 0.9 ],
		 [ 'A2', 'F', 'S1', 'F', 0.75 ],
		 [ 'A2', 'F', 'S2', 'F', 0.74 ],
		 [ 'A3', 'T', 'No', 'F', 0.9 ],
		 [ 'A3', 'T', 'S1', 'F', 0.7 ],
		 [ 'A3', 'T', 'S2', 'F', 0.69 ],
		 [ 'A3', 'F', 'No', 'F', 0.95 ],
		 [ 'A3', 'F', 'S1', 'F', 0.83 ],
		 [ 'A3', 'F', 'S2', 'F', 0.82 ],
		 [ 'A4', 'T', 'No', 'F', 0.99 ],
		 [ 'A4', 'T', 'S1', 'F', 0.985 ],
		 [ 'A4', 'T', 'S2', 'F', 0.982 ],
		 [ 'A4', 'F', 'No', 'F', 0.999 ],
		 [ 'A4', 'F', 'S1', 'F', 0.993 ],
		 [ 'A4', 'F', 'S2', 'F', 0.993 ]], [recrut, retry, exbig])

#Vremea de afara
vreme = DiscreteDistribution({'S': 0.55, 'R': 0.45})

#Dimensiune proiect
dimensiune = DiscreteDistribution({'Sml': 0.7, 'Big': 0.3})

#Locatie proiect
locatie = DiscreteDistribution({'In': 0.5, 'Out': 0.5})

#Epidemie coronavirus
covid = ConditionalProbabilityTable(
        [[ 'S', 'T', 0.001 ],
         [ 'S', 'F', 0.999 ],
		 [ 'R', 'T', 0.005 ],
         [ 'R', 'F', 0.995 ]], [vreme])

#Realizarea proiectului
proiect = ConditionalProbabilityTable(
        [[ 'S', 'In' , 'Big', 'T', 'T', 0.001 ],
		 [ 'S', 'In' , 'Big', 'F', 'T', 0.99 ],
		 [ 'S', 'In' , 'Sml', 'T', 'T', 0.005 ],
		 [ 'S', 'In' , 'Sml', 'F', 'T', 0.99 ],
		 [ 'S', 'Out', 'Big', 'T', 'T', 0.003 ],
		 [ 'S', 'Out', 'Big', 'F', 'T', 0.99 ],
		 [ 'S', 'Out', 'Sml', 'T', 'T', 0.005 ],
		 [ 'S', 'Out', 'Sml', 'F', 'T', 0.99 ],
		 [ 'R', 'In' , 'Big', 'T', 'T', 0.001 ],
		 [ 'R', 'In' , 'Big', 'F', 'T', 0.99 ],
		 [ 'R', 'In' , 'Sml', 'T', 'T', 0.005 ],
		 [ 'R', 'In' , 'Sml', 'F', 'T', 0.99 ],
		 [ 'R', 'Out', 'Big', 'T', 'T', 0.001 ],
		 [ 'R', 'Out', 'Big', 'F', 'T', 0.005 ],
		 [ 'R', 'Out', 'Sml', 'T', 'T', 0.002 ],
		 [ 'R', 'Out', 'Sml', 'F', 'T', 0.01 ],
		 [ 'S', 'In' , 'Big', 'T', 'F', 0.999 ],
		 [ 'S', 'In' , 'Big', 'F', 'F', 0.01 ],
		 [ 'S', 'In' , 'Sml', 'T', 'F', 0.995 ],
		 [ 'S', 'In' , 'Sml', 'F', 'F', 0.01 ],
		 [ 'S', 'Out', 'Big', 'T', 'F', 0.997 ],
		 [ 'S', 'Out', 'Big', 'F', 'F', 0.01 ],
		 [ 'S', 'Out', 'Sml', 'T', 'F', 0.995 ],
		 [ 'S', 'Out', 'Sml', 'F', 'F', 0.01 ],
		 [ 'R', 'In' , 'Big', 'T', 'F', 0.999 ],
		 [ 'R', 'In' , 'Big', 'F', 'F', 0.01 ],
		 [ 'R', 'In' , 'Sml', 'T', 'F', 0.995 ],
		 [ 'R', 'In' , 'Sml', 'F', 'F', 0.01 ],
		 [ 'R', 'Out', 'Big', 'T', 'F', 0.999 ],
		 [ 'R', 'Out', 'Big', 'F', 'F', 0.005 ],
		 [ 'R', 'Out', 'Sml', 'T', 'F', 0.998 ],
		 [ 'R', 'Out', 'Sml', 'F', 'F', 0.99 ]], [vreme, locatie, dimensiune, covid])

#Statut voluntari
statut = ConditionalProbabilityTable(
        [[ 'T', 'T', 'MA', 0.15 ],
         [ 'T', 'F', 'MA', 0.01 ],
		 [ 'F', 'T', 'MA', 0.28 ],
         [ 'F', 'F', 'MA', 0.02 ],
		 [ 'T', 'T', 'M' , 0.32 ],
         [ 'T', 'F', 'M' , 0.01 ],
		 [ 'F', 'T', 'M' , 0.56 ],
         [ 'F', 'F', 'M' , 0.03 ],
		 [ 'T', 'T', 'V' , 0.52 ],
         [ 'T', 'F', 'V' , 0.01 ],
		 [ 'F', 'T', 'V' , 0.15 ],
         [ 'F', 'F', 'V' , 0.01 ],
		 [ 'T', 'T', 'VI', 0.01 ],
         [ 'T', 'F', 'VI', 0.97 ],
		 [ 'F', 'T', 'VI', 0.01 ],
         [ 'F', 'F', 'VI', 0.85 ]], [proiect, activity])

s11 = State(recrut, name="recrut")
s12 = State(exbig, name="exbig")
s13 = State(sem, name="sem")
s14 = State(retry, name="retry")
s15 = State(activity, name="activity")

s21 = State(vreme, name="vreme")
s22 = State(dimensiune, name="dimensiune")
s23 = State(locatie, name="locatie")
s24 = State(covid, name="covid")
s25 = State(proiect, name="proiect")

s3 = State(statut, name="statut")

activitate = BayesianNetwork("Activitate membri organizatie")
activitate.add_states(s11, s12, s13, s14, s15)

activitate.add_edge(s13, s14)
activitate.add_edge(s11, s15)
activitate.add_edge(s12, s15)
activitate.add_edge(s14, s15)

project = BayesianNetwork("Proiecte organizatie")
project.add_states(s21, s22, s23, s24, s25)

project.add_edge(s21, s24)
project.add_edge(s21, s25)
project.add_edge(s22, s25)
project.add_edge(s23, s25)
project.add_edge(s24, s25)

status = BayesianNetwork("Statut membri organizatie")
status.add_states(s11, s12, s13, s14, s15, s21, s22, s23, s24, s25, s3)

status.add_edge(s13, s14)
status.add_edge(s11, s15)
status.add_edge(s12, s15)
status.add_edge(s14, s15)

status.add_edge(s21, s24)
status.add_edge(s21, s25)
status.add_edge(s22, s25)
status.add_edge(s23, s25)
status.add_edge(s24, s25)

status.add_edge(s15, s3)
status.add_edge(s25, s3)

activitate.bake()
project.bake()
status.bake()

print(activitate.probability(numpy.array(['A1','No', 
	'S1', 'F', 'T'], ndmin = 2 )))
print(project.probability(numpy.array(['S', 'Big',
	'In', 'F', 'T'], ndmin = 2 )))
print(status.probability(numpy.array(['A1','No', 
	'S1', 'F', 'T', 'S', 'Big', 'In', 'F', 'T', 
	'MA'], ndmin = 2 )))