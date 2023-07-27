print("fazendo conexão com o banco....")
import mysql.connector
from mysql.connector import errorcode
try:
    db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='cadastro')
    print("deu certo, conexao feita")
except mysql.connector.Error as error:
    if error.errno  == errorcode.ER_BAD_DB_ERROR:
        print("banco não existe")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("senha ou usuario errado, check ai piao")
    else:
        print(error)

else:
    db_connection.close()
