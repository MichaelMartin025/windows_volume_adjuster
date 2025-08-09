from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL


# Get default audio device
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

# Get volume control interface
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Set volume level (0.0 = min, 1.0 = max)
volume.SetMasterVolumeLevelScalar(0.45, None) # Sets volume to 50%
