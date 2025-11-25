import os
import matplotlib.pyplot as plt
from configuracion import TASA_LLEGADA, MATRIZ_PROB
from calculos import obtener_pi, generar_reporte
from sim import ejecutar_simulacion 

def main():
    #A)Calcular probabilidades estacionarias
    pi_vector = obtener_pi(MATRIZ_PROB)
    print(f"\nProbabilidades Estacionarias (pi): \n{pi_vector}")
    
    #C)Cálculos teóricos
    print("\n--- Métricas Teóricas por Turno ---")
    info_teorica = generar_reporte(TASA_LLEGADA, pi_vector)
    
    for item in info_teorica:
        print(f"Turno {item['Turno']}: "
              f"Rho={item['factor_uso']:.2f}, "
              f"L={item['L']:.2f}, "
              f"W={item['W']:.2f}")
        
    #CÁLCULO PONDERADO GLOBAL:
    l_global = sum(d['L'] * d['Prob_Estacionaria'] for d in info_teorica)
    w_global = sum(d['W'] * d['Prob_Estacionaria'] for d in info_teorica)
    rho_global = sum(d['factor_uso'] * d['Prob_Estacionaria'] for d in info_teorica)
    
    print("\nMétricas Globales Ponderadas (Promedios):")
    print(f"ρ: {rho_global:.2f}")
    print(f"L (Clientes): {l_global:.2f}")
    print(f"W (Tiempo): {w_global:.2f} horas")

    #B) Ejecutar simulación
    print("\nEjecutando simulación...")
    datos_simulacion = ejecutar_simulacion()
    
    #Mostrar primeras filas para verificar
    print("\nPrimeros registros de la simulación:")
    print(datos_simulacion.head())
    
    #GRÁFICOS:
    plt.figure(figsize=(10, 6))
    plt.plot(datos_simulacion['Minuto'], datos_simulacion['Clientes_en_Sistema'], 
             label='Evolución Cola', color='blue')
    
    plt.xlabel('Tiempo (Minutos)')
    plt.ylabel('Número de Clientes')
    plt.title('Nivel de Congestión del Centro de Soporte por Turnos')
    plt.legend()
    plt.grid(True)
    
    # Lógica para guardar graficos
    nombre_carpeta = "graficos"
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)
        print(f"\nCarpeta '{nombre_carpeta}' creada.")
    
    ruta_archivo = os.path.join(nombre_carpeta, "graf.png")
    plt.savefig(ruta_archivo)
    print(f"\nGráfico guardado exitosamente en: {ruta_archivo}")
    
    plt.close()

if __name__ == "__main__":
    main()