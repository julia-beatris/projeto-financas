import flet as ft 
from src.model.despesa_model import Despesa

class AdicionarDespesasView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina= pagina
        self.route= "/adicionardespesas"
                    
        self.vertical_alignment="CENTER"
        
        self.dados_usuario = pagina.session.store.get("usuario_logado")
                
                        
        titulo= ft.Text(value="Cadastre aqui as suas Despesas",weight="bold",font_family="arial",size=20)
        
        
        # Centraliza os componentes horizontalmente
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
                        
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

        self.campo_categorias= ft.dropdown(label="Categorias",
                                                    border_color= "#0c0b0b",
                                                    border_radius= 8,
                                                    border_width= 1,
                                                                )
        
        botao_salvar= ft.Button(content = "Salvar",
                                bgcolor= "#c0c0c0",
                                color= "#000000",
                                width=200,  
                                            )
        
        self.lista_categorias = []
        
    
        self.controls=[titulo,self.campo_descricao, self.campo_valor, self.campo_data, self.campo_categorias, botao_salvar]
                
        self.title = "feito por julia"
                
        # Define a cor de fundo da página
        self.bgcolor = "#e8ecf0"
        
   
        