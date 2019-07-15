#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup


def print_website(html_content):
    soup = BeautifulSoup(html_content,features="html.parser")
    teambox_list = soup.select('#option2 .teambox')
    for teambox in teambox_list:
        team1 = teambox.select(".team1")
        print(team1[0])


def get_netball_results_page():
    page = requests.get("https://www.nwc2019.co.uk/competition-hub")
    return page


def main():
    netballpage = get_netball_results_page()
    print_website(netballpage.content)


if __name__ == "__main__":
    main()
   
