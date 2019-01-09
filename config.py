# -*- coding:utf-8 -*-
"""
@author: guoyang
@contact: guoyang_add@163.com
@file: config.py
@time: 2018/12/4 4:00 PM
@desc:
"""
__author__ = 'guoyang'
# keystore信息
# Windows 下路径分割线请注意使用\\转义
keystorePath = ""
keyAlias = ""
keystorePassword = ""
keyPassword = ""

jiaguUser = ""
jiaguPassWord = ""

# 是否需要360加固
jiagu360 = True

channel = {
    "hd_1": "app_h1_guanwang",
    "hd_2": "app_h2_xiaomi",
    "hd_3": "app_h3_ali",
    "hd_4": "app_h4_yingyongbao",
    "hd_5": "app_h5_360",
    "hd_6": "app_h6_meizu",
    "hd_7": "app_h7_oppo",
    "hd_8": "app_h8_lianxiang",
    "hd_9": "app_h9_sougou",
    "hd_10": "app_h10_anzhi",
    "hd_11": "app_h11_yingyonghui",
    "hd_12": "app_h12_huawei",
    "hd_13": "app_h13_baidu",
    "hd_14": "app_h14_vivo",
    "hd_15": "app_h15_liqu",
    "hd_16": "app_h16_mumayi"
}

# 加固后的源文件名（未重签名）
protectedSourceApkName = "app.apk"
# Android SDK buidtools path , please use above 25.0+
sdkBuildToolPath = "/Users/guoyang/Library/Android/sdk/build-tools/26.0.2"
