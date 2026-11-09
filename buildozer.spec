[app]
title = Prospero PS5 Emulator
package.name = prosperops5
package.domain = org.prospero.engine
source.include_exts = py,mp4
source.dir = .
version = 5.0
requirements = python3
orientation = landscape
osx.python_version = 3
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 34
android.build_tools_version = 34.0.0
android.min_api = 24
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1

