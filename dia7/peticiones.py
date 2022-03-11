import requests # Librería para realizar consultas a URLs
from pprint import pprint # Librería para formatear diccionarios

API_KEY = "7eab6a82" # Se obtiene registrandose en imdbapi.com

# Concatenar a una URL a la cual haremos las consultas
titulo = "Avengers" # Selecciono el título de la película a buscar
basic_call = "http://www.omdbapi.com/?apikey="+API_KEY+"&t="+titulo # Concateno la URL para hacer la solicitud

datos_de_pelicula = requests.get(basic_call) # Llamo mediante el método get de la librería request a la URL mencionada arriba

#print(datos_de_pelicula)

datos_de_pelicula = datos_de_pelicula.json() # Y convierto a JSON para ver como diccionario
pprint(datos_de_pelicula)# Datos formateados
print("-----------------") 

#Con los datos recibidos, imprimir:
# "El nombre de la película es <<nombre>>. Su puntuación es <<puntuacion>> y su director es <<director>>"
mi_frase_es = f"El nombre de la pelicula es {datos_de_pelicula['Title']}. Su puntuacion es {datos_de_pelicula['imdbRating']} y su director es {datos_de_pelicula['Director']}"
print(mi_frase_es)

print("-------------")

monto_recaudado = datos_de_pelicula['BoxOffice']  # Obtener los datos y guardar en una variable
print(monto_recaudado)
print(type(monto_recaudado))

# Limpieza de datos (manejo de strings)

#Forma 1: 
quitar_dolar = monto_recaudado[1:]
print(quitar_dolar)
#Forma 2: Recomendado
quitar_excedente = monto_recaudado.replace("$","").replace(",","")
print(quitar_excedente)
monto_total_usd = int(quitar_excedente)
print(type(monto_total_usd))

# Ejercicio: Elegir una casa de cambio y sacar la cotización de Venta 
# Convertir el monto anterior en Gs multiplicando el costo de la película en dólares por su equivalente en Gs.
# Mostrar lo recaudado en la película con el siguiente mensaje:
# "Lo gastado en la película <<nombre_peli>> en Gs. es de <<monto_total_gs>>"

llamada_a_datos = "https://dolar.melizeche.com/api/1.0/" # Llamada a los datos de la API
obtencion_datos = requests.get(llamada_a_datos) # Obtenemos los datos y guardamos en la variable 
datos_json = obtencion_datos.json() # Convertimos mediante el metodo JSON 
pprint(datos_json)

cotizacion_venta_maxicambios = datos_json['dolarpy']['maxicambios']['venta'] # Ingresar clave por clave al valor que necesitamos extraer
pprint(type(cotizacion_venta_maxicambios))

calculo_total = int(cotizacion_venta_maxicambios) * monto_total_usd
print(calculo_total)
print(f"El monto total recaudado en la pelicula {datos_de_pelicula['Title']} en Gs. es de {calculo_total}")



# Crear una función que reciba como parámetro el título de la película.  Y que retorne el dato que devuelva la página en formato .json()
# Pedir por input el título por teclado y llamar a la función

def peticion(titulo_recibido):
    API_KEY= "595695c3"
    basic_call= "http://www.omdbapi.com/?apikey=" + API_KEY +"&t="+titulo_recibido
    datos= requests.get(basic_call)
    datos=datos.json()
    return datos

while True:
    titulo_enviado = input("Ingrese el nombre de una pelicula:")
    resultado = peticion(titulo_enviado)
    pprint(resultado)
    condicion = input("Desea informacion de otra pelicula? NO o SI")
    if condicion =="NO":
        break


print("-----------")
# Se realiza la consulta a los datos extraídos para ver la URL del poster
print(datos_de_pelicula['Poster'])