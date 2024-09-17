# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

# The main game class, inheriting from Kivy's App


class IdleBankTycoonApp(App):
    def build(self):
        # Create the main layout
        self.main_layout = BoxLayout(orientation='vertical')

        # Initialize bank balance as an instance attribute
        self.balance = 0

        # Create a label to display bank balance
        self.balance_label = Label(
            text='Bank Balance: ${self.balance}', font_size='24sp')
        self.main_layout.add_widget(self.balance_label)

        # Create a button to simulate income generation
        self.earn_button = Button(text='Earn Money', size_hint=(1, 0.2))
        self.earn_button.bind(on_press=self.earn_money)
        self.main_layout.add_widget(self.earn_button)

        # Schedule the income generation every second
        Clock.schedule_interval(self.generate_idle_income, 1)

        return self.main_layout

    def earn_money(self, instance):
        # Placeholder method for earning money manually increase balance by $100 and update the label
        self.balance += 100  # Increase balance by $100
        self.update_balance_label()  # Update the balance label

    def generate_idle_income(self, dt):
        # Plaeholder method for generating idle income increase balance by $10 every second and update the label
        self.balance += 10
        self.update_balance_label()

    def update_balance_label(self):
        # Update the balance label text
        self.balance_label.text = f'Bank Balance: ${self.balance}'


# Run the app
if __name__ == '__main__':
    try:
        IdleBankTycoonApp().run()
    except Exception as e:
        print(f"An error occurred: {e}")
