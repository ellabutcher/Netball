#!/usr/bin/env python3

import requests


def get_hockey_results_page():
    page = requests.get("https://www.nwc2019.co.uk/competition-hub")
    return page


def main():
    hockeypage = get_hockey_results_page()
    print(hockeypage.content)

if __name__ == "__main__":
    main()
   
