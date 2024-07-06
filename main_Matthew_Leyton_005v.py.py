from funciones_Matthew_Leyton_005v.py import *
BD = [
    {
        "nombre": "MATTHEW",
        "apellido": "LEYTON",
        "ID": 1,
        "Correo electronico": "Matt.leyton@gmail.com",
        "Compra": [{"fecha": "2024-07-05", "monto total": 45.000, "puntos acumulados": 450}, {"fecha": "2024-07-07", "monto total": 15.000, "puntos acumulados": 258}]
    }
]

print("bienvenidos a gestion del clientede TODOAHORRO")

while True:

    menu()

    opcion = input("ingrese la opcion a ejecutar: ")

    if opcion == "1":
        registrar_cliente(BD)

    elif opcion == "2":
        lista_clientes_registrados(BD)

    elif opcion == "3":
        registrar_compra(BD)

    elif opcion == "4":
        listar_compras_de_un_cliente(BD)

    elif opcion == "5":
        print("Muchas gracias por ejecutar nuestra gestion de clientes, que tenga buen dia")
        break
        
    
else:
    print("ingrese una opcion correcta! >:( )")