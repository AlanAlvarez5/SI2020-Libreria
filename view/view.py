class View:
    def start(self):
        print('-------------------------')
        print('- Bienvenido al Sistema -')
        print('-------------------------')

    def end(self):
        print('-------------------------')
        print('-     Vuelva pronto     -')
        print('-------------------------')
    
    def menu(self):
        print('-------------------------')
        print('-     Menú Principal    -')
        print('-------------------------')
        print(' 1. Prestamos')
        print(' 2. Usuarios')
        print(' 3. Libros')
        print(' 4. Salir')

    def opcion(self, last):
        print('Selecciona una opción (1- '+last+'): ', end = '')
    
    def opcion_incorrecta(self):
        print('* Opción Invalida *')
    
    def pregunta(self, output):
        print(output, end = '')
    
    def msg(self, output):
        print(output)
    
    def ok(self, id, op):
        print('-'*(len(str(id)))+len(op)+24)
        print('- ¡'+(str(id))+' se '+op+' correctamente -')
        print('-'*(len(str(id)))+len(op)+24)

    def error(self, err):
        print(' Error '.center(len(err)+4, '-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    # Nuevo préstamo menú
    def menu_prestamo(self):
        print('-------------------------')
        print('-     Menú Prestamo    -')
        print('-------------------------')
        print(' 1. Nuevo Prestamo')
        print(' 2. Buscar prestamo por ID')
        print(' 3. Buscar prestamo por Usuario')
        print(' 4. Buscar prestamo por Libro')
        print(' 5. Mostrar todos los prestamos')
        print(' 6. Actualizar prestamo')
        print(' 7. Eliminar prestamo')
        print(' 8. Regresar')

    # Usuario  menú
    def menu_usuario(self):
        print('-------------------------')
        print('-     Menú Usuario    -')
        print('-------------------------')
        print(' 1. Nuevo Usuario')
        print(' 2. Buscar Usuario por ID')
        print(' 3. Buscar Usuario por Telefono')
        print(' 4. Mostrar todos los Usuarios')
        print(' 5. Actualizar Usuario')
        print(' 6. Eliminar Usuario')
        print(' 7. Regresar')
    # Libro  menú
    def menu_libro(self):
        print('-------------------------')
        print('-     Menú Prestamo    -')
        print('-------------------------')
        print(' 1. Nuevo Libro')
        print(' 2. Buscar Libro por ID')
        print(' 3. Buscar Libro por Nombre')
        print(' 4. Mostrar todos los Libros')
        print(' 5. Actualizar Libro')
        print(' 6. Eliminar Libro')
        print(' 7. Regresar')