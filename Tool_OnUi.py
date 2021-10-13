import sys
import time

from PyQt5.QtWidgets import QApplication, QMainWindow

import Debug.Vision
import Debug.log
import Tool.CaesarCode
import Tool.Combination
import Tool.FencePassword
import Tool.Morse
import Tool.PassWord
import Tool.RomanNum
import Tool.Vigenere
import ToolUi

try:
    def remove(rempath):
        import os
        for path, dirnames, filenames in os.walk(rempath):
            for f in filenames:
                os.remove(os.path.join(path, f))
            os.rmdir(rempath)


    def getZipDir(dirpath, outFullName):
        import os
        import zipfile
        zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(dirpath):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
            fpath = path.replace(dirpath, '')
            for filename in filenames:
                zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
        zip.close()
        remove(dirpath)


    def NumToRoman():  # 转化为罗马数字
        Debug.log.Log(WindowsID).Log('[Roman][NumToRoman] 点击阿拉伯数字转为罗马数字按钮"←"')  # 日志输出
        try:
            Num = Ui.UiRomanNum.text()
            Debug.log.Log(WindowsID).Log(f'[Roman][NumToRoman] 获取到阿拉伯数字：{Num}')  # 日志输出
            Roman = Tool.RomanNum.Solution(WindowsID).intToRoman(int(Num))
            Ui.UiRomanRomanNum.setText(Roman)  # 结果
            Debug.log.Log(WindowsID).Log(f'[Roman][NumToRoman] 已输出为罗马数字：{Roman}\n')  # 日志输出
        except ValueError:
            Debug.log.Log(WindowsID).Error('[Roman][NumToRoman]')
        except:
            Debug.log.Log(WindowsID).Error('[Roman][NumToRoman]')  # 日志输出


    def RomanToNum():  # 转化为阿拉伯数字
        Debug.log.Log(WindowsID).Log('[Roman][RomanToNum] 点击阿拉伯数字转为罗马数字按钮"→"')  # 日志输出
        try:
            Roman = Ui.UiRomanRomanNum.text()
            Debug.log.Log(WindowsID).Log(f'[Roman][RomanToNum] 获取到罗马数字：{Roman}')  # 日志输出
            Num = str(Tool.RomanNum.Solution(WindowsID).RomanToInt(Roman))
            Ui.UiRomanNum.setText(Num)
            Debug.log.Log(WindowsID).Log(f'[Roman][RomanToNum] 已输出为阿拉伯数字：{Num}\n')  # 日志输出
        except:
            Debug.log.Log(WindowsID).Error('[Roman][RomanToNum]')  # 日志输出


    def MorseToPlain():  # 摩斯电码转明文
        Debug.log.Log(WindowsID).Log('[Roman][MorseToPlain] 点击摩斯电码转为明文按钮"→"')  # 日志输出
        try:
            sign = ' '
            Debug.log.Log(WindowsID).Log('[Morse][MorseToPlain] 开始确定分隔符')  # 日志输出
            for S in Ui.UiMorsePassWord.text():
                if S == '-' or S == '.':
                    Debug.log.Log(WindowsID).Log(
                        '[Morse][MorseToPlain][Exception] 在当前字符中没有找到分隔符')  # 日志输出
                else:
                    sign = S
                    break
            Debug.log.Log(WindowsID).Log(f'[Morse][MorseToPlain] 开始确认摩斯电码,分隔符将为：{sign}')
            Finally = str(Tool.Morse.Morse(WindowsID).morse(Ui.UiMorsePassWord.text(), sign))
            Debug.log.Log(WindowsID).Log(
                f'[Morse][MorseToPlain] 确认明文为：{Finally}')  # 日志输出
        except:
            Debug.log.Log(WindowsID).Error('[Morse][MorseToPlain]')  # 日志输出
        else:
            Ui.UiMorseOriginal.setText(Finally)
            Debug.log.Log(WindowsID).Log(f'[Morse][MorseToPlain] 已输出为明文：{Finally}\n')  # 日志输出


    def PlainToMorse():  # 明文转摩斯电码
        Debug.log.Log(WindowsID).Log('[Roman][PlainToMorse] 点击明文转为摩斯电码按钮"←"')  # 日志输出
        try:
            sign = Ui.UiMorselineEdit.text()  # 获取分隔符
            Debug.log.Log(WindowsID).Log(f'[Morse][PlainToMorse] 获取到分隔符：{sign}')  # 日志输出
            if Ui.UiMorselineEdit.text() == '':
                sign = ' '
                Debug.log.Log(WindowsID).Log(
                    f'[Morse][PlainToMorse] 没有输入分隔符，已将分隔符设为：{sign}')  # 日志输出
            Original = Ui.UiMorseOriginal.text().upper()
            Debug.log.Log(WindowsID).Log(f'[Morse][PlainToMorse] 原文：{Original}')  # 日志输出
            Finally = str(Tool.Morse.Morse(WindowsID).plaintext(Original, sign))
        except:
            Ui.UiMorseOriginal.setText('Error')
            Debug.log.Log(WindowsID).Error('[Morse][PlainToMorse]')  # 日志输出
        else:
            Ui.UiMorsePassWord.setText(Finally)
            Debug.log.Log(WindowsID).Log(
                f'[Morse][PlainToMorse] 已输出为摩斯电码：{Finally}\n')  # 日志输出


    def CaesarEncrypt():  # 凯撒密码加密
        Debug.log.Log(WindowsID).Log('[Caesar][CaesarEncrypt] 点击凯撒密码加密按钮"→"')  # 日志输出
        try:
            Caesar = Tool.CaesarCode.Caesar(WindowsID).encrypt(Ui.UiCaesarOriginal.text())
        except:
            Debug.log.Log(WindowsID).Error('[Caesar][CaesarEncrypt]')  # 日志输出
        else:
            Ui.UiCaesarPassWord.setText(Caesar)
            Debug.log.Log(WindowsID).Log(
                f'[Caesar][CaesarEncrypt] 已成功输出为密文：{Caesar}\n')  # 日志输出


    def CaesarDecrypt():  # 凯撒密码解密
        Debug.log.Log(WindowsID).Log('[Caesar][CaesarDecrypt] 点击凯撒密码解密按钮"←"')  # 日志输出
        try:
            Original = Tool.CaesarCode.Caesar(WindowsID).decrypt(Ui.UiCaesarPassWord.text())
        except:
            Debug.log.Log(WindowsID).Error('[Caesar][CaesarDecrypt]')  # 日志输出
        else:
            Ui.UiCaesarOriginal.setText(Original)

            Debug.log.Log(WindowsID).Log(
                f'[Caesar][CaesarDecrypt] 已成功输出为明文：{Original}\n')  # 日志输出


    def FenceEncrypt():  # 栅栏密码加密
        Debug.log.Log(WindowsID).Log('[Fence][FenceEncrypt] 点击栅栏密码加密按钮"→"')  # 日志输出
        try:
            Key = Ui.UiFenceFenceKey.text()
            Fence = Tool.FencePassword.Fence(WindowsID).encrypt(Ui.UiFenceOriginal.text(), int(Key))
        except:
            Debug.log.Log(WindowsID).Error('[Fence][FenceEncrypt]')  # 日志输出
        else:
            Ui.UiFenceFencePassWord.setText(Fence)
            Debug.log.Log(WindowsID).Log(f'[Fence][FenceEncrypt] 已成功输出为密文：{Fence} ; 密钥为：{Key}')  # 日志输出


    def FenceDecrypt():  # 栅栏密码解密
        Debug.log.Log(WindowsID).Log('[Roman][FenceEncrypt] 点击栅栏密码解密按钮"←"')  # 日志输出
        try:
            Original = Tool.FencePassword.Fence(WindowsID).decrypt(Ui.UiFenceFencePassWord.text(),
                                                                   int(Ui.UiFenceFenceKey.text()))
        except:
            Debug.log.Log(WindowsID).Error('[Fence][FenceDecrypt]')  # 日志输出
        else:
            Ui.UiFenceOriginal.setText(Original)
            Debug.log.Log(WindowsID).Log(
                f'[Fence][FenceDecrypt] 已成功输出为原文：{Original}\n')  # 日志输出


    def ZhiInt():
        Debug.log.Log(WindowsID).Log('[ZhiInt] 点击判断是否是合数按钮')  # 日志输出
        try:
            if Ui.UiZhiShuNum.text() != '':
                if Tool.Combination.ZHiShu(int(Ui.UiZhiShuNum.text()), WindowsID):
                    Ui.UiZhiShuFinally.setText(
                        "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">是合数</span></p></body></html>")
                    Debug.log.Log(WindowsID).Log(
                        f'[ZhiInt] 已输出：{int(Ui.UiZhiShuNum.text())} 是合数\n')  # 日志输出
                else:
                    Ui.UiZhiShuFinally.setText(
                        f"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">不是合数</span></p></body></html>")
                    Debug.log.Log(WindowsID).Log(
                        f'[ZhiInt] 已输出：{int(Ui.UiZhiShuNum.text())} 不是合数\n')  # 日志输出
        except:
            Debug.log.Log(WindowsID).Error('[ZhiInt]')


    def PassEn():
        PassWord = Tool.PassWord.PassWord(WindowsID).encrypt(Ui.UiPassWordOriginal.text())
        Ui.UiPassWordPassWord.setText(PassWord)


    def PassDe():
        Original = Tool.PassWord.PassWord(WindowsID).decrypt(Ui.UiPassWordPassWord.text())
        Ui.UiPassWordOriginal.setText(Original)


    def VigenereEn():
        PassWord = Tool.Vigenere.Vigenere(WindowsID).encrypt(Ui.UiVigenereOriginal.text(), Ui.UiVigenereKey.text())
        Ui.UiVigenerePassWord.setText(PassWord)


    def VigenereDe():
        Original = Tool.Vigenere.Vigenere(WindowsID).decrypt(Ui.UiVigenerePassWord.text(), Ui.UiVigenereKey.text())
        Ui.UiVigenereOriginal.setText(Original)


    FirstTime = time.time()
    HumanVision = Debug.Vision.Vision().Human_vision()
    RangeVision = Debug.Vision.Vision().Python_vision()
    VisionLog = Debug.Vision.Vision().Vision_Log()
    # 版本说明
    print(f'Tools [版本：{HumanVision}]\n(c) ZJH 保留所有权利\n')
    Debug.Vision.Vision().Vision_Show()
    if __name__ == '__main__':
        Tools = QApplication(sys.argv)
        MainWindow = QMainWindow()
        Ui = ToolUi.Ui_Tool()
        Ui.setupUi(MainWindow)
        MainWindow.show()
        WindowsID = id(Tools)
        FinallyTime = time.time()
        Debug.log.Log(WindowsID).Window('Open', FinallyTime - FirstTime)
        Ui.NumToRoman.clicked.connect(NumToRoman)  # 阿拉伯数字到罗马数字
        Ui.RumanToNum.clicked.connect(RomanToNum)  # 罗马数字到阿拉伯数字
        Ui.plaintext.clicked.connect(MorseToPlain)  # 转化明文
        Ui.morse.clicked.connect(PlainToMorse)  # 转化摩斯电码
        Ui.encrypt.clicked.connect(CaesarEncrypt)  # 凯撒密码加密
        Ui.decrypt.clicked.connect(CaesarDecrypt)  # 凯撒密码解密
        Ui.Encrypt.clicked.connect(FenceEncrypt)  # 栅栏密码加密
        Ui.Decrypt.clicked.connect(FenceDecrypt)  # 栅栏密码解密
        Ui.UiZhiShuStart.clicked.connect(ZhiInt)  # 质数判断
        Ui.UiPassWordEn.clicked.connect(PassEn)  # 密码加密
        Ui.UiPassWordDe.clicked.connect(PassDe)  # 密码解密
        Ui.UiVigenereEncrypt.clicked.connect(VigenereEn)  # Vigenere 加密
        Ui.UiVigenereDecrypt.clicked.connect(VigenereDe)  # Vigenere 解密
        MainWindow.setWindowTitle(f'工具箱 - {WindowsID}')
        sys.exit(Tools.exec_())

except SystemExit:
    Debug.log.Log(WindowsID).Window('Exit')  # 日志输出
except:
    Debug.log.Log(WindowsID).Error('[All]')  # 日志输出
