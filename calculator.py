from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        """
        Método principal para construir a interface do aplicativo.
        Cria o layout, botões e funcionalidades da calculadora.
        """
        # Lista de operadores suportados pela calculadora
        # List of operators supported by the calculator
        self.operators = ["/", "*", "+", "-"]

        # Controle do estado do último botão pressionado
        # Tracks the state of the last button pressed
        self.last_was_operator = None
        self.last_button = None

        # Layout principal com orientação vertical
        # Main layout with vertical orientation
        main_layout = BoxLayout(orientation="vertical")

        # Campo de entrada de texto para exibir a solução (apenas leitura)
        # Text input field to display the solution (read-only)
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)

        # Botões da calculadora organizados em linhas
        # Calculator buttons organized into rows
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]

        # Criação de botões e adição ao layout
        # Creating buttons and adding them to the layout
        for row in buttons:
            h_layout = BoxLayout()  # Layout horizontal para uma linha de botões
            for label in row:
                button = Button(
                    text=label,  # Texto exibido no botão / Text displayed on the button
                    pos_hint={"center_x": 0.5, "center_y": 0.5}  # Posição dentro do layout
                )
                # Vincula o evento de clique ao método on_button_press
                # Binds the click event to the on_button_press method
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)  # Adiciona o botão ao layout horizontal
            main_layout.add_widget(h_layout)  # Adiciona a linha ao layout principal

        # Botão "=" para calcular a solução
        # "=" button to calculate the solution
        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        # Vincula o evento de clique ao método on_solution
        # Binds the click event to the on_solution method
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)  # Adiciona o botão de igualdade ao layout principal

        return main_layout

    def on_button_press(self, instance):
        """
        Método acionado quando um botão é pressionado.
        Atualiza o texto na área de solução com base no botão pressionado.
        """
        # Obtém o texto atual do campo de solução
        # Gets the current text from the solution field
        current = self.solution.text

        # Obtém o texto do botão pressionado
        # Gets the text of the button pressed
        button_text = instance.text

        if button_text == "C":  # Limpa a tela se o botão "C" for pressionado
            # Clears the screen if "C" is pressed
            self.solution.text = ""
        else:
            # Impede a entrada de dois operadores consecutivos
            # Prevents entering two consecutive operators
            if current and (self.last_was_operator and button_text in self.operators):
                return
            # Impede iniciar a expressão com um operador
            # Prevents starting the expression with an operator
            elif current == "" and button_text in self.operators:
                return
            else:
                # Adiciona o texto do botão ao campo de solução
                # Adds the button's text to the solution field
                new_text = current + button_text
                self.solution.text = new_text

            # Atualiza o estado do último botão pressionado
            # Updates the state of the last button pressed
            self.last_button = button_text
            self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        """
        Método acionado ao pressionar o botão "=".
        Avalia a expressão e exibe o resultado no campo de solução.
        """
        # Obtém o texto da solução (expressão a ser avaliada)
        # Gets the solution text (expression to be evaluated)
        text = self.solution.text
        if text:
            try:
                # Avalia a expressão e atualiza o campo de solução com o resultado
                # Evaluates the expression and updates the solution field with the result
                solution = str(eval(self.solution.text))
                self.solution.text = solution
            except Exception:
                # Exibe "Erro" se a expressão for inválida
                # Displays "Error" if the expression is invalid
                self.solution.text = "Erro"


# Executa o aplicativo
# Runs the application
if __name__ == "__main__":
    MainApp().run()
