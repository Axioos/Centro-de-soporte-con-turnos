import matplotlib.pyplot as plt
from configuracion import TASA_LLEGADA, MATRIZ_PROB
from calculos import obtener_pi, generar_reporte
from sim import ejecutar_simulacion

def main():

    # A) Calcular probabilidades estacionarias (usando obtener_pi)
    pi_vector = obtener_pi(MATRIZ_PROB)
    print(f"\nProbabilidades Estacionarias (pi): \n{pi_vector}")
    
    # C) Cálculos teóricos y ponderados
    print("\n--- Métricas Teóricas por Turno ---")
    info_teorica = generar_reporte(TASA_LLEGADA, pi_vector)
    
    for item in info_teorica:
        print(f"Turno {item['Turno']}: "
              f"Rho={item['factor_uso']:.2f}, "
              f"L={item['L']:.2f}, "
              f"W={item['W']:.2f}")

    # B) Ejecutar simulación
    print("\nEjecutando simulación...")
    datos_simulacion = ejecutar_simulacion()
    
    # Mostrar primeras filas para verificar
    print("\nPrimeros registros de la simulación:")
    print(datos_simulacion.head())
    
    # GRAFICAR
    plt.figure(figsize=(10, 6))
    plt.plot(datos_simulacion['Minuto'], datos_simulacion['Clientes_en_Sistema'], 
             label='Evolución Cola', color='blue')
    
    plt.xlabel('Tiempo (Minutos)')
    plt.ylabel('Número de Clientes')
    plt.title('Simulación de Cola con Cambios de Turno (Markov)')
    plt.legend()
    plt.grid(True)
    
    print("\nGenerando gráfico...")
    plt.show()

if __name__ == "__main__":
    main()