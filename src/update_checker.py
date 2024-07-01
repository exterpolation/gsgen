import httpx
import tempfile
import os
import sys
import time
from colorama import Fore


def get_current_version() -> float:
    current_version = 1.0

    return current_version


def check_script_version() -> None:
    current_version = get_current_version()

    try:
        # Fetch the latest version from GitHub
        response = httpx.get("https://raw.githubusercontent.com/exterpolation/gsgen/production/version.txt")
        response.raise_for_status()
        latest_version = response.text.strip()
        latest_version = float(latest_version)

        # Compare versions
        if latest_version == current_version:
            print(f"{Fore.GREEN}[+] Current version is up to date.")
        else:
            print(f"{Fore.YELLOW}[!] New update found! Updating...")
            download_url = "https://github.com/exterpolation/gsgen/releases/download/Stable/GSGen.exe"

            # Download the new version
            with httpx.stream("GET", download_url) as response:
                response.raise_for_status()
                with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                    for chunk in response.iter_bytes():
                        tmp_file.write(chunk)

            print(f"{Fore.GREEN}[!]Download complete. Updating...")

            # Replace the current script with the updated version
            current_script_path = os.path.realpath(__file__)
            os.replace(tmp_file.name, current_script_path)

            print(f"{Fore.GREEN}[!]Update complete. Please restart the program.")
            time.sleep(5)
            sys.exit()

    except httpx.HTTPStatusError as e:
        print(f"{Fore.RED}[!]HTTP error occurred: {e.response.status_code} {e.response.reason_phrase}\n")
        time.sleep(2)
        sys.exit(1)
    except httpx.RequestError as e:
        print(f"{Fore.RED}[!]Request error occurred: {str(e)}\n")
        time.sleep(2)
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}[!]An error occurred: {str(e)}\n")
        time.sleep(2)
        sys.exit(1)
