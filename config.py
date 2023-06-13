import sqlalchemy

from sqlalchemy import create_engine

direccion_servidor = '10.168.180.51:5432'
nombre_bd = 'asisten'
nombre_usuario='postgres'
password='Test1234'
# try: 
#     connection = pyodbc.connect('DRIVER={SQL Server};SERVER=' +
#                                 direccion_servidor+ ';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
#     #ok! conexion exitosa
# except Exception as e:
#     #Atrapar error
#     print("ocurrio un error al conectar a SQL Server: ", e)
engine = create_engine(f'postgresql+psycopg2://{nombre_usuario}:{password}@{direccion_servidor}/{nombre_bd}')