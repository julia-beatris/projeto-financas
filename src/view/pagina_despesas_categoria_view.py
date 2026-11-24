import flet as ft 
from src.model.despesa_model import  Despesa
from src.model.categoria_model import Categoria
from datetime import datetime



class DespesasCategoriaView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()

        self.pagina= pagina
        self.route= "/despesascategoria"
        self.dados_usuario = pagina.session.store.get("usuario_logado")
        self.login = self.dados_usuario.get("login")
                                
        
        self.vertical_alignment="CENTER"
                
        titulo= ft.Text(value="Despesas por categoria",weight="bold",font_family="arial")

        # Centraliza os componentes horizontalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            
        self.title = "feito por julia"
        
        # Define a cor de fundo da página
        self.bgcolor = "#e8ecf0"

    


        opcoes_categorias= []

        categorias =Categoria().recuperar(self.login)

        for categorias in categorias:
            opcao=  ft.DropdownOption(key=categorias.get("id_categoria"),
                                    text= categorias.get("categoria"))
            opcoes_categorias.append(opcao)



        self.campo_categorias= ft.Dropdown( options= opcoes_categorias, label="categorias existentes", on_select= self.mostrar_despesas)
        #self.controls=[titulo,self.campo_categorias]




            
        self.lista_despesas =[]
        tabela_despesas = ft.DataTable(columns=[ft.DataColumn(label="Usuario"),
                                                    ft.DataColumn(label="Descrição"),
                                                    ft.DataColumn(label="Valor"),
                                                    ft.DataColumn(label="Data"),
                                                    ft.DataColumn(label= "Excluir despesa")],
                                                    rows= self.lista_despesas)

        self.mostrar_despesas()
        self.controls=[titulo,self.campo_categorias,tabela_despesas]

    def mostrar_despesas (self):
        self.lista_despesas.clear()
        id_categoria= self.campo_categorias.value
        despesas =Despesa().recuperar_categoria(self.login,id_categoria)

        for despesas in despesas:
            linha = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(despesas.get("login"))),
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
    

   