[app]
title = Muse_2
package.name = muse2
package.domain = org.fastprojects
source.dir = .
source.include_exts = py,kv,json,txt,png,jpg,jpeg
version = 1.0.0
requirements = python3==3.14.0,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 35
android.minapi = 24
android.archs = arm64-v8a, armeabi-v7a

# Keep the Android native API at 24 or higher. Python 3.14 uses preadv/pwritev,
# which are unavailable when compiling against Android API 23.
p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 1
