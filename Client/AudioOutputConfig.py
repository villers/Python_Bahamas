from PyQt5 import QtMultimedia


class AudioOutputConfig():
    def __init__(self):
        self.CurrentAudioOutput = self.GetDefaultAudioOutput()

    def GetDefaultAudioOutput(self):
        return QtMultimedia.QAudioDeviceInfo.defaultOutputDevice()

    def GetAudioOutputList(self):
        return QtMultimedia.QAudioDeviceInfo.availableDevices(QtMultimedia.QAudio.AudioOutput)

    def GetAudioOutputListName(self):
        return map(lambda x : x.deviceName(), self.GetAudioOutputList())

    def GetAudioOutputCurrent(self):
        return self.CurrentAudioOutput
