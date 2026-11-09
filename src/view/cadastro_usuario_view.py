import flet as ft
from src.model.usuario_model import Usuario

class CadastroUsuarioView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()

        self.pagina= pagina

        self.vertical_alignment="CENTER"
        
        titulo= ft.Text(value="Criar nova conta",weight="bold",font_family="arial")
        subtitulo= ft.Text(value="Preencha os dados abaixo:")
        

        self.title = "feito por julia"

        # Define a cor de fundo da página
        self.bgcolor = "#e8ecf0"
        

        # Centraliza os componentes horizontalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    

        self.campo_usuario= ft.TextField(label="Novo Usuario",
                                border_color= "#0c0b0b",
                                border_radius= 8,
                                border_width= 1,
                              )

        self.campo_senha= ft.TextField(label="Senha",
                                        border_color= "#0c0b0b",
                                        border_radius= 8,
                                        border_width= 1,
                                        password=True,
                                        can_reveal_password=True,)

        botao_cadastrar= ft.Button(content = "Cadastrar",
                    bgcolor= "#c0c0c0",
                    color= "#000000",
                    width=200,
                    on_click=self.cadastrar,
                    )

        

        botao_login= ft.Button(content = "Voltar ao login",
                            bgcolor= "#c0c0c0",
                            color= "#000000",
                            width=200,
                            on_click=self.ir_para_login,
                            )


        self.controls=[titulo, subtitulo,self.campo_usuario, 
                        self.campo_senha, botao_cadastrar,botao_login]

        
    def cadastrar(self):
        usuario= self.campo_usuario.value
        senha= self.campo_senha.value

        if usuario == "" or senha== "":
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text("Preencha todos os campos!!",color="#000000"),bgcolor="#edfabe"))
            return
            

        resultado= Usuario().cadastrar(usuario,senha)

        if resultado == True:
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text("Cadastro efetuado com sucesso!!",color="#000000"),bgcolor="#befacb"))

        else:
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text("Erro ao cadastrar.Entre em contato com o adiministrador!!",color="#000000"),bgcolor="#ffb2b2"))

    async def ir_para_login(self):
        await self.pagina.push_route("/login")
        


            


            

        

      
        