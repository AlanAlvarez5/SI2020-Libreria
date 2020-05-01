# from model.model import Model

# m = Model()

# m.crear_usuario('Alan', 'alan@mail.com', '4646461251')

# usuario = m.buscar_usuario(1)
# print(usuario)

# campos = ('`nombre_completo` = %s', '`email` = %s', '`telefono` = %s')
# vals = ('Alan Antonio', 'alan@mail2.com', '1111111', 1)

# print(m.actualizar_usuario(campos, vals))

# usuario = m.buscar_usuario(1)
# print(usuario)

# a = m.crear_libro('Ciencia pa', 'elCrixtof', 'CasaPepa', 400, 'Ciencia', 300, 280)
# m.crear_libro('Fisica', 'elCrixtof', 'CasaPepa', 400, 'Ciencia', 300, 280)
# m.crear_libro('Mates', 'elCrixtof', 'CasaPepa', 400, 'Ciencia', 300, 280)
# a = m.buscar_libro(3)
# a = m.buscar_libro_titulo('Fisica')
# a = m.buscar_todos_libros()


# campos = ('`titulo` = %s',)
# vals = ('Hentai', 3)
# a = m.actualizar_libro(campos, vals)

# a = m.eliminar_libro(1)
# print(a)


# m.close_db()

from controller.controller import Controller

c = Controller()
c.start()