import httpx
import sys
import time
import webbrowser
from colorama import Fore

# URL for fetching the latest version information and download link
VERSION_URL = "https://raw.githubusercontent.com/exterpolation/gsgen/production/src/version.txt"
DOWNLOAD_URL = "https://github.com/exterpolation/gsgen/releases/download/Release/GSGen.zip"


def get_current_version() -> float:
    """
    Returns the current version of the script.
    This is a hardcoded value representing the current version number.
    """
    return 1.2


def fetch_latest_version() -> float:
    """
    Fetches the latest version number from the remote server (GitHub).
    Raises exceptions if the HTTP request fails or the version format is invalid.
    """
    try:
        response = httpx.get(VERSION_URL, follow_redirects=True)
        response.raise_for_status()  # Raise an error if the HTTP request was not successful
        return float(response.text.strip())  # Convert the fetched version to a float
    except httpx.HTTPStatusError as e:
        # Handle HTTP errors
        print(f"{Fore.RED}[!] HTTP error: {e.response.status_code} {e.response.reason_phrase}")
        sys.exit(1)
    except httpx.RequestError as e:
        # Handle request errors such as connection issues
        print(f"{Fore.RED}[!] Request error: {str(e)}")
        sys.exit(1)
    except ValueError:
        # Handle errors in version conversion
        print(f"{Fore.RED}[!] Error converting the version number.")
        sys.exit(1)


def check_script_version() -> None:
    """
    Checks if the current script version matches the latest available version.
    If not, it prompts the user to download the latest release and exits the script.
    """
    current_version = get_current_version()

    print(f"{Fore.YELLOW}[!] Checking for updates...")
    latest_version = fetch_latest_version()

    if latest_version > current_version:
        # Notify the user about the new version and provide the download link
        print(f"{Fore.YELLOW}[!] New version available: {latest_version} (Current: {current_version})")
        print(f"{Fore.YELLOW}[!] Download the latest version from: {DOWNLOAD_URL}")
        print(f"{Fore.YELLOW}[!] Opening GitHub page for download...")
        time.sleep(1)
        webbrowser.open(DOWNLOAD_URL)  # Open the browser with the download URL
        time.sleep(3)
        sys.exit(0)  # Exit the script after opening the browser
    else:
        # Notify the user that the script is up to date
        print(f"{Fore.GREEN}[+] The current version ({current_version}) is up to date.\n")


def main() -> None:
    """
    Main function that initiates the version check process.
    """
    check_script_version()


if __name__ == '__main__':
    # Start the script by calling the main function
    main()
