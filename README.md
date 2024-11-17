# School Timer Script

This Python script reads a configuration file with defined time ranges and executes a command if the current time falls within one of those ranges. It also allows optional time offsets (in minutes and seconds) to adjust the end time of the countdown.

## Features
- Automatically reads configuration files from the `Config` folder.
- Supports multiple configuration files, letting the user select one if multiple are present.
- Detects the current time range and executes a command conditionally.
- Handles errors in file reading and command execution gracefully.

## Configuration File Example (`Config/config.txt`)
```text
08:00-12:00 5 30
```

In this example:
- `08:00-12:00` specifies the time range during which the script checks for command execution.
- `5` is the optional time offset in **minutes** added to the end of the time range.
- `30` is the optional time offset in **seconds** added to the end of the time range.

## Requirements
- Python 3.x
- [tclock](https://lib.rs/crates/clock-tui) (A utility used for displaying a countdown timer)

## How to Use
1. Ensure you have at least one configuration file in the `Config` folder. The configuration file should specify time ranges and optional time offsets.
2. Run the script with:
   ```bash
   python main.py

3. If there is only one configuration file, it will be used automatically. If there are multiple files, you will be prompted to select one.
4. The script will check the current time against the time ranges specified in the configuration file. If the current time falls within a range, the command using tclock will be executed with the specified countdown.

## Example Output
   ```text
Using configuration file: config.txt
Command executed: tclock -c '#FFC0CB' countdown --time 12:05:30
```

In this example :

The configuration file specifies a time range of `08:00-12:00` with an optional offset of 5 minutes and 30 seconds.
If the current time is within this range, the script adds the offset and runs the countdown command until `12:05:30`.

## Error Handling
- If no configuration files are found in the Config folder, the script will exit with an error message: No configuration files found.
- If a line in the configuration file is invalid (e.g., incorrect format), the script skips the line and displays an error message without stopping execution.
- If the command fails to execute, an error message is shown with details of the failure.

## License
This project is open-source and licensed under the MIT License. You are free to use, copy, modify, merge, publish, distribute, sublicense, and sell copies of the software, as long as the original license notice is included in all copies or substantial portions of the software.

For more details, see the [LICENSE](./LICENSE) file.
