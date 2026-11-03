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
    
    def recuperar ( login:str) -> list:
            conexao,cursor = Conexao().conectar()
            if conexao == None:
                            print("Erro ao tentar conectar!!")
                            return False
    
            try:
                cursor.execute(""" SELECT categoria, login from tb_categoria
                                   WHERE login = %s
                                  
                                        """,
                                        [login ])
    
                resultado= cursor.fetchall()
                conexao.close()
                return resultado
            except Exception as e :
                print(f"ERRO AO INSERIR{e}")        
                return False


    @staticmethod

    def excluir (id_categoria:str) -> bool:
        conexao,cursor =Conexao().conectar()
        if conexao == None:
                                    print("Erro ao tentar conectar!!")
                                    return False

        try:
            cursor.execute("""  DELETE FROM tb_categoria
                                WHERE id_categoria =%s
                                                """,
                                        [id_categoria])
            
            conexao.commit()
            conexao.close()
            return True
        except Exception as e :
            print(f"ERRO AO INSERIR{e}")        
            return False

