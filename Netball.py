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
        team2_score = scores[1].get_text()
        result.append(team1[0].get_text())
        result.append(team1_score)
        result.append(team2[0].get_text())
        result.append(team2_score)
        results_list.append(result)
    return results_list


def print_results(team_name, results_list):
    for result in results_list:
        team1  = result[0]
        team2 = result[2]
        if team1 == team_name or team2 == team_name:
            print(result)
        

def gather_historic_results(team_name, years):
    print("Gathering historic results...")
    results = []
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    for year in range(2019, 2019 - years, -1):
        print("[" + str(year) + "]")
        for month in months:
            url = "https://www.skysports.com/netball/results/" +month +"-" + str(year)
            scrape_sky_results(url, results)
    print (results)

def scrape_sky_results(url, results_list):
    print("Loading: " + url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content,features="html.parser")
    match_results = soup.select('.matches__list-item')
    for match in match_results:
        result = []
        scores = match.select(".matches__teamscores-side")
        teams = match.select(".swap-text__target")
        result.append(teams[0].text)
        result.append(int(scores[0].text))
        result.append(teams[1].text)
        result.append(int(scores[1].text))
        results_list.append(result)


def get_netball_results_page():
    page = requests.get("https://www.nwc2019.co.uk/competition-hub/")
    return page


def main():
    netballpage = get_netball_results_page()
    results = gather_results(netballpage.content)
    print_results("England", results)
    print_results("Scotland", results)
    gather_historic_results("England", 2)
    


if __name__ == "__main__":
    main()
   
