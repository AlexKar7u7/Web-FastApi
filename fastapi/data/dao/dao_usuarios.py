from data.modelo.usuario import Usuario

class DaoUsuarios:
    
    def get_all(self,db) -> list[Usuario]:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Usuarios")
        equipos_en_db = cursor.fetchall()
        equipos : list[Usuario] = list()
        for equipo in equipos_en_db:
            usuario = Usuario(equipo[0],equipo[1])
            print(usuario.nombre)
            equipos.append(usuario)
            print(len(equipos))
        
        cursor.close()
        return equipos
        