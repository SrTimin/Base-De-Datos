from pymongo import MongoClient
from bson.objectid import ObjectId

# Conectar a MongoDB
cliente = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.2')
db = cliente['data_base']
coleccion = db['coleccion']

while True:
    print("\nOperaciones CRUD")
    print("1. Crear documento")
    print("2. Leer documentos")
    print("3. Actualizar documento")
    print("4. Eliminar documento")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        # Crear documento
        date = input("Ingresa la fecha (dd/mm/yyyy): ")
        ht = input("Ingresa el equipo local: ")
        at = input("Ingresa el equipo visitante: ")
        hs = int(input("Ingresa los goles del equipo local: "))
        aas = int(input("Ingresa los goles del equipo visitante: "))
        nuevo_doc = {'Date': date, 'HT': ht, 'AT': at, 'HS': hs, 'AS': aas}
        resultado = coleccion.insert_one(nuevo_doc)
        print('Documento creado:', resultado.inserted_id)

    elif opcion == "2":
        # Leer documentos
        documentos = coleccion.find()
        for doc in documentos:
            print(doc)

    elif opcion == "3":
        # Actualizar documento
        id_doc = input("Ingresa el ID del documento a actualizar: ")
        campo = input("Ingresa el campo a actualizar (Date, HT, AT, HS, AS): ")
        nuevo_valor = input(f"Ingresa el nuevo valor para {campo}: ")
        if campo == 'HS' or campo == 'AS':
            nuevo_valor = int(nuevo_valor)
        filtro = {'_id': ObjectId(id_doc)}
        nueva_data = {'$set': {campo: nuevo_valor}}
        coleccion.update_one(filtro, nueva_data)
        print('Documento actualizado')

    elif opcion == "4":
        # Eliminar documento
        id_doc = input("Ingresa el ID del documento a eliminar: ")
        filtro = {'_id': ObjectId(id_doc)}
        coleccion.delete_one(filtro)
        print('Documento eliminado')

    elif opcion == "5":
        # Salir
        break

    else:
        print("Opción inválida. Intenta nuevamente.")