from devspace import handle_follower,get_followers,create_post, create_space, create_user, get_following_spaces,get_users,get_spaces_by_user,create_space,create_post,get_posts,follow_space, login

#Ejemplo de como agregar un nuevo usuario al sistema de DevSpace
if False:
    success, data = create_user("leoviquez", "leoviquez@gmail.com", "12345")
    print(success)
    print(data)
    success, data = create_user("Pedro", "pedro@gmail.com", "11111")
    print(success)
    print(data)
    success, data = create_user("Ana", "ana2@gmail.com", "22222")
    print(success)
    print(data)

#Ejemplo de como obtener la lista de usuarios registrados en el sistema de DevSpace
if False:
    success, data = get_users()
    print(success)
    print(data) 

#Ejemplo de como crear un nuevo espacio en el sistema de DevSpace utilizando una solicitud POST a la API correspondiente.
if False:
    success, data = create_space("leoviquez", "Taller de programación", "Materiales del curso", "public")
    print(success)
    print(data) 

    success, data = create_space("leoviquez", "Examen de Intro", "Ejercicios para el examen", "private")
    print(success)
    print(data) 

    success, data = create_space("Ana", "Diccionarios en Python", "Manejo de diccionarios en Python", "public")
    print(success)
    print(data) 

#Ejemplo de como obtener la lista de espacios asociados a un usuario específico en el sistema de DevSpace
if False:
    success, data = get_spaces_by_user("leoviquez")
    print(success)
    print(data) 
    success, data = get_spaces_by_user("ana")
    print(success)
    print(data) 
    success, data = get_spaces_by_user("pedro")
    print(success)
    print(data) 

#Ejemplo de como crear un nuevo post en el sistema de DevSpace utilizando una solicitud POST a la API correspondiente.
if False:
    success, data = create_post(7, "Introducción a las listas en python", 
                                "Las listas en python son una estructura de datos muy útil, que sirve para almacenar múltiples valores en una sola variable.", 
                                "post")
    print(success)
    print(data) 
    success, data = create_post(8, "Ejemplo de creación de una lista básica en python", 
                                "\n\n```python\nmy_list = [1, 2, 3, 4, 5]\nprint(my_list)\n```\n\nEsto imprimirá: \n\n```\n[1, 2, 3, 4, 5]\n```", 
                                "snippet")
    print(success)
    print(data) 
    success, data = create_post(9, "Ejemplo de creación de un diccionario básico en python", 
                                "\n\n```python\nmy_dict = {'nombre': 'Juan', 'edad': 30}\nprint(my_dict)\n```\n\nEsto imprimirá: \n\n```\n{'nombre': 'Juan', 'edad': 30}\n```", 
                                "snippet")
    print(success)
    print(data) 

#Ejemplo de como obtener la lista de posts asociados a un espacio específico en el sistema de DevSpace utilizando una solicitud POST a la API correspondiente.
if False:
    success,data = get_posts(7, "Ana")
    print(success)
    print(data)
    success,data = get_posts(8, "Ana")
    print(success)
    print(data)

#Ejemplo de como seguir un espacio específico en el sistema de DevSpace utilizando una solicitud POST a la API correspondiente.
if False:
    success, data = follow_space("Ana", 7)
    print(success)
    print(data)
    success, data = follow_space("Ana", 8)
    print(success)
    print(data)

#Ejemplo de como manejar la acción de seguir o dejar de seguir un espacio específico en el sistema de DevSpace utilizando una solicitud POST a la API correspondiente.
if False:
    success, data = handle_follower("leoviquez", 7, "ana", True)
    print(success)
    print(data)
    success, data = handle_follower("leoviquez", 8, "ana", True)
    print(success)
    print(data)

#Ejemplo de como obtener la lista de seguidores asociados a un usuario en el sistema de DevSpace utilizando una solicitud POST a la API correspondiente.
if False:
    success, data = get_followers("leoviquez")
    print(success)
    print(data)

#Ejemplo de como validar un usuario.
if False:
    success, data = login("leoviquez", 12345)
    print(success)
    print(data)

#Ejemplo de como obtener la lista de espacios que un usuario específico está siguiendo en el sistema de DevSpace utilizando una solicitud POST a la API correspondiente.
if True:
    success, data = get_following_spaces("ana")
    print(success)
    print(data)

#Ejemplo de como manejar la acción de seguir o dejar de seguir un espacio específico en el sistema de DevSpace utilizando una solicitud POST a la API correspondiente.
if True:
    success, data = handle_follower("leoviquez", 7, "ana", True)
    print(success)
    print(data)