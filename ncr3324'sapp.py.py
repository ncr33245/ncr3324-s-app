import webbrowser
import os
import shutil

# ANSI escape code for green text
GREEN = "\033[92m"

def set_console_title(title):
    if os.name == 'nt':  # Check if the OS is Windows
        os.system(f'title {title}')
    else:
        print(f'\033]0;{title}\007', end='', flush=True)

def show_menu():
    set_console_title("ncr3324's app")  # Set console title
    print(GREEN + "Welcome to ncr3324's app")
    print("Choose an option:")
    print("1. Install File")
    print("2. Calculator")
    print("3. Other Project")
    print("4. Exit")
    print("5. More Options" + "\033[0m")  # Reset text color

def get_user_choice():
    try:
        choice = int(input("Enter your choice (1-5): "))
        return choice
    except ValueError:
        return 0

def option_1():
    print(GREEN + "You selected Install Files")

    # List of files to install
    files_to_install = ["searchinfo.bat"]

    # Specify the installation directory (absolute path to Downloads)
    installation_directory = os.path.expanduser("~/Downloads")

    try:
        # Get the directory of the script
        script_directory = os.path.dirname(os.path.abspath(__file__))

        # Create the installation directory if it doesn't exist
        os.makedirs(installation_directory, exist_ok=True)

        # Simulate installation by copying the file
        for file in files_to_install:
            source_path = os.path.join(script_directory, file)
            destination_path = os.path.join(installation_directory, file)

            shutil.copy(source_path, destination_path)
            print(f"Installed {file} to {installation_directory}")

        print("Installation complete!" + "\033[0m")  # Reset text color

    except Exception as e:
        print(f"An error occurred: {e}")

    input("Press Enter to continue...")  # Add this line to keep the script open

def option_2():
    print(GREEN + "You selected Calculator" + "\033[0m")  # Reset text color
    
    try:
        # Get user input for mathematical expression
        expression = input("Enter a mathematical expression: ")
        
        # Evaluate the expression and print the result
        result = eval(expression)
        print(f"Result: {result}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

    input("Press Enter to continue...")  # Add this line to keep the script open

def option_3():
    print(GREEN + "You selected Other Project")
    project_link = "https://khlovr.000webhostapp.com/"
    webbrowser.open(project_link)
    print("\033[0m")  # Reset text color

def option_5():
    print(GREEN + "More options are being made. Stay tuned!" + "\033[0m")  # Reset text color

# Main program
set_console_title("ncr3324's app")  # Set initial console title
print(GREEN + "ncr3324's app" + "\033[0m")  # Reset text color
while True:
    show_menu()
    user_choice = get_user_choice()

    if user_choice == 1:
        option_1()
    elif user_choice == 2:
        option_2()
    elif user_choice == 3:
        option_3()
    elif user_choice == 5:
        option_5()
    elif user_choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
