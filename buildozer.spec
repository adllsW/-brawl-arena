[app]

# (str) Title of your application
title = Brawl Arena

# (str) Package name
package.name = brawlarena

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,ttf,otf,kv,json,wav,ogg,mp3

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Включены только стабильные зависимости и базовый hostpython3
requirements = python3,kivy==2.3.0,hostpython3

# (str) Supported orientation
orientation = landscape

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (list) Permissions (раскомментируй, если нужен интернет)
# android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version
android.sdk = 33

# (str) Android NDK version
android.ndk = 25b

# (bool) Skip trying to update the Android sdk
android.skip_update = False

# (bool) Accept all SDK licenses automatically
android.accept_sdk_license = True

# (str) The Android arch to build for
# Оставлена только arm64-v8a для быстрой и стабильной сборки
android.archs = arm64-v8a

# (bool) Enable Android logcat output
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
