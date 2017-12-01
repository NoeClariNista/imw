# PROGRAM 2.


def show_contacts(phone_book):
    if phone_book == {}:
        print("Vacio.\n")
    else:
        for name, phone in phone_book.items():
            print(f"{name}: {phone}.")
        print()


def add_contacts(phone_book, name, phone):
    if name in phone_book:
        print("El Nombre Ya Existe.\n")
    else:
        phone_book[name] = phone
        print("Usuario Nuevo Añadido.\n")


def remove_contact(phone_book, name):
    if name in phone_book:
        del(phone_book[name])
        print("Usuario Eliminado.\n")
    else:
        print("Ese Usuario No Existe.\n")


def menu():
    phone_book = {}
    while True:
        print("Menu:")
        print("1. Mostrar Lista De Contactos.")
        print("2. Añadir Contacto.")
        print("3. Borrar Contacto.")
        print("4. Salir.")
        option = int(input("Que Opción Desea. \n"))
        if option == 1:
            show_contacts(phone_book)
        elif option == 2:
            print("Agregar Nombre Y Telefono.")
            name = input("Introduce El Nombre Del Nuevo Contacto.\n")
            phone = input("Introduce El Telefono Del Nuevo Contacto.\n")
            add_contacts(phone_book, name, phone)
        elif option == 3:
            name = input("Introduce El Nombre Del Contacto Que Quieres Borrar.\n")
            remove_contact(phone_book, name)
        elif option == 4:
            print("Saliendo.\n")
            break
        else:
            print("Opcion Incorrecta.\n")

menu()
