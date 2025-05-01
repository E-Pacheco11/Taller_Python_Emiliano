import mariadb


def conectar_y_consultar():
    try:
        conexion = mariadb.connect(
            #host = "192.168.0.6"
            host =  "localhost",
            database = "almacen",
            user = "root",
            password = "",
            port = 3306
        )
        print(type(conexion))
        print("Conexion a la base de datos del servidor Ounus")

        cursor = conexion.cursor()
        consulta = "SELECT * FROM Usuarios"
        cursor.execute(consulta)

        resultados = cursor.fetchall()
        print("resultados:" , type(resultados))
        print("Datos en la tabla:")
        for fila in resultados:
            # print (fila)
            print(f"ID: {fila[0]}, Nombre de usuario:{fila[1]}, Correo electronico:{fila[2]}, Contraseña: {fila[3]}, Id_Rol:{fila[4]}")
    except mariadb.Error as e:
        print(f"Error al conectar con la base de datos: {e}")

    finally:
        #cerrar la conexion y el cursor si estan abiertos
        if 'cursor' in locals() and cursor:
            cursor.close()
            print("Conexion finalizada")

if __name__ == '__main__':
    conectar_y_consultar()