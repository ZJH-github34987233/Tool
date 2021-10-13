import time

import Debug.log


class Vigenere:
    def __init__(self, Window):
        self.Windows = Window
        self.letter = {}
        # 生成密码表
        for a in range(0, 26):
            Letter = ''
            for i in range(0, 26):
                Show = chr(ord(chr(ord('A') + a + i)))  # 转化
                if not ord('A') <= ord(Show) <= ord('Z'):  # 当转化后的字符不是字母时的处理
                    Show = chr(ord(Show) - 26)  # 切换为正常字母
                Letter = Letter + Show  # 合并
            self.letter[Letter[0]] = Letter  # 储存

    def encrypt(self, Original, Key):
        try:
            FirstTime = time.time()
            n = 0
            PassWord = ''
            for i in Original:
                if ord('A') <= ord(i.upper()) <= ord('Z'):
                    if not n + 1 > len(Key) - 1:  # 确认密钥索引
                        n += 1
                    else:
                        n = 0
                    K = self.letter[Key[n - 1].upper()][ord(i.upper()) - 65]  # 确认密文
                    PassWord += K
                else:
                    K = i
                    PassWord += K
                Debug.log.Log(self.Windows).Log(f'[模块][Vigenere][encrypt] 已将{i}加密为{K}')
            FinishTime = time.time()
            Time = str(FinishTime - FirstTime)
            Debug.log.Log(self.Windows).Log(f'[模块][Vigenere][encrypt] 已返回结果,用时：' + Time + '\n')
            return PassWord[0].upper() + PassWord[1:].lower()
        except:
            Debug.log.Log(self.Windows).Error('[模块][CaesarCode][encrypt]')

    def decrypt(self, PassWord, Key):
        try:
            FirstTime = time.time()
            n = 0
            Original = ''
            O = ''
            for i in PassWord:
                if ord('A') <= ord(i.upper()) <= ord('Z'):
                    if not n + 1 > len(Key) - 1:  # 确认密钥索引
                        n += 1
                    else:
                        n = 0
                    K = chr(65 + self.letter[Key[n - 1].upper()].find(i.upper()))
                    O += K  # 确认明文
                else:
                    K = i
                    O += K  # 不是字母处理
                Debug.log.Log(self.Windows).Log(f'[模块][Vigenere][decrypt] 已将{i}加密为{K}')
            FinishTime = time.time()
            Time = str(FinishTime - FirstTime)
            Debug.log.Log(self.Windows).Log(f'[模块][Vigenere][decrypt] 已返回结果,用时：' + Time + '\n')
            return O[0].upper() + O[1:].lower()
        except:
            Debug.log.Log(self.Windows).Error('[模块][CaesarCode][encrypt]')

# PassWord = Vigenere().encrypt('Helloworld', 'abc')
# Original = Vigenere().decrypt(PassWord, 'abc')
# print(PassWord)
# print(Original)
