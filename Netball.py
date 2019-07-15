#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup


def gather_results(html_content):
    soup = BeautifulSoup(html_content,features="html.parser")
    teambox_list = soup.select('#option2 .teambox')
    results_list = []
    for teambox in teambox_list:
        result = []
        team1 = teambox.select(".team1")
        team2 = teambox.select(".team2")
        scores = teambox.select(".status")
        team1_score = scores[0].get_text()
        team2_score = scores[0].get_text()
        result.append(team1[0].get_text())
        result.append(team1_score)
        result.append(team2[0].get_text())
        result.append(team2_score)
        results_list.append(result)
    return results_list


def print_results(team_name, results_list):
    for team_name in results_list:
        if team1 or team2 is "England":
            print(results_list)
        else:
            print_results



def get_netball_results_page():
    page = requests.get("https://www.nwc2019.co.uk/competition-hub/")
    return page


def main():
    netballpage = get_netball_results_page()
    results = gather_results(netballpage.content)
    print_results("England", results)
    


if __name__ == "__main__":
    main()
   
