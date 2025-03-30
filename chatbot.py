import kivy  
from kivy.app import App  
from kivy.uix.button import Button  
from kivy.uix.boxlayout import BoxLayout  

class ChatApp(App):  
    def build(self):  
        layout = BoxLayout(orientation='vertical')  
        btn = Button(text='НАЖМИ МЕНЕ, ЩОБ ПОЧАТИ!', size_hint=(1, 0.2))  
        btn.bind(on_press=self.start_chat)  
        layout.add_widget(btn)  
        return layout  

    def start_chat(self, instance):  
        print("БОТ: Привіт! Я вмію говорити українською. Спробуй мене!")  

if __name__ == '__main__':  
    ChatApp().run()  
