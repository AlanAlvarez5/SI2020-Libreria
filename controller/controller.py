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
                self.view.menu_usuario()
            elif o == '3':
                self.view.menu_libro()
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