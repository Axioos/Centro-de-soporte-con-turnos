import random
import pandas as pd
import numpy as np
from configuracion import *

def ejecutar_simulacion():
    # Variables de estado iniciales
    num_clientes = 0
    turno_id = 0  # 0: Mañana, 1: Tarde, 2: Noche
    
    registros = []
    pasos_totales = HORAS_TOTALES * 60
    
    # Bucle de tiempo (minuto a minuto)
    for t in range(pasos_totales):
        
        # 1. CAMBIO DE TURNO (MARKOV)
        # Se evalúa cada 60 minutos (inicio de hora)
        if t > 0 and t % 60 == 0:
            fila_probs = MATRIZ_PROB[turno_id]
            turno_id = np.random.choice([0, 1, 2], p=fila_probs)
            
        mu_actual = TASAS_MU[turno_id]
        
        # 2. EVENTO LLEGADA
        # Probabilidad en este intervalo de tiempo
        prob_entrar = TASA_LLEGADA * (MINUTOS_POR_PASO / 60)
        
        if random.random() < prob_entrar:
            num_clientes += 1
            
        # 3. EVENTO SERVICIO (SALIDA)
        if num_clientes > 0:
            prob_atencion = mu_actual * (MINUTOS_POR_PASO / 60)
            
            if random.random() < prob_atencion:
                num_clientes -= 1
        
        # Guardar datos del minuto actual
        registros.append({
            "Minuto": t,
            "Hora": t / 60,
            "Turno": NOMBRES_TURNOS[turno_id],
            "Clientes_en_Sistema": num_clientes,
            "Mu_Actual": mu_actual
        })
        
    # Convertir lista a DataFrame final
    datos_simulacion = pd.DataFrame(registros)
    return datos_simulacion