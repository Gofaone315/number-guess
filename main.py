import webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from random import randint
from kivy.clock import Clock

class LuckyGuessApp(App):
    def build(self):
     
        Window.clearcolor = (0.15, 0.15, 0.15, 1)  # Set background color

        self.coin_count = 0
        self.guesses = 0
        self.random_num = randint(1, 10)

        layout = FloatLayout()

        # Header
        header = Label(text='Lucky Guess', font_size=96, bold=True, color=(0, 0, 1, 1), size_hint=(None, None), size=(800, 120), pos_hint={'center_x': 0.5, 'top': 0.9})
        layout.add_widget(header)

        # Number input and submit button
        input_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(600, 160), pos_hint={'center_x': 0.5, 'top': 0.7})
        input_label = Label(text='Pick a number from (1-10)', font_size=48, color=(1, 0, 0, 1))
        self.input_field = TextInput(multiline=False, hint_text='Enter a number', size_hint=(None, None), size=(500, 80), font_size=36)
        input_layout.add_widget(input_label)
        input_layout.add_widget(self.input_field)
        layout.add_widget(input_layout)

        submit_btn = Button(text='Submit?', size_hint=(None, None), size=(200, 80), pos_hint={'center_x': 0.5, 'top': 0.5}, background_color=(0, 0.6, 0.5, 1), font_size=36)
        submit_btn.bind(on_press=self.check_guess)
        layout.add_widget(submit_btn)

        self.output_label = Label(text='', font_size=38, size_hint=(None, None), size=(400, 100), pos_hint={'center_x': 0.5, 'top': 0.6}, color=(1, 1, 1, 1))
        layout.add_widget(self.output_label)

        self.coin_count_label = Label(text='Coins: 0', font_size=36, size_hint=(None, None), size=(300, 60), pos_hint={'center_x': 0.5, 'top': 0.95}, color=(1, 0.647, 0, 1))
        layout.add_widget(self.coin_count_label)

        return layout
        
    def check_guess(self, instance):
        try:
            guess = int(self.input_field.text)
            self.guesses += 1

            if 1 <= guess <= 10:
                if guess == self.random_num:
                    self.coin_count += 5
                    self.output_label.text = f'You won! Guessed in {self.guesses} attempts. \nYou won 5 coins!'
                    self.guesses = 0
                    self.random_num = randint(1, 10)
                elif guess < self.random_num:
                    self.output_label.text = 'Your guess is too small ❌'
                    self.coin_count -= 1
                else:
                    self.output_label.text = 'Your guess is too big ❌'
                    self.coin_count -= 1  # Decrease coin count for incorrect guess

                self.input_field.text = ''
                self.coin_count_label.text = f'Coins: {self.coin_count}'  # Update coin count label
            else:
                self.output_label.text = 'Please guess a number between 1 and 10.'
        except ValueError:
            self.output_label.text = 'Please enter a valid number.'

if __name__ == '__main__':
    LuckyGuessApp().run()
