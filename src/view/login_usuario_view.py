import flet as ft

class UsuarioLoginView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()

        self.pagina= pagina
        self.route = "/login"
        self.vertical_alignment="CENTER"
        self.horizontal_alignment= "CENTER "
        self.title = "feito por julia"
        # Define a cor de fundo da página
        self.bgcolor = "#e8ecf0"

        titulo= ft.Text(value="TELA DE LOGIN(VOU FAZER DEPOIS!!!!)",weight="bold",font_family="arial",color="#000000")
       
        self.controls=[titulo]