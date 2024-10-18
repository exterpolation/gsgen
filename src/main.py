import os
import sys
import time
from update_checker import *
from colorama import Fore, init
from werkzeug.security import safe_join

# Initialize colorama for colored console output
init(autoreset=True)

source_url = "https://github.com/exterpolation/gsgen/"
author = "Lexia"
author_discord = "tickflow"

current_version = get_current_version()

def get_user_input() -> str:
    """
    Prompts the user to input a clantag.
    :return: User's clantag as a string
    """
    return input(f'{Fore.YELLOW}[?] Enter your clantag: ').strip()

def is_elevated_process() -> bool:
    """
    Checks if the process is running with elevated privileges (admin/system).
    :return: True if elevated, False otherwise
    """
    return os.getenv("PROCESS_ELEVATION_LEVEL") in ("High", "System")

def generate_clantag(user_clantag: str) -> list[str]:
    """
    Generates the animated clantag sequences.
    :param user_clantag: The input clantag from the user
    :return: A list of clantag sequences
    """
    clantag = []
    length = len(user_clantag)

    # Building up the clantag (left padding)
    for i in range(length + 1):
        clantag.append(f"{' ' * (length - i)}{user_clantag[:i]}")

    # Shifting spaces from left to right while removing characters
    for i in range(1, length):
        clantag.append(f"{user_clantag[i:]}{' ' * i}")

    return clantag

def create_file(filename: str = "clantag.txt") -> None:
    """
    Creates a new file if it doesn't exist.
    :param filename: Name of the file to create
    """
    with open(filename, "w"):
        pass

def write_to_file(clantag: list[str], file: str = "clantag.txt") -> None:
    """
    Writes the clantag list to a file.
    :param clantag: List of clantag sequences
    :param file: File path where the clantag will be written
    """
    directory = os.path.dirname(file)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    with open(safe_join(file), "w") as f:
        f.write("\n".join(clantag))

def display_header():
    """
    Clears the terminal and displays the program header.
    """
    os.system("cls" if os.name == "nt" else "clear")
    print(fr"""{Fore.WHITE}
     ________  ________  ________  _______   ________      
    |\   ____\|\   ____\|\   ____\|\  ___ \ |\   ___  \    
    \ \  \___|\ \  \___|\ \  \___|\ \   __/|\ \  \\ \  \   
     \ \  \  __\ \_____  \ \  \  __\ \  \_|/_\ \  \\ \  \  
      \ \  \|\  \|____|\  \ \  \|\  \ \  \_|\ \ \  \\ \  \ 
       \ \_______\____\_\  \ \_______\ \_______\ \__\\ \__\
        \|_______|\_________\|_______|\|_______|\|__| \|__|
                 \|_________|                              

    [?] Current version: {current_version}
    [>] Source: {source_url}
    
    [>] Author: {author}
    [>] Discord: {author_discord}
    """)

def check_for_updates():
    """
    Checks if there is a newer version of the script available.
    """
    print(f"{Fore.YELLOW}[!] Checking for updates..")
    check_script_version()

def get_user_save_path() -> str:
    """
    Prompts the user to input the path where the clantag file will be saved.
    :return: The user-defined path or an empty string
    """
    return input(f"\n{Fore.YELLOW}[?] Enter the path to save the clantag file "
                 f"(leave blank to save in the current folder as 'clantag.txt'): ").strip()

def handle_file_creation(clantag: list[str], user_path: str) -> str:
    """
    Handles file creation based on user input for file path and permissions.
    :param clantag: List of clantag sequences
    :param user_path: The user-provided path for saving the file
    :return: The final file path where the clantag was saved
    """
    if user_path:
        if is_elevated_process():
            write_to_file(clantag, user_path)
        else:
            print(f"{Fore.RED}\n[!] You need to run the program as an administrator "
                  f"to save the file in the specified path.")
            user_input = input(f"{Fore.YELLOW}[?] Do you wish to continue? "
                               f"(If 'n', 'clantag.txt' will be created in the current folder) (Y/n): ").lower()

            if user_input == "y":
                return None
            else:
                create_file()
                write_to_file(clantag)
                return os.path.realpath("clantag.txt")
    else:
        if not os.path.exists("clantag.txt"):
            create_file()
        write_to_file(clantag)
        return os.path.realpath("clantag.txt")

def main() -> int:
    """
    The main entry point of the program.
    :return: Exit status code (0 for success)
    """
    display_header()
    check_for_updates()

    user_clantag = get_user_input()
    if not user_clantag:
        print(f"{Fore.RED}[!] Clantag cannot be empty. Exiting...")
        return 1

    clantag = generate_clantag(user_clantag)

    user_path = get_user_save_path()
    final_path = handle_file_creation(clantag, user_path)

    if final_path:
        print(f"\n{Fore.GREEN}[+] Clantag generated successfully at '{final_path}'\n")
    else:
        print(f"{Fore.GREEN}[!] Default file 'clantag.txt' created in the current folder.\n")

    print(f"{Fore.GREEN}[!] Exiting the program in 5 seconds...")
    time.sleep(5)

    return 0

if __name__ == '__main__':
    sys.exit(main())
