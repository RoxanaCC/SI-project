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

s1 = State(recrut, name="recrut")
s2 = State(exbig, name="exbig")
s3 = State(activity, name="activity")

model = BayesianNetwork("Activitate noi recruti")

model.add_states(s1, s2, s3)

model.add_edge(s1, s3)
model.add_edge(s2, s3)

model.bake()

#model.probability(numpy.array(['A1', 'S1', 'Ac'], ndmin = 2))
