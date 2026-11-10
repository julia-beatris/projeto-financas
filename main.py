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



   def navegacao(componente):
      item_clicado = componente.control.selected_index
      if item_clicado == 0:
         pagina.navigate("/")
      elif item_clicado == 1:
         pagina.navigate("/")
      elif item_clicado == 2:
         pagina.navigate("/")
      elif item_clicado == 3:
         pagina.navigate("/")
      elif item_clicado == 4:
         pagina.navigate("/login")

   barra_navegacao= ft.NavigationBar(destinations=[
                              ft.NavigationBarDestination(icon=ft.Icons.CATEGORY_OUTLINED, label="Categoria"),
                              ft.NavigationBarDestination(icon=ft.Icons.ADD_CIRCLE_OUTLINE, label="Adicionar Despesas"),
                              ft.NavigationBarDestination(icon=ft.Icons.RECEIPT_LONG_OUTLINED, label="Todas Despesas"),
                              ft.NavigationBarDestination(icon=ft.Icons.PIE_CHART_OUTLINE, label="Despesas por Categoria"),
                              ft.NavigationBarDestination(icon=ft.Icons.LOGOUT_OUTLINED, label="Sair"),],
                              on_change=navegacao)
   

   tela_login_usuario = UsuarioLoginView(pagina)
   tela_cadastro_usuario = CadastroUsuarioView(pagina)
   tela_principal_usuario = PrincipalUsuarioView(pagina)
   tela_principal_usuario.navigation_bar=barra_navegacao
 
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
