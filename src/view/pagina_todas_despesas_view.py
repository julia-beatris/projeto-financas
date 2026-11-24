import flet as ft 

class TodasDespesasView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()

        self.pagina= pagina
        self.route= "/despesastotais"
        
        self.vertical_alignment="CENTER"
                
        titulo= ft.Text(value="Aqui está todas as suas Despesas:",weight="bold",font_family="arial")

        # Centraliza os componentes horizontalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER 
        
        self.title = "feito por julia"
        
        # Define a cor de fundo da página
        self.bgcolor = "#e8ecf0"

        self.controls=[titulo]

        lista_despesas =[]
        tabela_despesas = ft.DataTable(columns=[ft.DataColumn(label="id da Despesa"),
                                                ft.DataColumn(label="Descrição"),
                                                ft.DataColumn(label="Valor"),
                                                ft.DataColumn(label="Data"),
                                                ft.DataColumn(label="Categoria")],
                                                rows=[ft.DataRow()
                                                ])