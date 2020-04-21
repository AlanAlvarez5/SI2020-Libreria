from model.model import Model

m = Model()

# m.crear_usuario('Alan', 'alan@mail.com', '4646461251')

# usuario = m.buscar_usuario(1)
# print(usuario)

# campos = ('`nombre_completo` = %s', '`email` = %s', '`telefono` = %s')
# vals = ('Alan Antonio', 'alan@mail2.com', '1111111', 1)

# print(m.actualizar_usuario(campos, vals))

# usuario = m.buscar_usuario(1)
# print(usuario)

m.close_db()