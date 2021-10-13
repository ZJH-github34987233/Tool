import time

import Debug.log


class Morse:  # 摩斯电码
    def __init__(self, Windows):
        self.Windows = Windows
        self.MorseList = {
            ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
            "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
            "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
            "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",

            "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
            ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

            ".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?",
            "-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
            "..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$",
            ".--.-.": "@", ".-.-.": "+",

            ".-...": "AS"
        }  # 摩斯电码表
        self.Morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                      'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                      'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
                      'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',

                      '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                      '6': '-....', '7': '--...', '8': '---..', '9': '----.',

                      '.': '.-.-.-', ':': '---...', ',': '--..--', ';': '-.-.-.', '?': '..--..', '=': '-...-',
                      "'": '.----.', '/': '-..-.', '!': '-.-.--', '-': '-....-', '_': '..--.-', '"': '.-..-.',
                      '(': '-.--.', ')': '-.--.-', '$': '...-..-', '@': '.--.-.', '+': '.-.-.',
                      }
        Debug.log.Log(self.Windows).Log('[模块][Morse][__init__] 初始化成功')

    def plaintext(self, string, sign):  # 明文转化摩斯电码
        FirstTime = time.time()
        A, B = '', ''
        for code in string:
            A = str(self.Morse.get(code))
            if A == 'None':
                A = code
            Debug.log.Log(self.Windows).Log(
                '[模块][Morse][plaintext] 获取到{}对应摩斯电码为{}'.format(code, A))
            B = B + A + sign  # 转化为摩斯电码，合并
            Debug.log.Log(self.Windows).Log('[模块][Morse][plaintext] 已将先前获取到的摩斯电码与现摩斯密码合并')
        FinishTime = time.time()
        Time = str(FinishTime - FirstTime)
        Debug.log.Log(self.Windows).Log('[模块][Morse][plaintext] 已返回结果,用时：' + Time + '\n')
        return B

    def morse(self, string, sign):  # 摩斯密码转化为明文
        FirstTime = time.time()
        A, B = '', ''
        # 分割，字符串string，分割标识符sign
        lists = string.split(sign)
        Debug.log.Log(self.Windows).Log('[模块][Morse][morse] 已将摩斯电码分割为：' + str(lists))
        for code in lists:  # 转化为明文
            A = str(self.MorseList.get(code))
            if A == 'None':
                A = code
            Debug.log.Log(self.Windows).Log('[模块][Morse][morse] 获取到{}对应明文为{}'.format(code, A))
            B = B + A  # 合并
            Debug.log.Log(self.Windows).Log('[模块][Morse][morse] 已将先前获取到的明文与现明文合并')
        FinishTime = time.time()
        Time = str(FinishTime - FirstTime)
        Debug.log.Log(self.Windows).Log('[模块][Morse][morse] 已返回结果,用时：' + Time + '\n')
        return B
