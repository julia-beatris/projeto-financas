import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView

def main(pagina:ft.Page):

   pagina.title = "feito por julia;)"
   pagina.window.height = 600 #alterando a altura da janela
   pagina.window.width= 500 #alterando a largura da janela

   tela_cadastro_usuario= CadastroUsuarioView(pagina)
   pagina.views.append(tela_cadastro_usuario)


ft.run(main)
