[app]  
title = Український ЧатБот  
package.name = ukrchatbot  
package.domain = org.ukr  
source.dir = .  
source.include_exts = py,png,jpg,kv,atlas
source.main.file = chatbot.py
version = 1.0  
requirements = python3, kivy, cython==0.29.36  
p4a.branch = 2023.09.16
android.api = 34
android.minapi = 21
android.sdk = 34
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.2.9519653 
android.permissions = INTERNET  
android.bootstrap = sdl2
android.architectures = arm64-v8a, armeabi-v7a
orientation = portrait
