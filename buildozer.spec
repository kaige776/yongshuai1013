[app]
title = YourAppName
package.name = yourappname
package.domain = org.test

# 指定使用 Python 3
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy  # 根据你的需求添加依赖库（如requests、numpy等）

# 支持的架构（根据需要修改，建议加入 arm64-v8a 以支持现代设备）
android.archs = armeabi-v7a, arm64-v8a

# 自动接受 Android SDK 许可协议
android.accept_sdk_license = True

# Android API 级别
android.api = 33
android.minapi = 21
