import tkinter as tk
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

# Get volume control interface
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

def set_volume_from_entry(entry_widget, led_widget, other_led_widget):
    try:
        val = float(entry_widget.get()) / 100
        if 0 <= val <= 1:
            volume.SetMasterVolumeLevelScalar(val, None)
            led_widget.itemconfig("led", fill="#00FF00")
            other_led_widget.itemconfig("led", fill="gray")
        else:
            raise ValueError
    except ValueError:
        print("Invalid input: Enter a number between 0 and 100")

# GUI setup
root = tk.Tk()
root.title("Custom Volume Control")
root.geometry("330x150")
root.resizable(False, False)
root.iconbitmap(r"C:\Software\Python\volume_adjuster\basic_black_audio.ico")

# General padding frame to center contents
outer_frame = tk.Frame(root)
outer_frame.pack(expand=True)

# LOW VOLUME row
frame_low = tk.Frame(outer_frame)
frame_low.pack(pady=15)

led_low = tk.Canvas(frame_low, width=20, height=20, highlightthickness=0)
led_low.create_oval(2, 2, 18, 18, fill="gray", tags="led")
led_low.pack(side="left", padx=5)

btn_low = tk.Button(frame_low, text="Set Low Volume", width=18,
                    command=lambda: set_volume_from_entry(entry_low, led_low, led_high))
btn_low.pack(side="left", padx=5)

entry_low = tk.Entry(frame_low, width=5, justify="center")
entry_low.insert(0, "45")
entry_low.pack(side="left", padx=5)

# HIGH VOLUME row
frame_high = tk.Frame(outer_frame)
frame_high.pack(pady=10)

led_high = tk.Canvas(frame_high, width=20, height=20, highlightthickness=0)
led_high.create_oval(2, 2, 18, 18, fill="gray", tags="led")
led_high.pack(side="left", padx=5)

btn_high = tk.Button(frame_high, text="Set High Volume", width=18,
                     command=lambda: set_volume_from_entry(entry_high, led_high, led_low))
btn_high.pack(side="left", padx=5)

entry_high = tk.Entry(frame_high, width=5, justify="center")
entry_high.insert(0, "75")
entry_high.pack(side="left", padx=5)

root.mainloop()
