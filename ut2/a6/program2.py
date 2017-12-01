# PROGRAM 2.


def show_contacts(phone_book):
    if phone_book == {}:
        print("Vacio.")
    else:
        for name, phone in phone_book.items():
            print(f"{name}: {phone}.")


def add_contacts(phone_book, name, phone):
    if name in phone_book:
        print("El Nombre Ya Existe.")
    else:
        phone_book[name] = phone
        print("Usuario Nuevo Añadido.")


def remove_contact(phone_book, name):
    if name in phone_book:
        del(phone_book[name])
        print("Usuario eliminado.")
    else:
        print("Ese Usuario No Existe.")


def menu():
    phone_book = {}
    option = 0
    while option != 4:
        print("Menu:")
        print("1. Mostrar Lista De Contactos.")
        print("2. Añadir Contacto.")
        print("3. Borrar Contacto.")
        print("4. Salir.")
        option = int(input("Que Opcion Desea. \n"))
        if option == 1:
            show_contacts(phone_book)
        if option == 2:
            print("Agregar Nombre Y Telefono.")
            name = input("Introduce El Nombre Del Nuevo Contacto.\n")
            phone = input("Introduce El Telefono Del Nuevo Contacto.\n")
            add_contacts(phone_book, name, phone)
        elif option == 3:
            name = input("Introduce El Nombre Del Contacto Que QuieresBorrar.")
            remove_contact(phone_book, name)
        elif option == 4:
            print("Saliendo.")
            break
        else:
            print("Opcion Incorrecta.\n")

menu()
