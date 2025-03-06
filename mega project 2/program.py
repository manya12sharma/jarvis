import pyautogui
import time
import pyperclip

# Step 1: Click on the Chrome icon at coordinates (1000,739)
pyautogui.click(950,738)
time.sleep(1)  # Wait for 1 second to ensure the click is registered

# Step 2: Drag the mouse from (741,123) to (1317,642) to select the text
pyautogui.moveTo(470,138)
pyautogui.dragTo(1317,642,duration=1.0,button='left')  # ✅ Fixed

# Step 3: Copy the selected text to clipboard
pyautogui.hotkey('ctrl', 'c')  # ✅ Fixed
time.sleep(1)  # Wait for 1 second to ensure the copy is registered

# Step 4: Retrieve the text from the clipboard
text = pyperclip.paste()

# Step 5: Print the copied text to verify
print(text)
