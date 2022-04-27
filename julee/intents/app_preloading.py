def app_preloading():
    # preinstalled apps on windows 10
    default_apps = {"terminal": "cmd", "command prompt": "cmd", "resource monitor": "perfmon",
                    "device manager": "devmgmt.msc", "disk management": "diskmgmt.msc", "task manager": "taskmgr",
                    "paint": "mspaint", "edge": "msedge", "vscode": "code", "calculator": "calc",
                    "notepad": "notepad", "keyboard": "osk", "camera": "microsoft.windows.camera:"}

    # apps that count as file explorer(Ctrl + W)
    explorer_apps = {"control panel": "control", "my folder": ".", "this pc": "explorer", "file explorer": "explorer",
                     "explorer": "explorer"}

    # apps not include in windows 10
    other_apps = {"illustrator": "illustrator", "telegram": "telegram", "photoshop": "Photoshop",
                  "vlcplayer": "VLC", "video player": "VLC", "chrome": "chrome", "firefox": "firefox",
                  "word": "winword", "excel": "excel", "powerpoint": "powerpnt", "power point": "powerpnt",
                  "designer": "Formdesigner"}

    # for app that has different open and close method
    special_apps = {"device manager": "mmc.exe", "disk management": "mmc.exe", "resource monitor": "mmc.exe",
                    "camera": "windowscamera.exe", "calculator": "calculator.exe"}
    return default_apps, explorer_apps, other_apps, special_apps
