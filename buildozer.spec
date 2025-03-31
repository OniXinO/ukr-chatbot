[app]  
title = Український ЧатБот  
package.name = ukrchatbot  
package.domain = org.ukr  
source.dir = .  
version = 1.0  
requirements = python3, kivy, cython==0.29.36  
android.sdk_path = ./android-sdk  # Відповідає шляху в workflow
android.ndk_path = ./android-sdk/ndk/26.2.11394342  # Автоматично встановлюється actions/setup-android@v2  
android.permissions = INTERNET  
orientation = portrait
p4a.branch = 2023.09.16
