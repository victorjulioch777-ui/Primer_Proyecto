from devspace import create_user, follow_space, get_followers, get_following_spaces, get_posts, get_spaces_by_user, get_users, login, create_space, handle_follower, create_post
from utils import pintar as p, colorear_codigo, es_codigo, escribir_lento
import utils as c
import time as t

def crear_usuario():
    """
    Gestiona la creación de un usuario solicitando datos por consola.

    Solicita al usuario su nombre de usuario, correo electrónico y contraseña,
    y utiliza la función create_user para intentar registrarlo. Repite el proceso
    hasta que el usuario sea creado exitosamente.

    Args:
        None
    
    Returns:
        None
    """
    while True:
        print("===== Creación de usuario =====", c.AZUL)
        username = input(p("Usuario: ", c.AZUL)).strip()
        email = input(p("Email: ", c.AZUL)).strip()
        password = input(p("Contraseña: ", c.AZUL)).strip()

        success,data = create_user(username, email, password)

        if success:
            print("\033[H\033[J")
            print(p("\nUsuario creado exitosamente", c.VERDE))
            t.sleep(3)
            break
        else:
            print("\033[H\033[J")
            print(p("\nSucedio un error", c.ROJO))
            print(p("Vuelve a intentarlo.", c.ROJO))
            t.sleep(3)

def iniciar_sesion():
   """
   Gestiona el inicio de sesión de un usuario mediante consola.

    Solicita al usuario su nombre de usuario y contraseña, y utiliza la función
    login para validar las credenciales. Si el acceso es correcto, retorna el
    nombre de usuario. Si falla, permite reintentar.

    Args:
        None
    
    Returns:
        str: Nombre de usuario si el inicio de sesión es exitoso.
    """
   while True:
        print("\033[H\033[J") 
        print(p("\n===== INICIO DE SESIÓN =====", c.AZUL))
        username = input(p("Usuario: ", c.AZUL)).strip()
        password = input(p("Contraseña: ", c.AZUL)).strip()

        success, data = login(username, password)

        if success:
            print("\033[H\033[J")
            print(p("\nLogin exitoso", c.VERDE_BRIGHT))
            print(p(f"\nBienvenido, {username}", c.VERDE_BRIGHT))
            t.sleep(1)
            return username
        else:
            print("\033[H\033[J")
            print(p("\nUsuario o contraseña incorrectos", c.ROJO))
            print(p("Vuelve a intentarlo.", c.ROJO))
            t.sleep(1)

def mostrar_menu():
    """
    Muestra el menú principal de opciones al usuario.
    
    Presenta en consola las diferentes opciones disponibles del sistema,
    como consultas de usuarios, spaces, seguidores y cierre de sesión.

    Args:
        None

    Returns:
        None
    """
    print("\033[H\033[J")
    print(p("\n===== MENÚ PRINCIPAL =====", c.AZUL_BRIGHT, c.NEGRITA))
    print(p("1.", c.AMARILLO ) +p(" Consulta de usuarios", c.AZUL))
    print(p("2.", c.AMARILLO ) +p(" Consultar space de un usuario", c.AZUL))
    print(p("3.", c.AMARILLO ) +p(" Crear un space", c.AZUL))
    print(p("4.", c.AMARILLO ) +p(" Crear post", c.AZUL))
    print(p("5.", c.AMARILLO ) +p(" Seguir un space", c.AZUL))
    print(p("6.", c.AMARILLO ) +p(" Gestionar solicitudes", c.AZUL))
    print(p("7.", c.AMARILLO ) +p(" Consulta de space seguidos", c.AZUL))
    print(p("8.", c.AMARILLO ) +p(" Consulta de seguidores", c.AZUL))
    print(p("9.", c.AMARILLO ) +p(" Consulta de post por space", c.AZUL))
    print(p("10.", c.AMARILLO ) +p(" Cerrar sesión", c.AZUL))

def ver_users():
    """
    Obtiene y muestra la lista de usuarios registrados.

    Llama a la función get_users para recuperar los usuarios. Si la operación
    es exitosa, muestra la lista numerada en consola. Si no hay usuarios o ocurre
    un error, informa al usuario.

    Args:
        None

    Returns:
        None
    """
    success, data = get_users()

    if success:
        if len(data) == 0:
            print("\033[H\033[J")
            print("\n===== LISTA DE USUARIOS =====")
            print(p("No existe ningun usuario.", c.ROJO))
            t.sleep(3)
        else:
            print("\033[H\033[J")
            print("\n===== LISTA DE USUARIOS =====")
            for i, user in enumerate(data, start=1):
                print(f"{i}. {user}")
                t.sleep(1)
    else:
        print("\033[H\033[J")
        print("\n===== LISTA DE USUARIOS =====")
        print(p("No se pudieron cargar los usuarios.", c.ROJO))
        t.sleep(3)

def ver_spaces_por_usuario():
    """
    Obtiene y muestra los spaces asociados a un usuario.

    Solicita el nombre de usuario por consola y utiliza la función
    get_spaces_by_user para recuperar los spaces vinculados. Si la operación
    es exitosa, muestra la lista numerada. Si no hay spaces o ocurre un error,
    informa al usuario.

    Args:
        None

    Returns:
        None
    """
    print("\033[H\033[J")
    print(p("\n===== VER SPACE POR USUARIO =====", c.NEGRITA, c.AZUL))
    username =  input(p("\nIngresa el usuario del space: ", c.VERDE)).strip()   

    success, data = get_spaces_by_user(username)
    
    if success:
        if len(data) == 0:
            print("\033[H\033[J")
            print(p(f"\n===== LISTA DE SPACES DEL USUARIO {username.upper()} =====", c.NEGRITA, c.AZUL))
            print(p("No existe ningun space.", c.ROJO))
            t.sleep(3)
        else:
            print("\033[H\033[J")
            print(p(f"\n===== LISTA DE SPACES DEL USUARIO {username.upper()} =====", c.NEGRITA, c.AZUL))
            for i, space in enumerate(data, start=1):
                print(f"{i}. {space}")
                t.sleep(1)
    else:
        print("\033[H\033[J")
        print(p(f"\n===== LISTA DE SPACES DEL USUARIO {username.upper()} =====", c.NEGRITA, c.AZUL))
        print(p("No se pudieron cargar los spaces.", c.ROJO))
        t.sleep(3)

def crear_space(usuario):
    """
    Esta funcion se encarga de solicitar al usuario, nombre y descripción 
    y luego intenta crear un space.

    Args:
        usuario (str): Nombre del dueño del space.

    Returns:
        None
    """
    print("\033[H\033[J")
    print(p("\n ===Crear un space===", c.NEGRITA, c.AZUL))
    name = input(p("Ingresa el nombre del space: ", c.AZUL)).strip()
    description = input(p("Ingresa la descripcion del space: ", c.AZUL)).strip()
    
    success, data = create_space(usuario, name, description)

    if success:
        print("\033[H\033[J")
        print("\n ===Crear un space===", c.NEGRITA, c.AZUL)
        print("\nSpace creado exitosamente.")
        t.sleep(3)
    else:
        print("\033[H\033[J")
        print("\n ===Crear un space===", c.NEGRITA, c.AZUL)
        print(p("\Sucedio un error.", c.ROJO))
        print(p("Vuelve a intetarlo", c.AMARILLO))  
        t.sleep(3)

def crear_post():
    """
    Esta funcion se encarga de crear un nuevo post dentro de un space.

    Le solicita al usario el ID del space,titulo,contenido y tipo de post
    y luego intenta crear el post.

    Args:
        None

    Returns:
        None
    """
    print("\033[H\033[J")
    print(p("\n===== Crear un post =====", c.NEGRITA, c.AZUL))
    id = int((input(p("Ingresa el space ID al que pertenecerá el nuevo post: ", c.AZUL))))
    titulo = input(p("Ingresa el Titulo del nuevo post: ", c.AZUL))
    contenido = input(p("Ingresa el Contenido del nuevo post: ", c.AZUL))
    tipo_de_post = input(p("Ingresa el Tipo de post (post): ", c.AZUL))

    success, data = create_post(id, titulo, contenido, tipo_de_post)

    if success:
        print("\033[H\033[J")
        print(p("\n===== Crear un post =====", c.NEGRITA, c.AZUL))
        print(p("\nPost creado exitosamente", c.VERDE))
        print(data)
        t.sleep(3)
    else:
        print("\033[H\033[J")
        print(p("\n===== Crear un post =====", c.NEGRITA, c.AZUL))
        print(p("\nSucedio un error", c.ROJO))
        print(p("Vuelve a intentarlo", c.AMARILLO))
        t.sleep(3)

def seguir_space(usuario):
    """
    Permite a un usuario seguir un space.

    Solicita el nombre de usuario y el ID del space por consola, y utiliza la
    función follow_space para registrar la acción. Informa si la operación fue
    exitosa o si ocurrió un error.

    Args:
        None

    Returns:
        None
    """
    print("\033[H\033[J")
    print(p("\n===== Seguir un space =====\n", c.AZUL, c.NEGRITA))
    user_space = input(p("Ingrese el nombre del usuario que quieres seguir:", c.AZUL))
    success, data = get_spaces_by_user(user_space)

    if success:
        print("\033[H\033[J")
        print(p("\n===== Seguir un space =====", c.AZUL, c.NEGRITA))
        print(p("El usuario: ", c.AZUL) + user_space, p(" tiene los siguiente Spaces", c.AZUL))
        
        for space in data:
            id_espacio, nombre, descripcion = space
            print(p("===== SPACES =====", c.NEGRITA, c.AZUL))
            print(p("ID: ", c.AZUL) + f"{id_espacio}")
            print(p("Nombre: ", c.AZUL) + f"{nombre}")
            print(p("Descripción: ", c.AZUL) + f"{descripcion}\n")
            t.sleep(1)
    else:
        print("\033[H\033[J")
        print(p("\n===== Seguir un space =====", c.AZUL, c.NEGRITA))
        print(p("El", c.ROJO) + f"{user_space}" + p("que ingreso no tiene Spaces", c.ROJO))
        t.sleep(2)

    space_id = input(p("Ingresa el space id que deseas seguir: ", c.AZUL)).strip()

    success, data = follow_space(usuario, space_id)

    if success:
        print("\033[H\033[J")
        print(p("\n===== Seguir un space =====", c.AZUL, c.NEGRITA))
        print(p("\nSpace seguido exitosamente", c.VERDE))
        t.sleep(2)
    else:
        print("\033[H\033[J")
        print(p("\n===== Seguir un space =====", c.AZUL, c.NEGRITA))
        print(p("\nSucedio un error", c.ROJO))
        print(p("Vuelve a intentarlo.", c.ROJO))
        t.sleep(2)

def gestion_solicitudes(usuario):
    print("\033[H\033[J")
    ciclo = True
    while ciclo == True:
        print(p("GESTION DE SOLICITUDES DE SEGUIMIENTO", c.AZUL, c.NEGRITA))
        print(p("Ingrese su ID SPACE", c.AMARILLO))
        space_id = int(input(p("ID del space: ", c.VERDE)))

        print("\033[H\033[J")
        print(p("GESTION DE SOLICITUDES DE SEGUIMIENTO", c.AZUL, c.NEGRITA))
        print(p("Nombre de usuario que solicita seguir", c.AMARILLO))
        user_que_solicita = input(p("Nombre: ", c.VERDE))

        print("\033[H\033[J")
        print(p("GESTION DE SOLICITUDES DE SEGUIMIENTO", c.AZUL, c.NEGRITA))
        print(p(usuario, c.MAGENTA_BRIGHT) + p(" ID del space = ", c.MAGENTA_BRIGHT) + p(space_id, c.CYAN_BRIGHT) + p(": PROCESA A: ", c.MAGENTA_BRIGHT) + p(user_que_solicita, c.CYAN_BRIGHT))
        print(p("1. Aceptar", c.VERDE))
        print(p("2. Rechazar", c.ROJO))
        print("3. Salir")

        opcion = int(input(p("opcion: ", c.VERDE)))
        if opcion == 1:
            estado = True
            ciclo = False
        elif opcion == 2:
            estado = False
            ciclo = False
        else:
            print("\033[H\033[J")
            print(p("GESTION DE SOLICITUDES DE SEGUIMIENTO", c.AZUL, c.NEGRITA))
            print("No existe esa opcion", c.ROJO)
    
    success, data = handle_follower(usuario, space_id, user_que_solicita, estado)

    if success == True:
        print("\033[H\033[J")
        print(p("GESTION DE SOLICITUDES DE SEGUIMIENTO", c.AZUL, c.NEGRITA))
        print(p("Se acepto correctamente a", c.VERDE), p(user_que_solicita, c.CYAN_BRIGHT))
        t.sleep(5)
    else:
        print("\033[H\033[J")
        print(p("GESTION DE SOLICITUDES DE SEGUIMIENTO", c.AZUL, c.NEGRITA))
        print(p("Algo falló, no se pudo aceptar a:", c.ROJO), p(user_que_solicita, c.CYAN_BRIGHT))
        t.sleep(5)

def ver_spaces_seguidos(usuario):
    """
    Obtiene y muestra los spaces que sigue un usuario.

    Recibe el nombre de usuario como parámetro y utiliza la función
    get_following_spaces para recuperar los spaces que sigue. Si la operación
    es exitosa, muestra la lista numerada. Si no sigue ningún space o ocurre
    un error, informa al usuario.

    Args:
        usuario (str): Nombre de usuario.

    Returns:
        None
    """
    success, data = get_following_spaces(usuario)

    if success:
        if len(data) == 0:
            print("\033[H\033[J")
            print(p("\n===== SPACES QUE SIGO =====", c.NEGRITA, c.AZUL))
            print("No sigues ningún space.")
            t.sleep(3)
        else:
            print("\033[H\033[J")
            print(p("\n===== SPACES QUE SIGO =====", c.NEGRITA, c.AZUL))
            for i, space in enumerate(data, start=1):
                print(f"{i}. {space}")
                t.time(3)
    else:
        print("\033[H\033[J")
        print(p("\n===== SPACES QUE SIGO =====", c.NEGRITA, c.AZUL))
        print("No se pudieron cargar los spaces seguidos.")
        t.sleep(3)

def ver_seguidores(usuario):

    """
    Obtiene y muestra los seguidores de un usuario.

    Recibe el nombre de usuario como parámetro y utiliza la función
    get_followers para recuperar la lista de seguidores. Si la operación
    es exitosa, muestra los seguidores numerados. Si no hay seguidores o
    ocurre un error, informa al usuario.

    Args:
        usuario (str): Nombre de usuario.

    Returns:
        None
    """
    success, data = get_followers(usuario)
    
    if success:
        if len(data) == 0:
            print("\033[H\033[J")
            print(p("\n===== SEGUIDORES =====", c.NEGRITA, c.AZUL))
            print("No hay seguidores para mostrar.")
            t.sleep(3)
        else:
            print("\033[H\033[J")
            print(p("\n===== SEGUIDORES =====", c.NEGRITA, c.AZUL))
            for i, follower in enumerate(data, start=1):
                print(f"{i}. {follower}")
            t.sleep(3)
    else:
        print("\033[H\033[J")
        print(p("\n===== SEGUIDORES =====", c.NEGRITA, c.AZUL))
        print("No se pudieron cargar los seguidores.")
        t.sleep(3)

def ver_posts_por_space():
    """
    Obtiene y muestra los posts de un space para un usuario específico.

    Solicita el ID del space y el nombre de usuario por consola, y utiliza la
    función get_posts para recuperar los posts asociados. Si la operación es
    exitosa, muestra los posts numerados. Si no hay posts o ocurre un error,
    informa al usuario.

    Args:
        None

    Returns:
        None
    """
    print("\033[H\033[J")
    print(p("\n===== Post por Space =====", c.NEGRITA, c.AZUL))
    user_space = input(p("Ingrese el nombre dueño del Space: ", c.AZUL))
    success, data = get_spaces_by_user(user_space)
    if success:
        print("\033[H\033[J")
        print(p("\n===== Spaces =====", c.AZUL, c.NEGRITA))
        print(p("El usuario: ", c.AZUL) + user_space, p(" tiene los siguiente Spaces\n", c.AZUL))
        
        for space in data:
            id_espacio, nombre, descripcion = space
            print(p("===== space =====", c.NEGRITA, c.AZUL))
            print(p("ID: ", c.AZUL) + f"{id_espacio}")
            print(p("Nombre: ", c.AZUL) + f"{nombre}")
            print(p("Descripción: ", c.AZUL) + f"{descripcion}\n")
            t.sleep(1)
    else:
        print("\033[H\033[J")
        print(p("\n===== Post por Space =====", c.AZUL, c.NEGRITA))
        print(p("El", c.ROJO) + f"{user_space}" + p("que ingreso no tiene Spaces", c.ROJO))

    space_id = int(input(p("Ingrese el space ID del que desea obtener los posts: ", c.AZUL)))

    success2, data2 = get_posts(space_id, user_space)
    data2 = data2[1]
    if success2:
        if len(data2) == 0:
            print("\033[H\033[J")
            print(p("\n===== Post por Space =====", c.NEGRITA, c.AZUL))
            print(p("No hay posts para mostrar.", c.VERDE))
            t.sleep(2)
        else:
            i = 1
            while True :
                post = data2[i]
                id_post = post[0]
                titulo = post[1]
                contenido = post[2]
                tipo = post[3]

                print(f"{i+1}. Tipo de POST: [{tipo}] Título: {titulo}")
                print(f"Post ID: {id_post}")
                if es_codigo(contenido):
                    contenido_mostrar = colorear_codigo(contenido)
                else:
                    contenido_mostrar = contenido

                print("\033[H\033[J")
                print(p("\n===== Post del Space :", c.NEGRITA, c.AZUL))
                print("Contenido:\n")
                escribir_lento(contenido_mostrar)
                print(p("1) Ver post anterior   ", c.AMARILLO) + p("2) Ver siguiente post   ", c.VERDE) + p("3) Salir"))
                opcion = input(p(">", c.VERDE))

                if opcion == "1":
                    i -= 1
                    if i < 0:
                        i = 0
                elif opcion == "2":
                    i += 1
                    if i >= len(data2):
                        i = len(data2) - 1
                elif opcion == "3":
                    break
                else:
                    print("\033[H\033[J")
                    print(p("\n===== Post del Space :", c.NEGRITA, c.AZUL))
                    print (p("Opcion no valida", c.ROJO))
    else:
        print("\033[H\033[J")
        print(p("\n===== Post por Space =====", c.NEGRITA, c.AZUL))
        print("No se pudieron cargar los posts.")
        t.sleep(3)

def menu_principal(usuario):
    """
    Controla el flujo del menú principal del sistema para un usuario autenticado.

    Recibe el nombre de usuario y muestra el menú de opciones de forma continua.
    Según la opción seleccionada, ejecuta diferentes funcionalidades como ver usuarios,
    consultar spaces, seguir spaces, ver seguidores o cerrar sesión.

    Args:
        usuario (str): Nombre de usuario autenticado.

    Returns:
        None
    """ 
    while True:
        print("\033[H\033[J")
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print(ver_users())

        elif opcion == "2":
            print(ver_spaces_por_usuario())

        elif opcion == "3":
            crear_space(usuario)

        elif opcion == "4":
            crear_post()

        elif opcion == "5":
            seguir_space(usuario)

        elif opcion == "6":
            gestion_solicitudes(usuario)
        
        elif opcion == "7":
            ver_spaces_seguidos(usuario)
        
        elif opcion == "8":
            ver_seguidores(usuario)
        
        elif opcion == "9":
            ver_posts_por_space()

        elif opcion == "10":
            print(p("\nSesión cerrada.", c.VERDE))
            break

        else:
            print(p(" Opción inválida. Intente de nuevo.", c.ROJO))
            t.sleep(3)

def main():
    """
    Controla el flujo principal de la aplicación.

    Muestra el menú de bienvenida y permite al usuario iniciar sesión,
    registrarse o salir del sistema.

    Args:
        None

    Returns:
        None
    """
    while True:
        print("\033[H\033[J")
        print(p("\n===== BIENVENIDO A DevSpace =====", c.NEGRITA, c.VERDE, c.FONDO_BLANCO))
        print(p("1. ", c.AMARILLO) + p("Iniciar Sesion", c.AZUL))
        print(p("2. ", c.AMARILLO) + p("Registrarse", c.AZUL))
        print(p("3. ", c.AMARILLO) + p("Salir", c.AZUL))
        login = input(p("Opcion: ", c.VERDE))
        if login == "1": 
            usuario = iniciar_sesion()
            menu_principal(usuario)
        elif login == "2":
            print("\033[H\033[J") 
            print(crear_usuario())
        elif login == "3":
            print(t.sleep(3))
            print(print("\033c"))
            print("\033[H\033[J")
            print(p("Salió del sistema", c.ROJO))
            exit()
        else:
                print("\033[H\033[J") 
                print(p("\nSucedio un error", c.ROJO))
                print(p("Vuelve a intentarlo.", c.ROJO))
                input(p("Presione enter para Volver a intentar ", c.VERDE))
                t.sleep(3)

if __name__ == "__main__":
    main()
