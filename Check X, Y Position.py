
from pynput.mouse import Listener

def click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y})")
        return (x, y)


if __name__ == "__main__":
    with Listener(on_click=click) as listener:
        listener.join()

