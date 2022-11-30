import math

#%%Funcion del Bo

def Bo(colums,P,Pb,Rs,Rsb,Yg,Yo,T,API):
    """"
    Parameters
    ---------------
    colums:
        Correlación usada
    P:
        Presion del sistema
    Pb:
        Presion de burbuja
    Rs:
        Solubilidad del gas en PCN/BN
    Rsb:
        Solubilidad del gas en el punto de burbuja PCN/BN
    Yg:
        Gravedad específica del gas en solución
    Yo:
        Gravedad específica del crudo en superficie
    T:
        Temperatura del sistema en °R
    API:
        Gravedad API
    Returns
        float number  -> Bo
    """
    a=0.7423
    b=0.3232
    c=-1.202
    F = (Rs**a) * (Yg**b) * (Yo**c)
    Frsb = (Rsb**a) * (Yg**b) * (Yo**c)
    A = (4.1646E-7)*(Rsb**(0.69357))*(Yg**(0.1885))*(API**(0.3272))*((T-460)**(0.6729))
    if P < Pb:
        if colums == "Standing":
            Bo = 0.9759 + 0.00012 * (Rs*((Yg/Yo)**0.5) + 1.25*(T-460))**(1.2)
        else:
            Bo = 0.497069 + 0.862963 * (10**(-3)) * T + 0.182594 * 10**(-2) * F + 0.318099 * 10**(-5) * F**(2)
    else:
        if colums == "Standing":
            Bob = 0.9759 + 0.00012 * (Rsb*((Yg/Yo)**0.5) + 1.25*(T-460))**(1.2)
            Bo = Bob*(math.exp(((-A)*((P**(0.4094))-(Pb**(0.4094))))))
        else:
            Bob = 0.497069 + 0.862963 * (10**(-3)) * T + 0.182594 * 10**(-2) * Frsb + 0.318099 * 10**(-5) * Frsb**(2)
            Bo = Bob*(math.exp(((-A)*((P**(0.4094))-(Pb**(0.4094))))))
    return Bo

#%% Funcion Rs

def Rs(colums, P, Pb, API, T=None, Yg=None, Yo=None):
    """"
    Parameters
    ---------------
    colums:
        Correlación usada
    P:
        Presión del sistema en psi

    Pb:
        Presión del punto de burbuja

    API:
        Gravedad API
    T:
        Temperatura del sistema en °R
    Yg:
        Gravedad específica del gas en superficie
    Yo:
        Gravedad específica del crudo en superficie

    Returns
        float number  -> Rs
    """
    x = 0.0125 * API - 0.00091 * (T - 460)
    a = 185.843208
    b = 1.877840
    c = -3.1437
    d = -1.32657
    e = 1.398441
    if P < Pb:
        if colums == "Standing":
            Rs = float((Yg) * (((P / 18.2) + 1.4) * (10 ** x)) ** 1.2048)

        elif colums == "Al-Marhoun":
            Rs = float((a * (Yg ** b) * (Yo ** c) * (T ** d) * P) ** e)

        else:
            Rs = string("Seleccione una correlación de la lista")

    else:
        if colums == "Standing":
            Rsb = float((Yg) * (((Pb / 18.2) + 1.4) * (10 ** x)) ** 1.2048)
            Rs = Rsb
        elif colums == "Al-Marhoun":
            Rsb = float((a * (Yg ** b) * (Yo ** c) * (T ** d) * Pb) ** e)
            Rs = Rsb
        else:
            Rs = string("Seleccione una correlación de la lista")
            Rsb = 0
    return Rs

#%%Funcion de la Uo

def Uo(colums, P, Pb, API, T, Rs, Rsb):
    """

    Parameters
    ----------
    colums
        Correlación usada
    P
        Presion del sistema
    Pb
        Presion de saturación
    API
        Gravedas API
    T
        Temperatura en °R
    Rs
        Solubilidad del gas
    Rsb
        Solubilidad del gas a presión de saturación

    Returns
        Uo en cp
    -------

    """

    a = (10**(0.43+(8.33/API)))
    a1 = (10.313 * math.log10(T-460)) - 36.447
    a2 = (Rs * (((2.2E-7) * Rs) - (7.4E-4)))
    c = (8.62E-5) * Rs
    d = (1.1E-3) * Rs
    e = (3.741E-3) * Rs
    b = (0.68 / (10 * c)) + (0.25 / (10 * d)) + (0.062 / (10 ** e))


    a2_ = (Rsb * (((2.2E-7) * Rsb) - (7.4E-4)))
    c_ = (8.62E-5) * Rsb
    d_ = (1.1E-3) * Rsb
    e_ = (3.741E-3) * Rsb
    b_ = (0.68 / (10 * c)) + (0.25 / (10 * d)) + (0.062 / (10 ** e))
    a3_ = ((-3.9E-5)*P)-5
    m = (2.6*(P**(1.187)))*(10**a3_)


    if P < Pb:
        if colums == "Beal":
            Uod = (0.32+(1.8E7/(API**4.53)))*((360/(T-260))**a)
            Uob = ((10)**a2)*(Uod**b)
            Uo = Uob

        else:
            Uod = 3.141 * (10*10) * (T-460)(-3.414) * (math.log10(API))*a1
            Uob = ((10) ** a2_) * (Uod**b)
            Uo = Uob
    else:
        if colums == "Beal":
            Uod = (0.32+(1.8E7/(API**(4.53))))*(360/(T-260))**a
            Uob = ((10)**a2)*(Uod**b)
            Uo = Uob*((P/Pb)**m)

        else:
            Uod = 3.141 * (10*10) * (T-460)(-3.414) * (math.log10(API))*a1
            Uob = ((10) ** a2_) * (Uod**b)
            Uo = Uob*((P/Pb)**m)


    return Uo