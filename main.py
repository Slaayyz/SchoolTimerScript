import datetime
import subprocess
import os

# Directory for configuration files
config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Config")
config_files = [f for f in os.listdir(config_dir) if f.endswith(".txt")]

# Check if there are any configuration files
if not config_files:
    print("No configuration files found in the 'Config' folder.")
    exit(1)

# Choose the configuration file
if len(config_files) == 1:
    config_path = os.path.join(config_dir, config_files[0])
    print(f"Using configuration file: {config_files[0]}")
else:
    print("Select a configuration file:")
    for i, config_file in enumerate(config_files):
        print(f"{i + 1}. {config_file}")

    while True:
        try:
            choice = int(input(f"Enter the file number (1 to {len(config_files)}): "))
            if 1 <= choice <= len(config_files):
                config_path = os.path.join(config_dir, config_files[choice - 1])
                break
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

# Read the configuration file
try:
    with open(config_path, "r") as config_file:
        lines = config_file.readlines()
except Exception as e:
    print(f"Error reading the configuration file: {e}")
    exit(1)

current_time = datetime.datetime.now()
command_executed = False

# Parse the configuration lines
for line in lines:
    try:
        elements = line.strip().split(" ")
        time_range = elements[0]

        # Check for optional time offset
        if len(elements) == 3:
            offset_minutes = int(elements[1])
            offset_seconds = int(elements[2])
        else:
            offset_minutes = 0
            offset_seconds = 0

        start_time, end_time = time_range.split("-")
        start_time = datetime.datetime.strptime(start_time, "%H:%M").time()
        end_time = datetime.datetime.strptime(end_time, "%H:%M").time()

        # Check if the current time is within the time range
        if start_time <= current_time.time() <= end_time:
            try:
                end_time_datetime = datetime.datetime.combine(datetime.date.today(), end_time)
                new_end_time_datetime = end_time_datetime + datetime.timedelta(minutes=offset_minutes, seconds=offset_seconds)

                # Command to execute
                command = f"tclock -c '#FFC0CB' countdown --time {new_end_time_datetime.strftime('%H:%M:%S')}"
                subprocess.run(command, shell=True, check=True)
                print(f"Command executed: {command}")
                command_executed = True
            except subprocess.CalledProcessError as e:
                print(f"Error executing the command: {e}")
            break

    except (ValueError, IndexError) as e:
        print(f"Invalid configuration line: {line.strip()} - {e}")

# No command executed
if not command_executed:
    print("No command to execute for the current time.")
