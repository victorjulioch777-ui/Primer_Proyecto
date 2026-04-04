from devspace import create_user, follow_space, get_followers, get_following_spaces, get_posts, get_spaces_by_user, get_users, login

def crear_usuario():
    while True:
        print("===== Creación de usuario =====")
        username = input("Usuario: ").strip()
        email = input("Email: ").strip()
        password = input("Contraseña: ").strip()

        success,data = create_user(username, email, password)

        if success:
            print("\nUsuario creado exitosamente")
            break
        else:
            print("\nSucedio un error")
            print("Vuelve a intentarlo.")

def iniciar_sesion():
    while True:
        print("\n===== INICIO DE SESIÓN =====")
        username = input("Usuario: ").strip()
        password = input("Contraseña: ").strip()

        success,data = login(username, password)

        if success:
            print("\nLogin exitoso")
            print(f"\nBienvenido, {username}")
            return username
        else:
            print("\nUsuario o contraseña incorrectos")
            print("Vuelve a intentarlo.")
        
        
def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Consulta de usuarios")
    print("2. Consultar space por usuario")
    print("3. Seguir un space")
    print("4. Consulta de space seguidos")
    print("5. Consulta de seguidores")
    print("6. Consulta de post por space")
    print("7. Cerrar sesión")

def ver_users():
    success, data = get_users()

    print("\n===== LISTA DE USUARIOS =====")
    if success:
        if len(data) == 0:
            print("No existe ningun usuario.")
        else:
            for i, user in enumerate(data, start=1):
                print(f"{i}. {user}")
    else:
        print("No se pudieron cargar los usuarios.")
        print(data)
        
def ver_spaces_por_usuario():
    username =  input("\nIngresa el usuario del space: ").strip()   
       
    success, data = get_spaces_by_user(username)
    
    print(f"\n===== LISTA DE SPACES DEL USUARIO {username.upper()} =====")
    if success:
        if len(data) == 0:
            print("No existe ningun space.")
        else:
            for i, space in enumerate(data, start=1):
                print(f"{i}. {space}")
    else:
        print("No se pudieron cargar los spaces.")
        print(data)

def seguir_space():
        print("\n===== Seguir un space =====")
        username = input("Ingresa tu usuario: ").strip()
        space_id = input("Ingresa el space id que deseas seguir: ").strip()

        success, data = follow_space(username, space_id)

        if success:
            print("\nSpace seguido exitosamente")
        else:
            print("\nSucedio un error")
            print("Vuelve a intentarlo.")

def ver_spaces_seguidos(usuario):
    success, data = get_following_spaces(usuario)

    print("\n===== SPACES QUE SIGO =====")
    if success:
        if len(data) == 0:
            print("No sigues ningún space.")
        else:
            for i, space in enumerate(data, start=1):
                print(f"{i}. {space}")
    else:
        print("No se pudieron cargar los spaces seguidos.")
        print(data)

def ver_seguidores(usuario):
    success, data = get_followers(usuario)

    print("\n===== SEGUIDORES =====")
    if success:
        if len(data) == 0:
            print("No hay seguidores para mostrar.")
        else:
            for i, follower in enumerate(data, start=1):
                print(f"{i}. {follower}")
    else:
        print("No se pudieron cargar los seguidores.")
        print(data)
        
def ver_posts_por_space():
    print("\n===== Seguir un space =====")
    space_id = input("Ingrese el space id del que desea obtener los posts: ").strip()
    username = input("Ingrese el usuario que desea tener los posts: ").strip()

    success, data = get_posts(space_id, username)
    
    if success:
        if len(data) == 0:
            print("No hay posts para mostrar.")
        else:
            for i, post in enumerate(data, start=1):
                print(f"{i}. {post}")
    else:
        print("No se pudieron cargar los posts.")
        print(data)

def menu_principal(usuario):
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            ver_users()

        elif opcion == "2":
            ver_spaces_por_usuario()
            
        elif opcion == "3":
            seguir_space()
        
        elif opcion == "4":
            ver_spaces_seguidos(usuario)
        
        elif opcion == "5":
            ver_seguidores(usuario)
        
        elif opcion == "6":
            ver_posts_por_space()

        elif opcion == "7":
            print("\nSesión cerrada.")
            break

        else:
            print("\n Opción inválida. Intente de nuevo.")

def main():
    while True:
        print("\n===== BIENVENIDO =====")
        print("1. Iniciar sesión")
        print("2. Crear nuevo usuario")
        print("3. Salir")
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            usuario = iniciar_sesion()
            menu_principal(usuario)
        elif opcion == "2":
            crear_usuario()
        elif opcion == "3":
            print("\nGracias por usar el programa.")
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()