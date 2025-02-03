# Pentest Simulator

## Description
This Python script is designed to demonstrate how penetration testing tools can affect files in a system, emulating virus-like behavior. It scans specific files in a directory and simulates infection by overwriting them with the script's content. The tool logs all actions and results to a file for further analysis.

The goal of this script is purely educational and intended for use only in safe, controlled environments. Unauthorized use is prohibited.

## Features
- Scans files with specified extensions (e.g., `.txt`, `.exe`) 
- Simulates virus-like behavior by appending script code to existing files.
- Logs the results, including the files infected and the timestamp.
- Delays between actions to mimic real-time behavior.
- Safe environment check to prevent running in unsafe or production environments.

## Requirements
- Python 3.x
- No external dependencies required.

## Usage
1. Clone or download the repository.
2. Set up an environment variable `SAFE_ENV` with the value `YES` to enable the script to run.
3. Place some target files (`.txt`, `.exe`, etc.) in the same directory.
4. Run the script with the command:

Warning
This tool should only be used in a controlled and isolated testing environment. It is not intended for malicious use and should not be used on systems without explicit permission.

License
This script is provided for educational purposes only. All rights reserved.