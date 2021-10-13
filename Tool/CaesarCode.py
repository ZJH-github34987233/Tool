import re
import time

import Debug.log


class Caesar:  # 凯撒密码
    def __init__(self, Windows):
        self.WindowsID = Windows

    def encrypt(self, Original, PassWordSuppout=None):
        try:
            FirstTime = time.time()
            PassWord = ''
            Debug.log.Log(self.WindowsID).Log('[模块][CaesarCode][encrypt] 开始移位')
            for P in Original:
                if not re.match(r'[a-zA-Z]', P):
                    PassWord = PassWord + P
                    continue
                if Original == ' ':
                    PassWord = PassWord + P
                    Debug.log.Log(self.WindowsID).Log(f'[模块][CaesarCode][encrypt] {P}的密文为{P}')
                elif P == 'x' or P == 'y' or P == 'z' or P == 'X' or P == 'Y' or P == 'Z':
                    Pass = chr(ord(P) - 23)
                    PassWord = PassWord + Pass
                    Len = Original.find(P)
                    Debug.log.Log(self.WindowsID).Log(f'[模块][CaesarCode][encrypt] {P}的密文为{Pass}')
                elif P == '?':
                    Pass = P
                    PassWord = PassWord + Pass
                    Len = Original.find(P)
                    Debug.log.Log(self.WindowsID).Log(f'[模块][CaesarCode][encrypt] {P}的密文为{Pass}')
                else:
                    Pass = chr(ord(P) + 3)
                    PassWord = PassWord + Pass
                    Len = Original.find(P)
                    Debug.log.Log(self.WindowsID).Log(f'[模块][CaesarCode][encrypt] {P}的密文为{Pass}')
        except:
            Debug.log.Log(self.WindowsID).Error('[模块][CaesarCode][encrypt]')
        else:
            FinishTime = time.time()
            Time = str(FinishTime - FirstTime)
            Debug.log.Log(self.WindowsID).Log(
                '[模块][CaesarCode][encrypt] 已返回结果,用时：' + Time + '\n')  # 日志输出
            return PassWord

    def decrypt(self, PassWord, PassWordSuppout=None):
        try:
            FirstTime = time.time()
            Original = ''
            Debug.log.Log(self.WindowsID).Log('[模块][CaesarCode][decrypt] 开始移位')
            for O in PassWord:
                if not re.match(r'[a-zA-Z]', O):
                    Original = Original + O
                    continue
                if Original == ' ':
                    Original = Original + O
                    Len = PassWord.find(O)
                    Debug.log.Log(self.WindowsID).Log(f'[模块][CaesarCode][encrypt] {O}的明文为{O}')
                elif O == 'a' or O == 'b' or O == 'c' or O == 'A' or O == 'B' or O == 'C':
                    Orig = chr(ord(O) + 23)
                    Original = Original + Orig
                    Len = PassWord.find(O)
                    Debug.log.Log(self.WindowsID).Log(f'[模块][CaesarCode][encrypt] {O}的明文为{Orig}')
                else:
                    Orig = chr(ord(O) - 3)
                    Original = Original + Orig
                    Len = PassWord.find(O)
                    Debug.log.Log(self.WindowsID).Log(f'[模块][CaesarCode][encrypt] {O}的明文为{Orig}')
        except:
            Debug.log.Log(self.WindowsID).Error('[模块][CaesarCode][decrypt]')
        else:
            FinishTime = time.time()
            Time = str(FinishTime - FirstTime)
            Debug.log.Log(self.WindowsID).Log(
                '[模块][CaesarCode][decrypt] 已返回结果,用时：' + Time + '\n')  # 日志输出
            return Original
