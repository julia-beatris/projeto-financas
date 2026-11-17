import flet as ft 

class CategoriaView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()

        self.pagina= pagina
        self.route= "/categoria"
        
        self.vertical_alignment="CENTER"
                
        titulo= ft.Text(value="Cadastre aqui a sua Categoria",weight="bold",font_family="arial",size=20)

        subtitulo = ft.Text(value="Categorias existentes:", weight="bold",font_family="arial")

        # Centraliza os componentes horizontalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
                
        campo_categoria= ft.TextField(label="Nome da Categoria",
                                            border_color= "#0c0b0b",
                                            border_radius= 8,
                                            border_width= 1,
                                            )

        botao_salvar= ft.Button(content = "Salvar",
                                    bgcolor= "#c0c0c0",
                                    color= "#000000",
                                    width=200,  
                                    )


        self.controls=[titulo,campo_categoria,botao_salvar,subtitulo]
        
        self.title = "feito por julia"
        
        # Define a cor de fundo da página
        self.bgcolor = "#e8ecf0"

       