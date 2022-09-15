# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas

def es_numerico(cadena):
    try: 
        int(cadena)
        return True
    except ValueError:
        return False



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Utilizar comprensión de listas con condicionales

    # 1)
    # Utilizar comprensión de listas para convertir
    # una lista de números como str en números tipo int
    # sería un conversor string --> int
    # Ojo! Tener cuidado con lo string/caracteres
    # que no son números, utilizar condicionales para detectarlos
    # reemplazar dicho str "no numérico" por 0
    # TIP: Recomendamos ver el método "isdigit" de strings
    # para aplicar en este caso.
    list_numeros_str = ['5', '2', '3', '', '7', 'NaN']
    list_numeros_int = [int(x) if x.isdigit() else 0 for x in list_numeros_str]

    print("sin numeros negativos: ", list_numeros_int)

    # ¿Ya terminaron el ejercicio? ¿Por qué no prueban
    # hacer negativo alguno de los números de la lista?
    # ¿Qué sucede con isdigit? Sorprendente no?

    list_numeros_str = ['-5', '2', '-3', '', '7', 'NaN']
    list_numeros_int = [int(x) if es_numerico(x) else 0 for x in list_numeros_str]
    
    print("con numeros negativos: ", list_numeros_int)        


    print("terminamos")