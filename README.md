[Volume_toggle_README.md](https://github.com/user-attachments/files/21726484/Volume_toggle_README.md)
# Windows 11 Quick Volume Toggle

A simple Python utility for quickly switching between two preset audio output levels in Windows 11 — perfect for movie watching when dialog is quiet but action scenes are loud.  
Instead of fiddling with the system volume slider, press a key or run the script to instantly toggle between your chosen **low** and **high** volume levels.

## Features
- **Two preset levels** — define your own "low" and "high" master volume percentages.
- **Instant toggle** — switch between levels without opening the Windows sound menu.
- **Saves your preferences** — remembers your chosen levels between runs.
- **Works system-wide** — affects the main Windows audio output, not just one app.

## Requirements
- Windows 11 (may also work on Windows 10)
- Python 3.8+
- [pycaw](https://github.com/AndreMiras/pycaw) (Python Core Audio Windows bindings)

Install dependencies:
```bash
pip install pycaw comtypes
```

## Usage
1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/YourUsername/quick-volume-toggle.git
   cd quick-volume-toggle
   ```
2. **Run the script**:
   ```bash
   python volume_toggle.py
   ```
3. **Follow prompts** to set your preferred "low" and "high" volume levels.
4. Press the toggle key or re-run the script to switch between levels.

## Example
If you set:
- High volume: `60%`
- Low volume: `25%`

Running the script will flip between these two instantly — no more hunting for the Windows volume slider.

## Notes
- Works best when run in the background or bound to a global hotkey (optional extra feature).
- This script uses `pycaw` to directly interface with Windows Core Audio, so no extra apps or admin rights are needed.

## License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
