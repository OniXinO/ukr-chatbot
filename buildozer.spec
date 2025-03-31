[app]  
title = Test App  
package.name = testapp  
package.domain = org.test  
source.dir = .  
source.include_exts = py,png,jpg,kv,atlas
source.main.file = main.py
version = 1.0  
# Remove specific kivy version constraint to let buildozer handle it
requirements = python3,kivy,cython==0.29.36
p4a.branch = v2023.09.16
p4a.bootstrap = sdl2
android.api = 33
android.minapi = 21
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.2.9519653 
android.permissions = INTERNET  
android.architectures = armeabi-v7a
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1
