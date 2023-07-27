def conexao(nome, cp):
    from datetime import date
    import mysql.connector

    db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='cadastro')
    cursor = db_connection.cursor()

    # Inserting data into the database
    sql = "INSERT INTO user (name, cpf) VALUES (%s, %s)"
    values = (nome, cp)  # Using the function parameters here
    cursor.execute(sql, values)
    db_connection.commit()

    # Fetching and displaying all records
    sql = "SELECT id, name, cpf FROM user"
    cursor.execute(sql)
    print("All records:")
    for (id, name, cpf) in cursor:
        print(id, name, cpf)
    print("\n")

    # Fetching and displaying all records after the update
    sql = "SELECT id, name, cpf FROM user"
    cursor.execute(sql)
    print("All records after update:")
    for (id, name, cpf) in cursor:
        print(id, name, cpf)

    cursor.close()
    db_connection.close()

    print("registrado com sucesso")



print("[1]entrar")
print("[2]cadastrar")
print("[3]apagar")
valor = input("->")

nome = input('escreva o seu nome: ')
cp = input('escreva o seu cpf: ')
conexao(nome, cp)
