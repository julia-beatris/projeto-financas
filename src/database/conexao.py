import mysql.connector

class Conexao:
    def __init__(self):
        pass


    @staticmethod
    def conectar ():

        try:
            #criar a coexão com o banco de dados mysql
            conexao = mysql.connector.connect(host= "localhost",
                                            port= 3306,
                                            user= "root",
                                            password="root",
                                            database= "projeto_financa")

            cursor = Conexao().cursor()

            return  conexao, cursor
        except Exception as e: 
            print(f"ERRO:{e}")
            return None, None