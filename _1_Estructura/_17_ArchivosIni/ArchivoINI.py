import configparser
import sys

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    #Verifica que las secciones y claves existan
    if ('Maximus'in config and 'basededatos' in config['Maximus'] and 'usuario' in config['Maximus'] and 'contrasennia' in config['Maximus']):
        bd = config['Maximus']['basededatos']
        user = config['Maximus']['usuario']
        password =  config['Maximus']['contrasennia']

        #print(f"El usuario es: {user} , la contraseña es: {password} , la base de datos es: {bd}")
        sys.stdout.write(f"Usuario: {user}")
        sys.stdout.write(f"Contraseña: {password}")
        sys.stdout.write(f"Base de datos: {bd}")