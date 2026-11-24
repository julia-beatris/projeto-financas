import flet as ft 
from src.model.despesa_model import Despesa
from src.model.categoria_model import Categoria
from datetime import datetime

class AdicionarDespesasView(ft.View):
    def __init__(self,pagina:ft.Page):
      super().__init__()
        
      self.pagina= pagina
      self.route= "/adicionardespesas"
      self.title = "feito por julia"
                      
      # Define a cor de fundo da página
      self.bgcolor = "#e8ecf0"
                    
      self.vertical_alignment="CENTER"
      self.horizontal_alignment="CENTER"
        
      self.dados_usuario = pagina.session.store.get("usuario_logado")
      self.login = self.dados_usuario.get("login")
                
                        
      titulo= ft.Text(value="Cadastre aqui as suas Despesas",weight="bold",font_family="arial",size=20)
    
        
      # Centraliza os componentes horizontalmente
      #self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        
                      
      self.campo_descricao= ft.TextField(label="Descrição da sua despesa:",
                                          border_color= "#0c0b0b",
                                          border_radius= 8,
                                          border_width= 1,
                                                    )

      self.campo_valor= ft.TextField(label="Valor da despesa:",
                                        border_color= "#0c0b0b",
                                        border_radius= 8,
                                        border_width= 1,
                                                         )

      self.campo_data= ft.TextField(label="Data da Despesa:",
                                        border_color= "#0c0b0b",
                                        border_radius= 8,
                                        border_width= 1,
                                                        )

        
      botao_salvar= ft.Button(content = "Salvar",
                              bgcolor= "#c0c0c0",
                              color= "#000000",
                              width=200,  
                              on_click= self.cadastrar_despesas)



      opcoes_categorias= []

      categorias =Categoria().recuperar(self.login)

      for categorias in categorias:
        opcao=  ft.DropdownOption(key=categorias.get("id_categoria"),
                              text= categorias.get("categoria"))
        opcoes_categorias.append(opcao)



      self.campo_categorias= ft.Dropdown( options= opcoes_categorias, label="categorias existentes",)
      self.controls=[titulo,self.campo_descricao, self.campo_valor, self.campo_data, self.campo_categorias, botao_salvar]


    def cadastrar_despesas(self):

      descricao= self.campo_descricao.value
      valor = self.campo_valor.value
      data= self.campo_data.value
      id_categoria =self.campo_categorias.value
      data_convertida = str(datetime.strptime(data, "%d/%m/%Y").date())
      resultado = Despesa().incluir(id_categoria,descricao,valor,data_convertida,self.login)

      if resultado:
        self.pagina.show_dialog(ft.SnackBar(content=ft.Text("Cadastro da despesa efetuado com sucesso!!!",color="#000000"),bgcolor="#c0fabe"))         
      else:
        self.pagina.show_dialog(ft.SnackBar(content=ft.Text("Erro ao cadastrar a despesa",color="#000000"),bgcolor="#fabebe"))
            
       
        
   
        