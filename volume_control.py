import numpy as np
from pycaw.pycaw import AudioUtilities

devices = AudioUtilities.GetSpeakers()

volume = devices.EndpointVolume

volMin, volMax = volume.GetVolumeRange()[:2]

def setVolume(length):
    if length is None:
        return

    length = max(15, min(140, length))

    vol = np.interp(length, [15, 140], [volMin, volMax])
    volume.SetMasterVolumeLevel(vol, None)


def mute():
    volume.SetMute(1, None)


def unmute():
    volume.SetMute(0, None)