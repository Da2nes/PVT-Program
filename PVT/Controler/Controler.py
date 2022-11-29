#%% Import Libraries
import blackd

import xlwings as xw
import numpy as np
import pandas as pd
import blackd as bd
import matplotlib.pyplot as plt
from PVT.Model.Functions import Rs
from PVT.Model.Functions import Bo
from PVT.Model.Functions import Uo

#%% Program code
#Etiquetas
SUMMARY = "Summary"
RESULTS = "Results"
Rs_ = "Rs"
Rsb_ = "Rsb"
Bo_ = "Bo"
Pb_ = "Pb"
Uo_ = "Uo"
Num_datos = 20
PRESION_R = "Presion_r (psi)"
PRESION_TEST = "Presion_test (psi)"
PRESION_SAT = "Pb (psi)"
TEMPERATURA = "Temperatura (R)"
API = "°API"
G_GAS = "ϒgas"
G_OIL = "ϒoil"
