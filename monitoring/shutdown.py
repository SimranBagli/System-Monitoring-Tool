import subprocess
import sys


class ShutdownSystem:

    def confirm_shutdown(self):
        stop_script = input("Do you want to stop the script? (yes/no): ")
        if stop_script.lower() == 'yes':
            confirm = input(
                """
                Stopping the script will
                initiate system shutdown.
                Do you want to proceed? (yes/no):
                """
                )
            if confirm.lower() == 'yes':
                self.shutdown_system()
            return True
        return True

    def shutdown_system(self):
        # Perform the necessary steps to initiate system shutdown
        if sys.platform.startswith('linux'):
            subprocess.call(['sudo', 'shutdown', '-P', 'now'])
