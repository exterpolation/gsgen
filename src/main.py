"""
Clantag example:
                ("                  ")
                ("                 g")
                ("                ga")
                ("               gam")
                ("              game")
                ("             games")
                ("            gamese")
                ("           gamesen")
                ("          gamesens")
                ("         gamesense")
                ("        gamesense ")
                ("       gamesense  ")
                ("      gamesense   ")
                ("     gamesense    ")
                ("    gamesense     ")
                ("   gamesense      ")
                ("  gamesense       ")
                (" gamesense        ")
                ("gamesense         ")
                ("amesense          ")
                ("mesense           ")
                ("esense            ")
                ("sense             ")
                ("sens              ")
                ("sen               ")
                ("se                ")
                ("s                 ")
"""

from update_checker import *

source_url = "https://github.com/exterpolation/gsgen/"
author = "Lexia"
author_discord = "tickflow"

current_version = get_current_version()


def get_user_input() -> str:
    user_clantag = input(f'{Fore.YELLOW}[?]Enter your clantag: ')

    return user_clantag


def generate_clantag(user_clantag: str) -> list[str]:
    clantag = []
    length = len(user_clantag)

    # Building up the clantag
    for i in range(length + 1):
        clantag.append(f"{' ' * (length - i)}{user_clantag[:i]}")

    # Shifting spaces from left to right while removing characters
    for i in range(1, length - 1):
        clantag.append(f"{user_clantag[i:]}{' ' * i}")

    return clantag


def create_file() -> None:
    open("clantag.txt", "x")


def write_to_file(clantag: list[str], file="clantag.txt") -> None:
    # Ensure the directory exists if a full path is provided
    directory = os.path.dirname(file)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    with open(file, "w") as f:
        for tag in clantag:
            f.write(f"{tag}\n")


def main() -> int:
    os.system("cls") if os.name == "nt" else os.system("clear")
    print(fr"""
         ________  ________  ________  _______   ________      
        |\   ____\|\   ____\|\   ____\|\  ___ \ |\   ___  \    
        \ \  \___|\ \  \___|\ \  \___|\ \   __/|\ \  \\ \  \   
         \ \  \  __\ \_____  \ \  \  __\ \  \_|/_\ \  \\ \  \  
          \ \  \|\  \|____|\  \ \  \|\  \ \  \_|\ \ \  \\ \  \ 
           \ \_______\____\_\  \ \_______\ \_______\ \__\\ \__\
            \|_______|\_________\|_______|\|_______|\|__| \|__|
                     \|_________|                              

            [?]Current version: {current_version}
            [>]Source: {source_url}
            
            [>]Author: {author}
            [>]Discord: {author_discord}
            
        """)

    print(f"{Fore.YELLOW}[!]Checking for updates..")
    check_script_version()

    user_clantag = get_user_input()
    clantag = generate_clantag(user_clantag)

    user_path = input(f"{Fore.YELLOW}[?]Enter the path to save the clantag file (If the field is blank, "
                      "clantag.txt will be generated in the same folder): ")

    if user_path:
        write_to_file(clantag, user_path)
    else:
        if not os.path.exists("clantag.txt"):
            create_file()
            write_to_file(clantag)
            user_path = os.path.realpath("clantag.txt")
        else:
            write_to_file(clantag)
            user_path = os.path.realpath("clantag.txt")

    print(f"\n{Fore.GREEN}[+]Clantag generated successfully in {Fore.WHITE}'{user_path}'\n\n"
          f"{Fore.GREEN}[!]Exiting the program in 5s..")
    time.sleep(5)

    return 0


if __name__ == '__main__':
    sys.exit(main())
