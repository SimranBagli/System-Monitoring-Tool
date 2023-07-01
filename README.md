# System Monitoring Tool

The System Monitoring Tool is a Python script that allows you to monitor system activity, including active applications, memory usage, key presses, and captures screenshots at specified intervals. It provides insights into how the system is being utilized over a defined monitoring duration.

## Requirements

- Python 3.6 or above
- Dependencies listed in `requirements.txt`

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.

   ```shell
   cd system-monitoring-tool
   ```

3. Install the required dependencies using pip.

   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Open a terminal and navigate to the project directory.
2. Run the script using the following command:

   ```shell
   python main.py
   ```

3. Set the monitoring duration in minutes when prompted.
4. Set the monitoring interval in minutes when prompted.
5. The script will start monitoring the system, capturing data at the specified intervals.
6. To stop the script, enter 'yes' when prompted or press `Ctrl+C`.
7. If you choose to stop the script, a confirmation message will be displayed before initiating a system shutdown. Enter 'yes' to proceed with the shutdown or 'no' to continue monitoring.
8. The monitoring data will be saved to an Excel file named `monitoring_data_screen.xlsx` in the project directory.
