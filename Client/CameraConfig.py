from PyQt5 import QtMultimedia

class CameraConfig():
    def __init__(self):
        self.CameraCurrent = self.GetDefaultCamera()

    def GetDefaultCamera(self):
        return QtMultimedia.QCameraInfo.defaultCamera()

    def GetCameraList(self):
        return QtMultimedia.QCameraInfo.availableCameras()

    def GetCameralistName(self):
        return map(lambda x : x.deviceName(), self.GetCameraList())

    def GetCurrentCamera(self):
        return self.CameraCurrent


