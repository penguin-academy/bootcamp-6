from fastapi import FastAPI, Request #Importo la libreria fastapi
from fastapi.responses import HTMLResponse  #Respuestas HTML 
from fastapi.staticfiles import StaticFiles #Para configuración de archivos estaticos
from fastapi.templating import Jinja2Templates  #Jinja es una librería que maneja los paquetes de renderizado
from pathlib import Path #Se utiliza para especificar una ruta
import requests #Realiza la llamada a una URL y devuelve un dato


app = FastAPI()  #Invoco a la Clase dentro de "app" para invocar a los metodos get
templates = Jinja2Templates(directory="templates") #Linkeo el directorio templates

app.mount("/static", StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"), name="static") #Monto la carpeta static

@app.get("/") #Configuro la ruta raiz
def inicio(request: Request): # Funcion inicio para la página principal (nombre semantico) 
    mis_datos = {
        'nombre' : 'Pinguinitos',
        'hobbie' : 'Bailar'
    }
    return templates.TemplateResponse("inicio.html", {"request": request, "mis_datos": mis_datos}) #Devuelve un dato en forma de diccionario
    #Edit2: a traves de request como valor retornado, se está renderizando el diccionario datos iniciales en la página inicio.html y se muestra con {{mis_datos.nombre}} en el html

# Comando para ejecutar: uvicorn main:app --reload --port 5000
# Con la salvedad de: Guardar el archivo main. 
# Estar en la carpeta servidor
# No tener terminales abiertas.



# Ejercicio: Crear una función que tome el nombre y director de una pelicula y devolver al html lo resuelto

@app.get("/respuesta") #Crear una nueva ruta
def respuesta(request: Request):
    API_KEY= "595695c3" #API key que se consigue en ombdapi.com tras registro
    titulo = "Harry Potter" 
    basic_call= "http://www.omdbapi.com/?apikey=" + API_KEY +"&t="+titulo #Concatenacion de URL a la que se realizará la búsqueda
    datos= requests.get(basic_call) #Se ingresa en datos los datos de respuests
    datos=datos.json() #se convierte a json
   
    titulo_de_pelicula = datos['Title'] #Extraigo el título
    director_de_pelicula = datos['Director'] #Extraigo el director

    datos_filtrados = {'titulo':titulo_de_pelicula, 'director':director_de_pelicula } #Creo el diccionario datos filtrados en el que alojo clave,valor
    return templates.TemplateResponse("respuesta.html", {"request": request, "datos_filtrados": datos_filtrados})  #Retorno al html, los datos filtrados a través de Requests 