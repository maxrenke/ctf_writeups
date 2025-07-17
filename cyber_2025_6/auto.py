import time
import pyautogui
import string

# Wait for 10 seconds
time.sleep(10)

combinations = set()
chars = string.ascii_letters + string.digits + string.punctuation
for a in chars:
    for b in chars:
        combinations.add(a + b)

print(combinations)

for c in combinations:
    text = f'RESUME{{{c}}}'
    pyautogui.write(text)
    pyautogui.press('enter')
    time.sleep(0.2)