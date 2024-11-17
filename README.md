# 📅 School Timer Script

This **Python script** reads configuration files with predefined time ranges and executes a command if the current time falls within one of those ranges. It also supports optional time offsets (in minutes and seconds) to extend the end of the countdown.

## ✨ **Key Features**
- 📂 **Automatic configuration file loading** from the `Config` folder.
- 📑 **Multiple configuration support**: The user can choose a file if more than one is detected.
- 🕒 **Time-based execution**: The script checks the current time and runs a command conditionally.
- ⚠️ **Error handling**: Robust error messages for file reading issues and command execution failures.

## 📄 **Configuration File Example** (`Config/Example.txt`)
```text
08:00-12:00 5 30
```

In this example:
- `08:00-12:00` specifies the **time range** during which the script checks for command execution.
- `5` is an optional **time offset in minutes** added to the end of the time range.
- `30` is an optional **time offset in seconds** added to the end of the time range.

## 🛠️ **Requirements**
- **Python 3.x**
- [tclock](https://lib.rs/crates/clock-tui) (**external utility**) for displaying a countdown timer.

## 🚀 **How to Use**
1. Make sure you have at least one configuration file in the `Config` folder. The file should define time ranges and optional time offsets.
2. Run the script using:
   ```bash
   python main.py
   ```
3. If only one configuration file is found, it will be used automatically. If there are multiple, you will be prompted to select one.
4. The script checks the current time against the defined ranges. If it falls within a range, the command is executed with the specified countdown.

## 📝 **Example Output**
```text
Using configuration file: config.txt
Command executed: tclock -c '#FFC0CB' countdown --time 12:05:30
```

In this example:
- The configuration file specifies a time range of `08:00-12:00` with an optional offset of **5 minutes** and **30 seconds**.
- If the current time is within this range, the script extends the time range with the offset and runs the countdown command until `12:05:30`.

## ⚙️ **Error Handling**
- If no configuration files are found in the `Config` folder, the script will exit with the error: **"No configuration files found."**
- If a line in the configuration file is incorrectly formatted, the script skips it and shows an error message, continuing execution.
- If the command fails to execute, an error message is displayed with details of the failure.

## 📜 **License**
This project is open-source and licensed under the **MIT License**. You are free to use, copy, modify, merge, publish, distribute, sublicense, and sell copies of the software, as long as the original license notice is included in all copies or substantial portions of the software.

For more information, refer to the [LICENSE](./LICENSE) file.
