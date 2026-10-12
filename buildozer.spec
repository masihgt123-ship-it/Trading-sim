[app]
title = Dog Runner
package.name = dogrunner
package.domain = org.masihgt

source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf,ogg,mp3,wav

version = 0.1

requirements = python3,pygame

orientation = landscape
fullscreen = 1

android.archs = arm64-v8a
android.api = 33
android.minapi = 24
android.accept_sdk_license = True
android.permissions = INTERNET,VIBRATE

[buildozer]
log_level = 2
warn_on_root = 0
