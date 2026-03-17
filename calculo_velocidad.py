# calculo_velocidad.py
# Script de validación de telemetría para buses en Quito

def calcular_velocidad(distancia_m, tiempo_s):
    if tiempo_s <= 0:
        return 0.0
    velocidad_kmh = (distancia_m / tiempo_s) * 3.6
    return round(velocidad_kmh, 2)

if __name__ == "__main__":
    # Simulamos un bus moviéndose 500 metros en 60 segundos
    distancia = 500  
    tiempo = 60      
    
    velocidad = calcular_velocidad(distancia, tiempo)
    print(f"Velocidad registrada: {velocidad} km/h")
    
    # El test: Si el cálculo es incorrecto, el Pipeline fallará
    assert velocidad == 30.0, "Fallo en el cálculo matemático"
    print("Prueba de integración continua superada.")
