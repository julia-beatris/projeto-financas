from src.database.conexao import Conexao

class Usuario:
    def __init__(self):
        pass

    @staticmethod
    def cadastrar(login:str, senha:str) -> bool:
        conexao,cursor = Conexao().conectar()

        try:
            if conexao == None:
                print("Erro ao tentar conectar!!")
                return False
            
            cursor.execute("""
                            INSERT INTO tb_usuario(login, senha)
                            VALUES(%s, %s)
                        """,
                        [login, senha])

            conexao.commit()
            conexao.close()

            return True 

        except Exception as e:
            print(f"ERRO AO INSERIR: {e}")
            return False

    @staticmethod
    def verificar(login:str, senha:str) -> dict:
        conexao,cursor = Conexao().conectar()

        if conexao == None:
            print("Erro ao tentar conectar!!")
            return None

        cursor.execute("""
                         select login, senha from tb_usuario
                         where login = %s
                         and senha = %s;
                        """,
                        [login, senha])

        resultado= cursor.fetchone()

        conexao.close()
        return resultado

        

   