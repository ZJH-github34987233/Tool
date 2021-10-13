import json

from Control import Dialog


class Vision:
    def __init__(self):
        with open('Debug\Vision.json', 'r', encoding='utf-8') as V:
            self.VisionJson = json.load(V)

    def Human_vision(self):
        return self.VisionJson.get('type') + ' ' + self.VisionJson.get('vision')

    def Python_vision(self):
        return self.VisionJson.get('Range')

    def Vision_Log(self):
        return self.VisionJson.get('UpDataLog')

    def Vision_Show(self):
        if self.VisionJson.get('Show') != 'False':
            with open('Debug\Vision.json', 'w', encoding='utf8') as i:
                self.VisionJson['Show'] = 'False'
                json.dump(self.VisionJson, i)
            VisionLog = self.VisionJson.get('UpDataLog')

            try:
                Dialog.DiaLog('更新日志', VisionLog)
            except:
                pass
        else:
            return ''
