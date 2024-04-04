## Descripción

Este proyecto es un programa CRUD en Python que se conecta a una base de datos MongoDB.

## Requerimientos

- Python 3.8 o superior
- MongoDB 4.4 o superior
- Un entorno virtual de Python
  Instalación de Python

    Abre una terminal.
    Actualiza el gestor de paquetes de tu sistema con el comando: sudo apt update
    Instala Python con el comando: sudo apt install python3.8
    Verifica la instalación con el comando: python3 --version

Instalación de MongoDB

  Importa la clave pública utilizada por el sistema de gestión de paquetes con el siguiente comando: wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
  
  Crea un archivo de lista para MongoDB con el comando: echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
  
  Recarga la base de datos local de paquetes con el comando: sudo apt-get update
  
  Instala MongoDB con el comando: sudo apt-get install -y mongodb-org
  
  Inicia MongoDB con el comando: sudo systemctl start mongod
  
  Verifica que MongoDB ha iniciado correctamente con el comando: sudo systemctl status mongod
  
  Habilita el inicio automático de MongoDB al arrancar el sistema con el comando: sudo systemctl enable mongod

Configuración del Entorno Virtual

  Crea un entorno virtual utilizando el siguiente comando: python3 -m venv env
  Activa el entorno virtual en Linux: source env/bin/activate
  Una vez activado el entorno virtual, instala pymongo (un controlador de MongoDB para Python) utilizando el siguiente comando: pip install pymongo

## Conexión a la Base de Datos

Este programa se conecta a una base de datos MongoDB local en la dirección `mongodb://127.0.0.1:27017/`. La base de datos se llama `data_base` y la colección se llama `coleccion`.

## Esquema de la Base de Datos

La base de datos utiliza el siguiente esquema para los documentos:

json
{
    "Date": "dd/mm/yyyy",
    "HT": "Equipo local",
    "AT": "Equipo visitante",
    "HS": "Goles del equipo local",
    "AS": "Goles del equipo visitante"
}

## Importar la Base de Datos

Para importar la base de datos desde el archivo matches.csv, puedes usar la herramienta mongoimport de MongoDB:

mongoimport --type csv -d data_base -c coleccion --headerline --drop matches.csv

Este comando importará los datos del archivo matches.csv a la colección coleccion de la base de datos data_base.

## Uso del Programa

  Clona el repositorio: git clone https://github.com/SrTimin/Base-De-Datos.git
  
  Navega hasta el directorio del proyecto: cd tu-proyecto
  
  Activa el entorno virtual.
  
  Ejecuta el programa: python main.py

Una vez que el programa esté en ejecución, puedes seleccionar una opción del menú CRUD para interactuar con la base de datos.
