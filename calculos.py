import numpy as np
from configuracion import TASAS_MU, NOMBRES_TURNOS

def obtener_pi(matriz):
    #Dimensión de la matriz
    n = matriz.shape[0]
    
    #Preparar sistema de ecuaciones (I - P)^T = 0
    A = (matriz.T - np.eye(n))
    
    #Restricción de normalización (suma de probs = 1)
    A[-1] = np.ones(n)
    
    #Vector objetivo
    B = np.zeros(n)
    B[-1] = 1
    
    #Resolver sistema lineal
    pi = np.linalg.solve(A, B)
    return pi

def calculos_cola_teoricos(tasa_llegada, tasa_mu):
    #Cálculo del factor de utilización (rho)
    factor_uso = tasa_llegada / tasa_mu
    
    #Verificar saturación
    if factor_uso >= 1:
        return None
        
    #Número medio clientes (L)
    L = factor_uso / (1 - factor_uso)
    
    #Tiempo medio sistema (W)
    W = 1 / (tasa_mu - tasa_llegada)
    
    return {
        "factor_uso": factor_uso,
        "L": L,
        "W": W
    }

def generar_reporte(tasa_llegada, pi_vector):
    reporte = []
    
    for i, prob in enumerate(pi_vector):
        mu_actual = TASAS_MU[i]
        resultados = calculos_cola_teoricos(tasa_llegada, mu_actual)
        
        fila = {
            "Turno": NOMBRES_TURNOS[i],
            "Prob_Estacionaria": prob,
            "Mu": mu_actual
        }
        if resultados:
            fila.update(resultados)
            
        reporte.append(fila)
        
    return reporte