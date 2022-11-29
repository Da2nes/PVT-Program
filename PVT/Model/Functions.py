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
