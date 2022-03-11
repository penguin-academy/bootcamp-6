'''
REPASO: Diccionarios
Compuestos por `clave` y `valor`, son tipos de datos que se alojan en una variable 
y manipulados mediante la sintaxis:
'''

mi_diccionario = {
    'clave': 'valor'
}

print(mi_diccionario['clave'])
print("-----------------------")

# Crear un diccionario datos_personales que va a contener las claves nombre, apellido, edad y celular

datos_personales = {
    'nombre':'Steven Rey',
    'apellido': 'Britez Toledo',
    'edad': 24,
    'celular': 595985187623,
    'hobbie': 'bailar'
}

print(datos_personales)

# Ejercicio: Agregar a la lista anterior la clave "hobbie" y rellenar con datos personales para crear la siguiente concatenación:
# "Hola, mi nombre es <<nombre>>, me gusta <<hobbie>> y estoy acá para aprender lo básico del desarrollo web"

#Solución de un/a participante
print("Hola, mi nombre es "+datos_personales['nombre']+", me gusta "+datos_personales['hobbie']+" y estoy aca para aprender lo basico de desarrollo web")

#Solución #2 : Recomendada
mi_frase = f"Hola, mi nombre es {datos_personales['nombre']}, me gusta {datos_personales['hobbie']} y estoy aca para aprender lo basico de desarrollo web"
print(mi_frase)

