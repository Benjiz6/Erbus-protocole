import pip
pip install pywifi
import pywifi
def disable_ai_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    if iface.status() == pywifi.const.IFACE_CONNECTED:
        iface.disconnect()
        print("AI WiFi connection disabled.")
    else:
        print("AI WiFi already disabled.")

disable_ai_wifi()
import subprocess
def disable_ai_wifi():
    platforms = {
        'darwin': 'networksetup -setairportpower airport off',
        'linux': 'nmcli device wifi off',
        'win32': 'netsh wlan disconnect'
    }
    command = platforms.get(subprocess.os.name, None)
    if command:
        subprocess.run(command, shell=True)
        print("AI WiFi connection disabled.")
    else:
        print("Unsupported platform.")

disable_ai_wifi()