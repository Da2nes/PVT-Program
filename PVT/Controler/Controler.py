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

def main():
    wb = xw.Book.caller()
    sheet_summary = wb.sheets[SUMMARY]
    RAND_PRESIONS = np.array(sorted((list(range(150,3150,150))),reverse=True))
    sheet_summary["B6"].options(transpose = True).value = RAND_PRESIONS
    df_data = sheet_summary["B5"].options(pd.DataFrame, expand = "table", index = False).value
    df_correlations = sheet_summary["I3"].options(pd.DataFrame, expand="table", index=False).value
    df_results = sheet_summary["H5"].options(pd.DataFrame, expand="table", index=False).value
    corr_Rs = df_correlations.iloc[0,0]
    corr_Bo = df_correlations.iloc[0,1]
    corr_Uo = df_correlations.iloc[0,2]

    #%%Rs

    Rs_corr = []
    for i in range(Num_datos):
        Rs_corr.append(corr_Rs)
    Params_Rs = pd.DataFrame({"Correlacion": Rs_corr,"Presion": RAND_PRESIONS,"Presion_Burb": df_data[PRESION_SAT], "API": df_data[API], "Temperatura": df_data[TEMPERATURA], "G_gas": df_data[G_GAS], "G_oil": df_data[G_OIL]})
    v_Rs = []
    for i in range(Num_datos):
        Rs_resul = Rs(*(Params_Rs.iloc[i,0],Params_Rs.iloc[i,1],Params_Rs.iloc[i,2],Params_Rs.iloc[i,3],Params_Rs.iloc[i,4],Params_Rs.iloc[i,5],Params_Rs.iloc[i,6]))
        v_Rs.append(Rs_resul)

    sheet_summary["I6"].options(transpose = True).value = v_Rs #Agregando el vector Rs result al data frame resultado

    Rs_saturacion = df_results.iloc[0,1]
    v_Rsb = []
    for i in range(Num_datos):
        v_Rsb.append(Rs_saturacion)
    sheet_summary["L6"].options(transpose=True).value = v_Rsb

    # Rs
    plt.plot(df_data[PRESION_TEST], df_results[Rs_])
    plt.xlabel("Presion")
    plt.ylabel("Solubilidad")
    plt.title("Rs vs P")
    plt.show()

    # Bo
    Bo_corr = []
    for i in range(Num_datos):
        Bo_corr.append(corr_Bo)

    Params_Bo = pd.DataFrame({"Correlacion": Bo_corr,"Presion": RAND_PRESIONS,"Presion_burb":df_data[PRESION_SAT],"Rs":df_results[Rs_],"Rsb":df_results[Rsb_],"G_gas":df_data[G_GAS],"G_oil":df_data[G_OIL],"Temperatura":df_data[TEMPERATURA],"API":df_data[API]})
    v_Bo = []
    for i in range(Num_datos):
        Bo_resul = Bo(*(
            Params_Bo.iloc[i, 0], Params_Bo.iloc[i, 1], Params_Bo.iloc[i, 2], Params_Bo.iloc[i, 3],
            Params_Bo.iloc[i, 4],
            Params_Bo.iloc[i, 5], Params_Bo.iloc[i, 6], Params_Bo.iloc[0, 7], Params_Bo.iloc[0, 8]))
        v_Bo.append(Bo_resul)
    sheet_summary["J6"].options(transpose=True).value = v_Bo

    # Bo
    plt.plot(df_data[PRESION_TEST], df_results[Bo_])
    plt.xlabel("Presion")
    plt.ylabel("Factor Volumétrico")
    plt.title("Bo vs P")
    plt.show()