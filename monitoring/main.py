from system_monitor import SystemMonitor


def main():
    monitoring_duration = int(input("Set the monitoring duration in minutes: "))
    monitoring_interval = int(input("Set the monitoring interval in minutes: "))

    monitor = SystemMonitor(monitoring_duration, monitoring_interval)
    monitor.start()


if __name__ == "__main__":
    main()
