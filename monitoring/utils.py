import subprocess


def get_active_window():
    try:
        active_window = subprocess.check_output(
            [
                'xdotool',
                'getwindowfocus',
                'getwindowname'
                ]).decode().strip()
    except subprocess.CalledProcessError:
        active_window = None
    return active_window
