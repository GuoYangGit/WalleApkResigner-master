# ProtectedApkResignerForWalle
一步解决应用加固导致[Walle](https://github.com/Meituan-Dianping/walle)渠道信息失效的自动化脚本，自动生成渠道包

----------
# 用法：

- 按照config.py文件中的注释改成自己项目配置
- 将已经加固好的包【未签名的包，请不要使用加固客户端签名工具】放到脚本工具根目录下，即app-release.encrypted.apk
- 各种渠道的定义是在channel这个文件中，请根据项目情况修改
- 运行命令 `python ApkResigner.py`,即可自动生成所有渠道包。
----------
