import pyautogui
import time
def auto_click(x, y):
    pyautogui.click(x, y)
    time.sleep(1)
if __name__ == "__main__":

    while True:
        x, y = (2460, 307) #Delete Cookies
        auto_click(x, y)

        x, y = (2301, 515)  # Confirm
        auto_click(x, y)
        auto_click(x, y)

        x, y = (2309, 373)# Close Windows
        auto_click(x, y)

        time.sleep(2)
        x, y = (2434, 163)

        # Send button
        auto_click(x, y)

        time.sleep(2)
        auto_click(x, y)

        time.sleep(5)

