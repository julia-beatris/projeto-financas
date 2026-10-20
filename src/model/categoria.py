from src.database.conexao import Conexao

class Categoria:
    def __init__(self):
        pass

    @staticmethod

    def adicionar (categoria:str, login:str) -> int:
        conexao,cursor = Conexao().conectar()
        if conexao == None:
                        print("Erro ao tentar conectar!!")
                        return False

        cursor.execute("""
                                    INSERT INTO tb_usuario(categoria, login )
                                    VALUES(%s, %s)
                                """,
                                [categoria, login ])
        
                    


