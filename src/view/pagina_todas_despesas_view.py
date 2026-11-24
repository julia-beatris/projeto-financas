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


        self.lista_despesas =[]
        tabela_despesas = ft.DataTable(columns=[ft.DataColumn(label="Usuario"),
                                                ft.DataColumn(label="Categoria"),
                                                ft.DataColumn(label="Descrição"),
                                                ft.DataColumn(label="Valor"),
                                                ft.DataColumn(label="Data"),
                                                ft.DataColumn(label= "Excluir despesa")],
                                                rows= self.lista_despesas)

        self.mostrar_despesas()
        self.controls=[titulo,tabela_despesas]

    def mostrar_despesas (self):
        self.lista_despesas.clear()
        despesas =Despesa().recuperar_todos(self.login)

        for despesas in despesas:
            linha = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(despesas.get("login"))),
                    ft.DataCell(ft.Text(despesas.get("categoria"))),
                    ft.DataCell(ft.Text(despesas.get("descricao"))),
                    ft.DataCell(ft.Text(despesas.get("valor"))),
                    ft.DataCell(ft.Text(datetime.strftime(despesas.get("data"), "%d/%m/%Y"))),
                    ft.DataCell(ft.IconButton(icon=ft.Icons.DELETE,
                                              key=despesas.get("id_despesa"),
                                              on_click= self.excluir)),
                ] )

            self.lista_despesas.append(linha)

        self.pagina.update()


    def excluir(self,botao):
        id_despesa = botao.control.key
        Despesa.excluir(id_despesa)
        self.mostrar_despesas()
    
            



                                                