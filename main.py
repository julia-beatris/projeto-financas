import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import UsuarioLoginView
from src.view.principal_usuario_view import PrincipalUsuarioView

def main(pagina:ft.Page):
   ALTURA = 600
   LARGURA = 500

   pagina.title = "feito por julia;)"
   pagina.window.height = ALTURA #alterando a altura da janela
   pagina.window.width= LARGURA #alterando a largura da janela
   pagina.window.left = 1920/2 - LARGURA/2
   pagina.window.top = 1080/2 - ALTURA/2
   

   tela_login_usuario = UsuarioLoginView(pagina)
   tela_cadastro_usuario = CadastroUsuarioView(pagina)
   tela_principal_usuario = PrincipalUsuarioView(pagina)
 
   def roteamento(e= None):
      pagina.views.clear()
      if pagina.route == "/cadastro":
         pagina.views.append(tela_cadastro_usuario)

      elif pagina.route == "/login":
         pagina.views.append(tela_login_usuario)
      elif pagina.route == "/principal":
         pagina.views.append(tela_principal_usuario)
         pagina.window.maximized= True

      pagina.update()

   pagina.on_route_change = roteamento
   roteamento()
   pagina.views.append(tela_login_usuario)



ft.run(main)
