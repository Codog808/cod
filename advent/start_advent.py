from selen_base import shorter_EC
from selen_base import main as chrome_setup

def main(year):
    website = f"https://adventofcode.com/{str(year)}"
    ChromeDriver, wait = chrome_setup()
    ChromeDriver.get(website)
    input("Enter to Quit")
    ChromeDriver.quit()

if __name__ == "__main__":
    main(2022)
