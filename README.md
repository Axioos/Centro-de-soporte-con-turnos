# Tarea 4b: Simulación de Centro de Soporte

Se simula el funcionamiento de un centro de soporte técnico que opera durante 24 horas. El sistema modela la llegada de clientes y la atención mediante una cola **M/M/1**, donde la capacidad de atención ($\mu$) varía según el turno (Mañana, Tarde, Noche), determinado por una Cadena de Markov.

## Descripción

El programa realiza dos tareas principales:
1.  **Cálculo Teórico:** Obtiene las probabilidades estacionarias de cada turno y calcula métricas esperadas ($L$, $W$).
2.  **Simulación:** Ejecuta una simulación minuto a minuto durante 24 horas para comparar el comportamiento real con el teórico.

## Librerias

El programa requiere las siguientes librerías:
* `numpy` 
* `pandas`
* `matplotlib`

#### Instalación
Ejecuta el siguiente comando en tu terminal para instalar las dependencias:

```bash
pip install numpy pandas matplotlib
```

##### Ejecución
```bash
pip python3 main.py
```