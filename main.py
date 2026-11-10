import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import UsuarioLoginView
from src.view.principal_usuario_view import PrincipalUsuarioView
from src.view.pagina_categoria_view import CategoriaView
from src.view.pagina_adicionar_despesa_view import AdicionarDespesasView
from src.view.pagina_despesas_categoria_view import DespesasCategoriaView
from src.view.pagina_todas_despesas_view import TodasDespesasView

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
         pagina.navigate("/categoria")
      elif item_clicado == 1:
         pagina.navigate("/adicionardespesas")
      elif item_clicado == 2:
         pagina.navigate("/despesastotais")
      elif item_clicado == 3:
         pagina.navigate("/despesascategoria")
      elif item_clicado == 4:
         pagina.navigate("/login")

   barra_navegacao= ft.NavigationBar(destinations=[
                              ft.NavigationBarDestination(icon=ft.Icons.CATEGORY_OUTLINED, label="Categoria"),
                              ft.NavigationBarDestination(icon=ft.Icons.ADD_CIRCLE_OUTLINE, label="Adicionar Despesas"),
                              ft.NavigationBarDestination(icon=ft.Icons.RECEIPT_LONG_OUTLINED, label="Todas Despesas"),
                              ft.NavigationBarDestination(icon=ft.Icons.PIE_CHART_OUTLINE, label="Despesas por Categoria"),
                              ft.NavigationBarDestination(icon=ft.Icons.LOGOUT_OUTLINED, label="Sair"),],
                              on_change=navegacao)
   
 
   def roteamento(e= None):
      pagina.views.clear()
      if pagina.route == "/cadastro":
         tela_cadastro_usuario = CadastroUsuarioView(pagina)
         pagina.views.append(tela_cadastro_usuario)

      elif pagina.route == "/login":
         tela_login_usuario = UsuarioLoginView(pagina)
         pagina.views.append(tela_login_usuario)

      elif pagina.route == "/principal":
         tela_principal_usuario = PrincipalUsuarioView(pagina)
         tela_principal_usuario.navigation_bar=barra_navegacao
         pagina.views.append(tela_principal_usuario)

         pagina.window.maximized= True
      elif pagina.route == "/categoria":
         tela_categoria = CategoriaView(pagina)
         tela_categoria.navigation_bar=barra_navegacao
         pagina.views.append(tela_categoria) 

      elif pagina.route == "/adicionardespesas":
         tela_adicionar_despesas = AdicionarDespesasView(pagina)
         tela_adicionar_despesas.navigation_bar=barra_navegacao
         pagina.views.append(tela_adicionar_despesas) 

      elif pagina.route == "/despesastotais":
         tela_todas_despesas = TodasDespesasView(pagina)
         tela_todas_despesas.navigation_bar=barra_navegacao
         pagina.views.append(tela_todas_despesas)   
       
      elif pagina.route == "/despesascategoria":
         tela_despesas_categoria = DespesasCategoriaView (pagina)
         tela_despesas_categoria.navigation_bar=barra_navegacao
         pagina.views.append(tela_despesas_categoria)   
       
       
      pagina.update()

   pagina.on_route_change = roteamento
   roteamento()
   pagina.navigate("/login")



ft.run(main)
