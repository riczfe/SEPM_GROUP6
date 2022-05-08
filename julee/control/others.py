import win32gui, win32con


def fullscreen_mode():
    hwnd = win32gui.GetForegroundWindow()
    state = win32gui.GetWindowPlacement(hwnd)  # get the state of the active app
    if state[1] == win32con.SW_MAXIMIZE:
        win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
    elif state[1] == win32con.SW_SHOWNORMAL:
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    """
    elif state[1] == win32con.SW_MINIMIZE:
        return "MINIMIZED
    """