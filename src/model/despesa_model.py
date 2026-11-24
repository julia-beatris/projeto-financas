from src.database.conexao import Conexao

class Despesa:
    def __init__(self):
        pass

    @staticmethod
    def incluir(id_categoria:int, descricao:str, valor: float, data:str, login: str) -> int:
        conexao, cursor = Conexao().conectar()
        if conexao == None:
            print("Erro ao tentar conectar!!")
            return None
        try:
            cursor.execute("""
                INSERT INTO tb_despesa
                (id_categoria, descricao, valor, data,login)
                VALUES(%s,%s,%s,%s,%s);
                """,
                [id_categoria,descricao,valor,data,login])
            
            id_despesa = cursor.lastrowid
            conexao.commit()
            conexao.close()

            return id_despesa
        
        except Exception as e:
            print(f"ERRO AO INCLUIR{e}")
            return False


    @staticmethod
    def recuperar_todos(login:str)->list:
        conexao, cursor = Conexao().conectar()
        if conexao == None:
            print("Erro ao tentar conectar!!")
            return False
        try:
            cursor.execute("""
                SELECT tb_despesa.id_categoria, descricao, valor, data,tb_despesa.login, tb_categoria.categoria
                FROM tb_despesa
                inner join tb_categoria on tb_categoria.id_categoria = tb_despesa.id_categoria
                WHERE tb_categoria.login =%s;
                """,
                [login])
            
            despesas = cursor.fetchall()
            conexao.close()
            return despesas
        except Exception as e:
            print(f"ERRO AO RECUPERAR {e}")
            return False



    @staticmethod
    def recuperar_categoria(login:str, id_categoria:int)-> list:
        conexao, cursor = Conexao().conectar()
        if conexao == None:
                    print("Erro ao tentar conectar!!")
                    return False
        try:
            cursor.execute("""
                            SELECT id_categoria, descricao, valor, data,login
                            FROM tb_despesa
                            WHERE login =%s
                            AND id_categoria = %s;
                            """,
                            [login,id_categoria])

            despesa = cursor.fetchall()
            conexao.close()
            return despesa
        except Exception as e:
            print(f"ERRO AO RECUPERAR {e}")
            return False


    @staticmethod
    def excluir (id_despesa:str) -> bool:
        conexao,cursor =Conexao().conectar()
        if conexao == None:
                    print("Erro ao tentar conectar!!")
                    return False
    
        try:
            cursor.execute("""  DELETE FROM tb_despesa
                                WHERE id_despesa =%s;
                            """,
                            [id_despesa])
                
            conexao.commit()
            conexao.close()
            return True
        except Exception as e :
                print(f"ERRO AO EXCLUIR{e}")        
                return False


    @staticmethod
    def alterar (id_despesa:int, id_categoria:int, descricao:str ,valor:float ,data:str, login:str) -> bool:
        conexao, cursor = Conexao().conectar()
        if conexao == None:
                        print("Erro ao tentar conectar!!")
                        return False

        try:
            cursor.execute("""
                            UPDATE tb_despesa
                            SET id_categoria=%s, descricao=%s, valor=%s, data=%s
                            WHERE id_despesa = %s
                            AND login= %s;
                            """,
                            [id_categoria,descricao,valor,data,id_despesa,login])

            conexao.commit()
            conexao.close()
            return True
        
        except Exception as e :
                print(f"ERRO AO ALTERAR{e}")        
                return False

