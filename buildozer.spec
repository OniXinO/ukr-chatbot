[app]  
title = Український ЧатБот  # Назва програми  
package.name = ukrchatbot  # Унікальний ідентифікатор (наприклад: org.ukr.chatbot)  
package.domain = org.ukr  # Домен  
source.dir = .  # Папка з кодом (якщо файли в корені — ставимо крапку)  
version = 1.0  # Версія  
requirements = python3, kivy, cython==0.29.36  # Залежності  

# Додатково:  
orientation = portrait    
log_level = 2  # Рівень логування (2 — детальний)  
android.permissions = INTERNET  # Дозволи  

[buildozer]  
log_level = 2  
