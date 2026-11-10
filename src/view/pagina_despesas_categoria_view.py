import flet as ft 

class DespesasCategoriaView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()

        self.pagina= pagina
        self.route= "/despesascategoria"
        
        self.vertical_alignment="CENTER"
                
        titulo= ft.Text(value="VOU FORMATAR DEPOIS (PAGINA DESPESAS CATEGORIA)",weight="bold",font_family="arial")

        # Centraliza os componentes horizontalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
                
                    
                
        
        self.title = "feito por julia"
        
        # Define a cor de fundo da página
        self.bgcolor = "#e8ecf0"

        self.controls=[titulo]