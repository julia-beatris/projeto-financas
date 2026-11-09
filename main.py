import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import UsuarioLoginView

def main(pagina:ft.Page):

   pagina.title = "feito por julia;)"
   pagina.window.height = 600 #alterando a altura da janela
   pagina.window.width= 500 #alterando a largura da janela

   tela_login_usuario = UsuarioLoginView(pagina)
   tela_cadastro_usuario = CadastroUsuarioView(pagina)
 
   def roteamento(e= None):
      pagina.views.clear()
      if pagina.route == "/cadastro":
         pagina.views.append(tela_cadastro_usuario)

      elif pagina.route == "/login":
         pagina.views.append(tela_login_usuario)

      pagina.update()

   pagina.on_route_change = roteamento
   roteamento()
   pagina.views.append(tela_cadastro_usuario)



ft.run(main)
