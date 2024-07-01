import httpx
import sys
import time
import webbrowser
from colorama import Fore


def get_current_version() -> float:
    current_version = 1.2

    return current_version


def check_script_version() -> None:
    current_version = get_current_version()

    try:
        # Fetch the latest version from GitHub
        response = httpx.get("https://raw.githubusercontent.com/exterpolation/gsgen/production/src/version.txt",
                             follow_redirects=True)

        # Check the HTTP status code
        if response.status_code == 200:
            latest_version = response.text.strip()

            # Compare versions
            latest_version = float(latest_version)
            current_version = float(current_version)

            if latest_version == current_version:
                print(f"{Fore.GREEN}[+] Current version is up to date.")
            else:
                print(f"{Fore.YELLOW}[!] New update found!")
                download_url = "https://github.com/exterpolation/gsgen/releases/download/Release/GSGen.zip"

                print(f"{Fore.YELLOW}[!] Download the latest version from: {download_url}")
                print(f"{Fore.YELLOW}[!] Opening the GitHub Page..")
                time.sleep(1)
                webbrowser.open(download_url)
                time.sleep(3)
                sys.exit()

    except httpx.HTTPStatusError as e:
        print(f"{Fore.RED}[!] HTTP error occurred: {e.response.status_code} {e.response.reason_phrase}")
        time.sleep(3)
        sys.exit()
    except httpx.RequestError as e:
        print(f"{Fore.RED}[!] Request error occurred: {str(e)}")
        time.sleep(3)
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}[!] An error occurred: {str(e)}")
        time.sleep(3)
        sys.exit()
