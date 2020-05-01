from model.model import Model
from view.view import View
from datetime import date

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def start(self):
        self.view.start()
        self.menu()
    
    def menu(self):
        o = '0'
        while o != '4':
            self.view.menu()
            self.view.opcion('4')
            o = input()
            if o == '1':
                self.view.menu_prestamo()
            elif o == '2':
                self.usuario_menu()
            elif o == '3':
                self.libro_menu()
            elif o == '4':
                self.view.end()
            else:
                self.view.opcion_incorrecta()
        return 
    
    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs, vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals

    # Controlador prestamo
    def menu_prestamo(self):
        o = '0'
        while o != '8':
            self.view.menu()
            self.view.opcion('8')
            o = input()
            if o == '1':
                self.nuevo_prestamo()
            elif o == '2':
                self.buscar_prestamo_id()
            elif o == '3':
                self.buscar_prestamo_usuario()
            elif o == '4':
                self.buscar_prestamo_libro()
            elif o == '5':
                self.mostrar_prestamos()
            elif o == '6':
                self.actualizar_prestamo()
            elif o == '7':
                self.eliminar_prestamo()
            elif o == '8':
                return
            else:
                self.view.opcion_incorrecta()
        return 

    def preguntar_prestamo(self):
        self.view.pregunta('ID de usuario: ')
        id_usuario = input()
        self.view.pregunta('ID de libro: ')
        id_libro = input()
        self.view.pregunta('Fecha: ')
        fecha = input()
        self.view.pregunta('Estatus: ')
        estatus = input()
        return [id_usuario, id_libro, fecha, estatus]

    def nuevo_prestamo(self):
        vals = self.preguntar_prestamo()
        out = self.model.crear_prestamo(vals[0], vals[1], vals[2], vals[3])
        if out == True:
            self.view.ok('Nuevo Prestamo', 'agregó')
        else:
            self.view.error('No se pudo agregar prestamo')
        return

    def buscar_prestamo_id(self):
        self.view.pregunta('ID del prestamo: ')
        id = input()
        prestamo = self.model.buscar_prestamo_id(id)
        if type(prestamo) == tuple:
            print(prestamo)
        else:
            if prestamo == None:
                self.view.error('No existe ese prestamo con ese ID')
            else:
                self.view.error('Problema al encontrar el prestamo')
        return 

    def buscar_prestamo_usuario(self):
        self.view.pregunta('ID del usuario: ')
        id = input()
        prestamo = self.model.buscar_prestamo_usuario(id)
        if type(prestamo) == tuple:
            print(prestamo)
        else:
            if prestamo == None:
                self.view.error('No existen prestamos de ese usuario')
            else:
                self.view.error('Problema al encontrar el prestamo')
        return 

    def buscar_prestamo_libro(self):
        self.view.pregunta('ID del libro: ')
        id = input()
        prestamo = self.model.buscar_prestamo_libro(id)
        if type(prestamo) == tuple:
            print(prestamo)
        else:
            if prestamo == None:
                self.view.error('No existen prestamos de ese libro')
            else:
                self.view.error('Problema al encontrar el prestamo')
        return 
    def mostrar_prestamos(self):
        prestamo = self.model.buscar_todos_prestamos()
        if type(prestamo) == tuple:
            print(prestamo)
        else:
            if prestamo == None:
                self.view.error('No existen prestamos')
            else:
                self.view.error('Problema al encontrar el prestamo')
        return 

    def actualizar_prestamo(self):
        self.view.pregunta('ID de prestamo: ')
        id = input()
        prestamo = self.model.buscar_prestamo_id(id)
        if type(prestamo) == tuple:
            print(prestamo)
        else:
            if prestamo == None:
                self.view.error('No existe ese prestamo')
            else:
                self.view.error('Problema al encontrar el prestamo')
            return
        self.view.msg('Ingresa los valores a modificar:')
        todos = self.preguntar_prestamo()
        fields, vals = self.update_lists(['usuario_id', 'libro_id', 'fecha', 'estatus'], todos)
        vals.append(id)
        vals = tuple(vals)
        out = self.model.actualizar_prestamo(fields, vals)
        if out == True:
            self.view.ok(id, 'Actualizado')
        else:
            self.view.error('No se pudo actualizar el prestamo')
        return
    
    def eliminar_prestamo(self):
        self.view.pregunta('ID de prestamo a eliminar: ')
        id = input()
        count = self.model.eliminar_prestamo(id)
        if count != 0:
            self.view.ok(id, 'eliminado')
        else:
            if count == 0:
                self.view.error('Prestamo no existe')
            else:
                self.view.error('Problema al eliminar el prestamo')
    
    # Controlador para libro
    def libro_menu(self):
        o = '0'
        while o != '7':
            self.view.menu_libro()
            self.view.opcion('7')
            o = input()
            if o =='1':
                self.crear_libro()
            elif o == '2':
                self.buscar_libro()
            elif o == '3':
                self.buscar_libro_titulo()
            elif o == '4':
                self.buscar_todos_libros()
            elif o == '5':
                self.actualizar_libro()
            elif o == '6':
                self.eliminar_libro()
            elif o == '7':
                return
    
    def preguntar_libro(self):
        self.view.pregunta('Titulo: ')
        titulo = input()
        self.view.pregunta('Autor: ')
        autor = input()
        self.view.pregunta('Editorial: ')
        editorial = input()
        self.view.pregunta('Numero de paginas: ')
        no_paginas = input()
        self.view.pregunta('Genero: ')
        genero_id = input()
        self.view.pregunta('Cantidad de libros: ')
        cantidad = input()
        self.view.pregunta('Libros disponibles ')
        disponible = input()
        return [titulo, autor, editorial, no_paginas, genero_id, cantidad, disponible]
    
    def crear_libro(self):
        titulo, autor, editorial, no_paginas, genero_id, cantidad, disponible = self.preguntar_libro()
        out = self.model.crear_libro(titulo, autor, editorial, no_paginas, genero_id, cantidad, disponible)
        if out == True:
            self.view.ok(titulo, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL LIBRO ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL LIBRO. REVISA.')
        return

    def buscar_libro(self):
        self.view.pregunta('ID libro: ')
        libro_id = input()
        libro = self.model.buscar_libro(libro_id)
        if type(libro) == tuple:
            self.view.show_libro_header(' Datos del libro '+libro_id+' ')
            self.view.show_libro(libro)
            self.view.show_libro_midder()
            self.view.show_libro_footer()
        else:
               if libro == None:
                    self.view.error('EL LIBRO NO EXISTE')
               else: 
                    self.view.error('PROBLEMA AL LEER EL LIBRO. REVISA.')
        return


    def buscar_libro_titulo(self):
        self.view.pregunta('Titulo: ')
        titulo = input()
        libro = self.model.buscar_libro_titulo(titulo)
        if type(libro) == tuple:
            self.view.show_libro_header(' Datos del libro '+titulo+' ')
            self.view.show_libro(libro)
            self.view.show_libro_midder()
            self.view.show_libro_footer()
        else:
               if libro == None:
                    self.view.error('EL LIBRO NO EXISTE')
               else: 
                    self.view.error('PROBLEMA AL LEER EL LIBRO. REVISA.')
        return


    def buscar_todos_libros(self):
        libros = self.model.buscar_todos_libros()
        if type(libros) == list:
            self.view.show_libro_header(' Todos los libros ')
            for libro in libros:
                self.view.show_libro(libro)
                self.view.show_libro_midder()
            self.view.show_libro_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS LIBROS. REVISA')
        return

    def actualizar_libro(self):
        self.view.pregunta('ID libro: ')
        libro_id = input()
        libro = self.model.buscar_libro(libro_id)
        if type(libro) == tuple:
            self.view.show_libro_header(' Datos del libro '+libro_id+' ')
            self.view.show_libro(libro)
            self.view.show_libro_midder()
            self.view.show_libro_footer()
        else:
                if libro == None:
                    self.view.error('EL LIBRO NO EXISTE')
                else: 
                    self.view.error('PROBLEMA AL LEER EL LIBRO. REVISA.')
                return
        self.view.msg('Ingresa los valores a modificar(vacio para dejarlo igual)')
        whole_vals = self.preguntar_libro()
        fields, vals = self.update_lists(['titulo', 'autor', 'editorial', 'no_paginas', 'genero_id', 'cantidad', 'disponible'], whole_vals)
        vals.append(libro_id)
        vals = tuple(vals)
        out = self.model.actualizar_libro(fields, vals)
        if out == True:
            self.view.ok(libro_id, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL LIBRO. REVISA')
        return

    def eliminar_libro(self):
        self.view.pregunta('ID libro: ')
        libro_id = input()
        count = self.model.eliminar_libro(libro_id)
        if count != 0:
             self.view.ok(libro_id, 'borro')
        else: 
             if count == 0:
                  self.view.error('EL LIBRO NO EXISTE')
             else:
                  self.view.error('PROBLEMA AL BORRAR EL LIBRO. REVISA.')
        return
     
    # Controlador para usuarios
    def usuario_menu(self):
        o = '0'
        while o != '7':
            self.view.menu_usuario()
            self.view.opcion('7')
            o = input()
            if o =='1':
                self.crear_usuario()
            elif o == '2':
                self.buscar_usuario()
            elif o == '3':
                self.buscar_usuario_tel()
            elif o == '4':
                self.buscar_todos_usuarios()
            elif o == '5':
                self.actualizar_usuario()
            elif o == '6':
                self.eliminar_usuario()
            elif o == '7':
                return
    
    def preguntar_usuario(self):
        self.view.pregunta('Nombre: ')
        nombre_completo = input()
        self.view.pregunta('Email: ')
        email = input()
        self.view.pregunta('Telefono: ')
        telefono = input()
        return [nombre_completo, email, telefono]
    
    def crear_usuario(self):
        nombre_completo, email, telefono = self.preguntar_usuario()
        out = self.model.crear_usuario(nombre_completo, email, telefono)
        if out == True:
            self.view.ok(nombre_completo, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL USUARIO ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL USUARIO. REVISA.')
        return

    def buscar_usuario(self):
        self.view.pregunta('ID usuario: ')
        usuario_id = input()
        usuario = self.model.buscar_usuario(usuario_id)
        if type(usuario) == tuple:
            self.view.show_usuario_header(' Datos del libro '+usuario_id+' ')
            self.view.show_usuario(usuario)
            self.view.show_usuario_midder()
            self.view.show_usuario_footer()
        else:
               if usuario_id == None:
                    self.view.error('EL LIBRO NO EXISTE')
               else: 
                    self.view.error('PROBLEMA AL LEER EL LIBRO. REVISA.')
        return


    def buscar_usuario_tel(self):
        self.view.pregunta('Telefono: ')
        telefono = input()
        usuario = self.model.buscar_usuario_tel(telefono)
        if type(usuario) == tuple:
            self.view.show_usuario_header(' Datos del usuario '+telefono+' ')
            self.view.show_usuario(usuario)
            self.view.show_usuario_midder()
            self.view.show_usuario_footer()
        else:
               if usuario == None:
                    self.view.error('EL USUARIO NO EXISTE')
               else: 
                    self.view.error('PROBLEMA AL LEER EL USUARIO. REVISA.')
        return


    def buscar_todos_usuarios(self):
        usuarios = self.model.buscar_todos_usuarios()
        if type(usuarios) == list:
            self.view.show_usuario_header(' Todos los usuarios ')
            for usuario in usuarios:
                self.view.show_usuario(usuario)
                self.view.show_usuario_midder()
            self.view.show_usuario_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS USUARIOS. REVISA')
        return

    def actualizar_usuario(self):
        self.view.pregunta('ID usuario: ')
        usuario_id = input()
        usuario = self.model.buscar_usuario(usuario_id)
        if type(usuario) == tuple:
            self.view.show_usuario_header(' Datos del usuario '+usuario_id+' ')
            self.view.show_usuario(usuario)
            self.view.show_usuario_midder()
            self.view.show_usuario_footer()
        else:
                if usuario == None:
                    self.view.error('EL USUARIO NO EXISTE')
                else: 
                    self.view.error('PROBLEMA AL LEER EL USUARIO. REVISA.')
                return
        self.view.msg('Ingresa los valores a modificar(vacio para dejarlo igual)')
        whole_vals = self.preguntar_usuario()
        fields, vals = self.update_lists(['nombre_completo', 'email', 'telefono'], whole_vals)
        vals.append(usuario_id)
        vals = tuple(vals)
        out = self.model.actualizar_usuario(fields, vals)
        if out == True:
            self.view.ok(usuario_id, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL USUARIO. REVISA')
        return

    def eliminar_usuario(self):
        self.view.pregunta('ID usuario: ')
        usuario_id = input()
        count = self.model.eliminar_usuario(usuario_id)
        if count != 0:
             self.view.ok(usuario_id, 'borro')
        else: 
             if count == 0:
                  self.view.error('EL USUARIO NO EXISTE')
             else:
                  self.view.error('PROBLEMA AL BORRAR EL USUARIO. REVISA.')
        return