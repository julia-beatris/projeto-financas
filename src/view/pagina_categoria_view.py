import flet as ft 

class CategoriaView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()

        self.pagina= pagina
        self.route= "/categoria"
        
        self.vertical_alignment="CENTER"
                
        titulo= ft.Text(value="VOU FORMATAR DEPOIS (PAGINA CATEGORIA)",weight="bold",font_family="arial")

        # Centraliza os componentes horizontalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
                
                    
                
        
        self.title = "feito por julia"
        
        # Define a cor de fundo da página
        self.bgcolor = "#e8ecf0"

        self.controls=[titulo]