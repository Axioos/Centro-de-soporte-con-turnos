import numpy as np

#DATOS:

#Tasa de llegada (lambda)
TASA_LLEGADA = 10 

#Tasas de servicio por turno (mu)
TASAS_MU = {
    0: 15.0,  # Turno Mañana
    1: 12.0,  # Turno Tarde
    2: 10.5   # Turno Noche
}

#Nombres para mostrar en gráficos
NOMBRES_TURNOS = {0: "Mañana", 1: "Tarde", 2: "Noche"}

# Matriz de Transición
MATRIZ_PROB = np.array([
    [0.8, 0.2, 0.0],
    [0.0, 0.7, 0.3],
    [0.4, 0.0, 0.6]
])

#--- CONFIGURACIÓN---
HORAS_TOTALES = 24
MINUTOS_POR_PASO = 1