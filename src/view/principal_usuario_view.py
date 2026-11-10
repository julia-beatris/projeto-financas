import flet as ft
class PrincipalUsuarioView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()

        self.pagina= pagina
        self.route = "/principal"
        self.vertical_alignment="CENTER"

        dados_usuario = pagina.session.store.get("usuario_logado")
        nome_usuario = dados_usuario.get("usuario")
        
        titulo= ft.Text(value=f"""
        Seja muito bem-vindo{nome_usuario}!É um prazer ter você aqui!Nosso site foi criado pensando em você, para oferecer a melhor experiência, com qualidade, dedicação e confiança.
        Explore nossos conteúdos, conheça nossas novidades e fique à vontade para descobrir tudo o que preparamos especialmente para você.
        Sua presença é muito importante para nós. Aproveite e sinta-se em casa! """,
                            weight="bold",font_family="arial",)
                        
                
    
        self.title = "feito por julia"
        
        # Define a cor de fundo da página
        self.bgcolor = "#e8ecf0"
        # Centraliza os componentes horizontalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.controls = [titulo]











        