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

        try:
            cursor.execute("""
                                        INSERT INTO tb_categoria(categoria, login )
                                        VALUES(%s, %s);
                                    """,
                                    [categoria, login ])
            
            id_categoria= cursor.lastrowid
            conexao.commit()
            conexao.close()
            return id_categoria
        except Exception as e :
            print(f"ERRO AO INSERIR{e}")        
            return False

                        
    @staticmethod
    
    def recuperar (categoria:str, login:str) -> int:
            conexao,cursor = Conexao().conectar()
            if conexao == None:
                            print("Erro ao tentar conectar!!")
                            return False
    
            try:
                cursor.execute(""" SELECT categoria, login from tb_categoria
                                   WHERE categoria = %s
                                   AND login = %s
                                        """,
                                        [categoria, login ])
    
                conexao.commit()
                conexao.close()
                return True
            except Exception as e :
                print(f"ERRO AO INSERIR{e}")        
                return False

