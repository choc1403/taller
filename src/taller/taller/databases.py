import os

class Database:
    def __init__(self, nombreDB,username, password):
        self.__nombreDB = nombreDB
        self.__username = username
        self.__password = password
    
    @property
    def nombreDB(self):
        if self.__nombreDB == None:
            raise Exception('No se ha definido un nombre para la base de datos')

        return self.__nombreDB
    
    @property
    def username(self):
        if self.__username == None:
            raise Exception('No se ha establecido el username para la base de datos')
        return self.__username
    
    @property
    def password(self):
        if self.__password == None:
            raise Exception('No se ha establecido el password para la base de datos')
        return self.__password


    def sqlite(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        SQLITE = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }

        return SQLITE      

    def postgresql(self):
        try:
        
            POSTGRESQL = {
                'default': {
                    'ENGINE': 'django.db.backends.postgresql_psycopg2',
                    'NAME': os.environ.get('POSTGRES_NAME'),
                    'USER': os.environ.get('POSTGRES_USER'),
                    'PASSWORD':os.environ.get('POSTGRES_PASSWORD'),
                    'HOST': 'db',
                    'PORT': 5432
                }
            }

            return POSTGRESQL

        except Exception as error:
            print('No fue posible realizar dicha operacion')
            print(error)
        
    def mysql(self):
        try:
            
            return {
                'default':{
                    'ENGINE':'django.db.backends.mysql',
                    'NAME':os.environ.get('MYSQL_DATABASE'),
                    'USER': os.environ.get('MYSQL_USER'),
                    'PASSWORD':os.environ.get('MYSQL_PASSWORD'),
                    'HOST': 'db',
                    'PORT':'3306'
                }
            }

        except Exception as error:
            print('No fue posible realizar dicha operacion')
            print(error)



