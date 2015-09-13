from PyQt5 import QtMultimedia


class AudioInputConfig():
    def __init__(self):
        self.CurrentAudioInput = self.GetDefaultAudioInput()

    def GetDefaultAudioInput(self):
        return QtMultimedia.QAudioDeviceInfo.defaultInputDevice()

    def GetAudioInputList(self):
        return QtMultimedia.QAudioDeviceInfo.availableDevices(QtMultimedia.QAudio.AudioInput)

    def GetAudioInputListName(self):
        return map(lambda x : x.deviceName(), self.GetAudioInputList())

    def GetAudioInputCurrent(self):
        return self.CurrentAudioInput
