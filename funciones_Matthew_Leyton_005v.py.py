def menu():
    opciones = [
        "registrar clientes",
        "listar clientes registrados",
        "registrar compra",
        "listar compras de un cliente",
        "salir del programa",
    ]
    for i, opcion in enumerate(opciones):
        print(f"{i+1}, {opcion}")

def registrar_cliente(BD):
    nombre = input("ingrese el nombre del cliente: ").upper()
    apellido = input("ingrese apellido del cliente: ").upper()
    Correo_electronico = input("ingrese Correo electronico del cliente: ").upper()
    
    
    

    id_cliente = len(BD) + 1

    BD.append(
        {
            "nombre": nombre,
            "apellido": apellido,
            "ID": id_cliente,
            "Correo electronico": Correo_electronico,
            "Compra": []
        }
    )

    print("\nSE HA AGREGADOR UN CLIENTE NUEVO A LA BD!")

def lista_clientes_registrados(BD):
    print("\n los clientes registrados son \n")
    print("nombre\t\tapellido\tID\tCorreo electronico")
    for cliente in BD:
        print(f'{cliente["nombre"]}\t\t{cliente["apellido"]}\t\t{cliente["ID"]}\t{cliente["Correo electronico"]}')
    
    print("\nlistado creado con exito!")

def registrar_compra(BD):
    id = int(input("ingrese el ID del cliente que asiste: "))

    for cliente in BD:
        if cliente["ID"] == id:
            fecha = input("ingrese fecha de compra(AAAA-MM-DD): ")
            monto_total = (input("ingrese monto de Compra: "))
            cliente["Compra"].append(
                {
                    "fecha": fecha,
                    "monto total": monto_total
                }
            )
            print(f"\nse ha agregado un registro de compra a {cliente["nombre"]}{cliente["apellido"]}")

        


def listar_compras_de_un_cliente(BD):
    id = int(input("ingrese el ID del cliente que asiste: "))

    for cliente in BD:
        if cliente["ID"] == id:
            texto = f"ID socio: {id}\n"
            texto += f'nombre cliente: {cliente["nombre"]} {cliente["apellido"]}\n'
            texto += f"fecha de compra\t\tmonto total de la Compra\n"

            monto_total = 0
            for Compra in cliente["Compra"]:
                texto += f'{Compra["fecha"]}\t\t{Compra["monto total"]}\n'
                monto_total += Compra["monto total"]

            texto += f'monto total de la compra: {monto_total} pesos'

            with open(f'ASISTENCIAS_ID_{id}.txt', 'w', encoding="utf-8") as archivo:
                archivo.write(texto)



    