import flet as ft 
from datetime import datetime
from src.model.despesa_model import Despesa

class TodasDespesasView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()

        self.pagina= pagina
        self.route= "/despesastotais"
        self.dados_usuario = pagina.session.store.get("usuario_logado")
        self.login = self.dados_usuario.get("login")
                        
        self.vertical_alignment="CENTER"
                
        titulo= ft.Text(value="Aqui está todas as suas Despesas:",weight="bold",font_family="arial")

        # Centraliza os componentes horizontalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER 
        
        self.title = "feito por julia"
        
        # Define a cor de fundo da página
        self.bgcolor = "#e8ecf0"


        botao_mostrar= ft.Button(content = "Mostrar",
                                            bgcolor= "#c0c0c0",
                                            color= "#000000",
                                            width=200, 
                                            on_click=self.mostrar_despesas
                                            )

        self.lista_despesas =[]
        tabela_despesas = ft.DataTable(columns=[ft.DataColumn(label="Usuario"),
                                                ft.DataColumn(label="Descrição"),
                                                ft.DataColumn(label="Valor"),
                                                ft.DataColumn(label="Data"),
                                                ft.DataColumn(label="Categoria")],
                                                rows= self.lista_despesas)

        
        self.controls=[titulo,botao_mostrar,tabela_despesas]

    def mostrar_despesas (self):
        despesas =Despesa().recuperar_todos(self.login)

        for despesas in despesas:
            linha = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(despesas.get("login"))),
                    ft.DataCell(ft.Text(despesas.get("descricao"))),
                    ft.DataCell(ft.Text(despesas.get("valor"))),
                    ft.DataCell(ft.Text(datetime.strftime(despesas.get("data"), "%d/%m/%Y"))),
                    ft.DataCell(ft.Text(despesas.get("id_categoria")))
                ] )

            self.lista_despesas.append(linha)

        self.pagina.update()
            



                                                