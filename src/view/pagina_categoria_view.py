import flet as ft 
from src.model.categoria_model import Categoria

class CategoriaView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()

        self.pagina= pagina
        self.route= "/categoria"
        
        self.vertical_alignment="CENTER"

        self.dados_usuario = pagina.session.store.get("usuario_logado")
        
                
        titulo= ft.Text(value="Cadastre aqui a sua Categoria",weight="bold",font_family="arial",size=20)

        subtitulo = ft.Text(value="Categorias existentes:", weight="bold",font_family="arial")

        # Centraliza os componentes horizontalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
                
        self.campo_categoria= ft.TextField(label="Nome da Categoria",
                                            border_color= "#0c0b0b",
                                            border_radius= 8,
                                            border_width= 1,
                                            )

        botao_salvar= ft.Button(content = "Salvar",
                                    bgcolor= "#c0c0c0",
                                    color= "#000000",
                                    width=200,  
                                    on_click= self.cadastrar_categoria
                                    )

        self.lista_categorias = []

        lista= ft.Column(controls=self.lista_categorias)


        self.controls=[titulo,self.campo_categoria,botao_salvar,subtitulo, lista]
        
        self.title = "feito por julia"
        
        # Define a cor de fundo da página
        self.bgcolor = "#e8ecf0"

        self.historico()



    def cadastrar_categoria(self):
        nome_categoria = self.campo_categoria.value

        resultado =Categoria().adicionar(nome_categoria,self.dados_usuario['login'])

        if resultado:
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text("Cadastro da categoria efetuado com sucesso!!!",color="#000000"),bgcolor="#c0fabe"))

            self.historico()

        else:
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text("Erro ao cadastrar a categoria",color="#000000"),bgcolor="#fabebe"))


    def historico(self):

        lista= Categoria.recuperar(self.dados_usuario["login"])
        self.lista_categorias.clear()

        for categorias in lista:
            print(categorias['categoria'])
            self.lista_categorias.append(ft.Text(categorias['categoria']))

        self.pagina.update()



       