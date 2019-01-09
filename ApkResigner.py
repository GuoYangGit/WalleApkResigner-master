# -*- coding:utf-8 -*-
"""
@author: guoyang
@contact: guoyang_add@163.com
@file: config.py
@time: 2018/12/4 4:00 PM
@desc:
"""

import os
import sys
import config
import platform
import shutil


# 获取脚本文件的当前路径
def curFileDir():
    # 获取脚本路径
    path = sys.path[0]
    # 判断为脚本文件还是py2exe编译后的文件，
    # 如果是脚本文件，则返回的是脚本的目录，
    # 如果是编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


# 判断当前系统
def isWindows():
    sysStem = platform.system()
    if "Windows" in sysStem:
        return 1
    else:
        return 0


# 兼容不同系统的路径分隔符
def getBackslash():
    if isWindows() == 1:
        return "\\"
    else:
        return "/"


# 清空临时资源
def cleanTempResource():
    try:
        os.remove(zipAlignedApkPath)
        os.remove(signedApkPath)
        if config.jiagu360:
            os.remove(protectedSourceApkPath)
    except Exception:
        raise FileNotFoundError()


# 清空渠道信息
def cleanChannelsFiles():
    try:
        shutil.rmtree(channelsOutputFilePath)
    except Exception:
        raise FileNotFoundError()


# 创建Channels输出文件夹
def createChannelsDir():
    try:
        os.makedirs(channelsOutputFilePath)
    except Exception:
        raise FileNotFoundError()


# 写入渠道
def writeChannel():
    channel = config.channel
    with open(channelFilePath, "w") as f:
        for key in channel:
            f.write(key + "\n")


# 进行加固
def jiagu():
    print("开启360加固")
    # 获取360加固jar
    os.chdir(jiaguPath)
    jiaguLoginShell = "java -jar jiagu.jar -login " + config.jiaguUser + " " + config.jiaguPassWord
    os.system(jiaguLoginShell)
    jiaguShell = "java -jar jiagu.jar -jiagu " + protectedSourceApkPath + " " + jiaguApkPath
    os.system(jiaguShell)


# 改变apk名字
def changeApkName():
    channel = config.channel
    apkPath = channelsOutputFilePath + getBackslash()
    for key in channel:
        for file in os.listdir(apkPath):
            if apkName + key + ".apk" == file:
                os.rename(apkPath + file, apkPath + channel[key] + ".apk")


if __name__ == '__main__':
    # 当前脚本文件所在目录
    parentPath = curFileDir() + getBackslash()

    # config
    # 获取lib的目录
    libPath = parentPath + "lib" + getBackslash()
    # 获取BuildTool
    buildToolsPath = config.sdkBuildToolPath + getBackslash()
    # 获取checkAndroidV2Signature
    checkAndroidV2SignaturePath = libPath + "CheckAndroidV2Signature.jar"
    # 获取walleChannelWritter
    walleChannelWritterPath = libPath + "walle-cli-all.jar"
    keystorePath = config.keystorePath
    keyAlias = config.keyAlias
    keystorePassword = config.keystorePassword
    keyPassword = config.keyPassword
    channelsOutputFilePath = parentPath + "channels"
    channelFilePath = parentPath + "channel"
    protectedSourceApkPath = parentPath + config.protectedSourceApkName

    # 清空Channels输出文件夹
    cleanChannelsFiles()

    # 创建Channels输出文件夹
    createChannelsDir()

    # 进行channel渠道写入
    writeChannel()

    jiaguPath = parentPath + "jiagu" + getBackslash()
    jiaguApkPath = jiaguPath + "apk" + getBackslash()
    apkName = config.protectedSourceApkName[0:-4] + "_aligned_signed_"

    # 进行360加固
    if config.jiagu360:
        jiagu()
        protectedSourceApkPath = jiaguApkPath + os.listdir(jiaguApkPath)[0]
        apkName = os.listdir(jiaguApkPath)[0][0:-4] + "_aligned_signed_"

    zipAlignedApkPath = protectedSourceApkPath[0: -4] + "_aligned.apk"
    signedApkPath = zipAlignedApkPath[0: -4] + "_signed.apk"

    # 对齐
    print("开启v4对齐")
    zipAlignShell = buildToolsPath + "zipalign -v 4 " + protectedSourceApkPath + " " + zipAlignedApkPath
    os.system(zipAlignShell)
    print(zipAlignShell)

    # 签名
    print("开启签名")
    signShell = buildToolsPath + "apksigner sign --ks " + keystorePath + " --ks-key-alias " + keyAlias + " --ks-pass pass:" + keystorePassword + " --key-pass pass:" + keyPassword + " --out " + signedApkPath + " " + zipAlignedApkPath
    os.system(signShell)
    print(signShell)

    # 检查V2签名是否正确
    print("检查V2签名是否正确")
    checkV2Shell = "java -jar " + checkAndroidV2SignaturePath + " " + signedApkPath
    os.system(checkV2Shell)
    print(checkV2Shell)

    # 写入渠道
    print("开启写入渠道")
    writeChannelShell = "java -jar " + walleChannelWritterPath + " batch -f " + channelFilePath + " " + signedApkPath + " " + channelsOutputFilePath
    os.system(writeChannelShell)
    print(writeChannelShell)

    print("开始修改apk名称")
    changeApkName()

    print("清空临时资源")
    cleanTempResource()

    print("\n**** =============================TASK FINISHED=================================== ****\n")
    print("\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   Please check channels in the path   ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n")
    print("\n" + channelsOutputFilePath + "\n")
    print("\n**** =============================TASK FINISHED=================================== ****\n")
