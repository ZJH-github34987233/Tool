import random
import time

import Debug.log
from Tool import CaesarCode, FencePassword, Vigenere


class PassWord:
    def __init__(self, Window):
        self.Window = Window
        self.Key = {1: [CaesarCode.Caesar, None], 2: [FencePassword.Fence, 2],
                    3: [Vigenere.Vigenere, 'PassWordVigenere']}

    def encrypt(self, Original):
        try:
            FirstTime = time.time()
            n = 0
            O = Original
            # 确认需要的加密方法
            K = []
            while n <= len(self.Key) * 4:
                key = random.randint(1, len(self.Key))  # 加密密钥
                Debug.log.Log(self.Window).Log(
                    f'[模块][PassWord][encrypt] 已确认加密的方法为{str(self.Key[key][0])}')
                K.append(key)
                Original = self.Key[key][0](self.Window).encrypt(Original, self.Key[key][1])
                Debug.log.Log(self.Window).Log(
                    f'[模块][PassWord][encrypt] 已将{O}加密为{Original}')
                n += 1
            B = ''
            for i in K:
                B = str(B) + str(i)
            K.clear()
            # 若密文与原文一致的处理
            if Original == O:
                Debug.log.Log(self.Window).Log(
                    f'[模块][PassWord][encrypt] 密文与原文重复')
                key = 1
                n = 0
                while n <= 5:
                    K.append(key)
                    Original = self.Key[key][0](self.Window).encrypt(Original, self.Key[key][1])
                    Debug.log.Log(self.Window).Log(
                        f'[模块][PassWord][encrypt] 已将{O}加密为{Original}')
                    n += 1
                for i in K:
                    B = str(B) + str(i)  # 合并加密密钥
                Debug.log.Log(self.Window).Log(
                    f'[模块][PassWord][encrypt] 密钥为{B}')
            Original = str(B) + '/' + str(Original)
            Original = FencePassword.Fence(self.Window).encrypt(Original, 2)
            # 转化为 16 进制
            by = bytes(Original, 'UTF-8')
            Original = by.hex()
            FinishTime = time.time()
            Time = str(FinishTime - FirstTime)
            Debug.log.Log(self.Window).Log(
                f'[模块][PassWord][encrypt] 已返回结果,用时：{Time}')
            return Original
        except:
            Debug.log.Log(self.Window).Error('[模块][PassWord][encrypt]')

    def decrypt(self, PassWord):
        try:
            FirstTime = time.time()
            import binascii
            # 转化为普通文字
            PassWord = str(binascii.unhexlify(PassWord), encoding="utf-8")
            PassWord = FencePassword.Fence(self.Window).decrypt(str(PassWord), 2)
            Debug.log.Log(self.Window).Log(
                f'[模块][PassWord][decrypt] 已将密文解密为真正的密文，密文为：{PassWord}')
            PassWord = PassWord.split('/')
            Debug.log.Log(self.Window).Log(
                f'[模块][PassWord][decrypt] 已分隔')
            PassWord, Key = PassWord[1], PassWord[0]
            List = []
            for i in Key:
                List.append(i)  # 读取密钥
            while List != []:
                key = List.pop()
                PassWord = self.Key[int(key)][0](self.Window).decrypt(PassWord, self.Key[int(key)][1])
            Debug.log.Log(self.Window).Log(
                f'[模块][PassWord][decrypt] 明文为{PassWord}')
            FinishTime = time.time()
            Time = str(FinishTime - FirstTime)
            Debug.log.Log(self.Window).Log(
                f'[模块][PassWord][decrypt] 已返回结果,用时：{Time}')
            return str(PassWord)
        except:
            Debug.log.Log(self.Window).Error('[模块][PassWord][decrypt]')
