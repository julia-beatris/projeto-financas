from src.database.conexao import Conexao

class Despesa:
    def __init__(self):
        pass

    @staticmethod
    def adicionar(id_categoria:int, descrição:str, valor: float, local:str, login:str) -> int:
        conexao, cursor = Conexao().conectar()
        if conexao == None:
            print("Erro ao tentar conectar")
            return None
        try:
            cursor.execute("""
                INSERT INTO tb_despesa
                (id_categoria, descrição, valor, local, login)
                VALUES(%s,%s,%s,%s,%s)
                """,
                [id_categoria,descrição,valor,local,login])
            id_despesa = cursor.lastrowid
            conexao.commit()
            conexao.close()
            return id_despesa
        except Exception as e:
            print(f"ERRO AO INSERIR {e}")
            return False


    @staticmethod
    def recuperar_todos(login:str)->list:
        conexao, cursor = Conexao().conectar()
        if conexao == None:
            print("Erro ao tentar recuperar")
            return False
        try:
            cursor.execute("""
                SELECT despesa, login from tb_despesa
                WHERE login =%s
                """,
                [login])
            resultado = cursor.fetchall()
            conexao.close()
            return resultado
        except Exception as e:
            print(f"ERRO AO RECUPERAR {e}")
            return False