import time
import psutil
import subprocess
import pandas as pd
from pynput import keyboard
import pyautogui
from shutdown import ShutdownSystem


class SystemMonitor:
    def __init__(self, monitoring_duration, monitoring_interval):
        self.monitoring_duration = monitoring_duration
        self.monitoring_interval = monitoring_interval
        self.data = pd.DataFrame(
            columns=[
                'Timestamp',
                'Active App',
                'Memory Usage',
                'Key Presses',
                'Screenshot Path'
                ])
        self.key_press_count = 0
        self.keyboard_listener = None
        self.stop_flag = False

    def start(self):
        # Start the keyboard listener
        self.keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
        self.keyboard_listener.start()

        start_time = time.time()
        end_time = start_time + (self.monitoring_duration * 60)

        try:
            while time.time() < end_time:
                # Get the current timestamp
                timestamp = time.strftime(
                    '%Y-%m-%d %H:%M:%S', time.localtime())

                # Get the currently active app/window on Linux
                try:
                    active_window = subprocess.check_output(
                        [
                            'xdotool',
                            'getwindowfocus',
                            'getwindowname'
                            ]).decode().strip()
                except subprocess.CalledProcessError:
                    active_window = None

                # Get system memory usage
                memory_usage = psutil.virtual_memory()
                percent_memory = memory_usage.percent

                # Capture screenshot
                screenshot = pyautogui.screenshot()

                # Save the screenshot
                curr_time = time.strftime("%Y%m%d%H%M%S")
                screenshot_path = f'media/screenshot_{curr_time}_{active_window}.png'
                screenshot.save(screenshot_path)

                # Append the data to the DataFrame
                self.data = pd.concat([self.data, pd.DataFrame({
                    'Timestamp': timestamp,
                    'Active App': active_window,
                    'Memory Usage': percent_memory,
                    'Key Presses': self.key_press_count,
                    'Screenshot Path': screenshot_path
                }, index=[0])], ignore_index=True)

                # Reset the key press count for the next interval
                self.key_press_count = 0

                # Wait for the next monitoring interval
                time.sleep(self.monitoring_interval * 60)

        except KeyboardInterrupt:
            # Keyboard interruption occurred
            print("Keyboard interruption detected....")
            shutdown = ShutdownSystem()
            if shutdown.confirm_shutdown():
                print("Continue Working")
                self.continue_start()

        # Stop the keyboard listener
        self.keyboard_listener.stop()

        # Save the data to an Excel sheet
        output_file = 'execlfile/monitoring_data_screen.xlsx'  # Set file name
        self.data.to_excel(output_file, index=False)
        print(f"Monitoring completed. Data saved to {output_file}.")

    def on_key_press(self, key):
        self.key_press_count += 1

    def continue_start(self):
        self.start()
