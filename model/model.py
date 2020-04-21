from mysql import connector

class Model:
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()
    
    def close_db(self):
        self.cnx.close()


# Usuario Methods ---------------

    def crear_usuario(self, nombre, email, tel):
        try:
            sql = 'INSERT INTO usuario(`nombre_completo`, `email`, `telefono`) VALUES(%s, %s, %s)'
            vals = (nombre, email, tel)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 
    
    def buscar_usuario(self, id):
        try:
            sql = 'SELECT * FROM usuario WHERE usuario_id = %s'
            vals = (id,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def buscar_todos_usuarios(self):
        try:
            sql = 'SELECT * FROM usuario'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def buscar_usuario_tel(self, tel):
        try:
            sql = 'SELECT * FROM usuario WHERE telefono = %s'
            vals = (tel,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def actualizar_usuario(self, campos, vals):
        # vals = (campo 1, campo2, ... , usuario_id)
        try:
            sql = 'UPDATE usuario SET '+','.join(campos)+' WHERE usuario_id = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def eliminar_usuario(self, id):
        try: 
            sql = 'DELETE FROM usuario WHERE usuario_id = %s'
            vals = (id,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

# Prestamo Methods ---------------------

    def crear_prestamo(self, usuario_id, libro_id, fecha, estatus):
        try:
            sql = 'INSERT INTO prestamo(`usuario_id`, `libro_id`, `fecha`, `estatus`) VALUES(%s, %s, %s, %s)'
            vals = (usuario_id, libro_id, fecha, estatus)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def buscar_prestamo_id(self, id):
        try:
            sql = 'SELECT * FROM prestamo WHERE prestamo_id = %s'
            vals = (id,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def buscar_prestamo_libro(self, id):
        try:
            sql = 'SELECT * FROM prestamo WHERE libro_id = %s'
            vals = (id,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def buscar_prestamo_usuario(self, id):
        try:
            sql = 'SELECT * FROM prestamo WHERE usuario_id = %s'
            vals = (id,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def buscar_todos_prestamos(self):
        try:
            sql = 'SELECT * FROM prestamo'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def actualizar_prestamo(self, campos, vals):
        try:
            sql = 'UPDATE prestamo SET '+','.join(campos)+' WHERE prestamo_id = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def eliminar_prestamo(self, id):
        try: 
            sql = 'DELETE FROM prestamo WHERE prestamo_id = %s'
            vals = (id,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err