import csv

import requests
from bs4 import BeautifulSoup

date = input("Please enter the date in the following format MM/DD/YY: ")

# Request the webpage
page = requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}#")

def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    matches_details = []

    # Find all match cards
    championShips = soup.find_all("div", {"class": "matchCard"})

    def get_match_info(championShip):
        if championShip:
            title_element = championShip.find('h2')
            if title_element:
                championShip_title = title_element.text.strip()
                print(f"Championship Title: {championShip_title}")
            else:
                print("No title element found.")

            matches_section = championShip.find("div", {"class": "matchCard matchesDate"})
            if matches_section:
                all_matches = matches_section.find_all('li')
                print(f"Found {len(all_matches)} matches.")
                for match in all_matches:
                    try:
                        team_A = match.find('div', {'class': 'teams teamA'}).find('p').text.strip()
                        team_B = match.find('div', {'class': 'teams teamB'}).find('p').text.strip()
                        print(f"Match: {team_A} vs {team_B}")

                        match_result = match.find('div', {'class': 'MResult'}).find_all('span', {'class': 'score'})
                        if len(match_result) >= 2:
                            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
                        else:
                            score = "N/A"

                        match_time = match.find('div', {'class': 'MResult'}).find('span', {'class': 'time'}).text.strip()
                        print(f"Time: {match_time}, Score: {score}")

                        matches_details.append({
                            "نوع البطولة": championShip_title,
                            "الفريق الاول": team_A,
                            "الفريق الثاني": team_B,
                            "ميعاد المبارة": match_time,
                            "النتيجة": score
                        })
                    except AttributeError as e:
                        print(f"Error extracting match data: {e}")
            else:
                print("No matches section found in championShip.")
        else:
            print("ChampionShip content is empty.")

    if championShips:
        for championShip in championShips:
            get_match_info(championShip)

        if matches_details:
            keys = matches_details[0].keys()
            with open("yallakora.csv", 'w', newline='', encoding='utf-8') as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(matches_details)
            print("CSV file created successfully.")
        else:
            print("No match details found.")
    else:
        print("No match cards found.")

# Call the main function
main(page)
