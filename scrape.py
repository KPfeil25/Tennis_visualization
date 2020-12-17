from bs4 import BeautifulSoup
import requests
import csv

###############################################################################
# Names
###############################################################################
source = requests.get('https://www.espn.com/tennis/rankings').text

soup = BeautifulSoup(source, 'lxml')

#print(soup.prettify())
top400 = []

csv_file = open('top400_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name'])

# find all a tags where the class is AnchorLink, BUT theres an issue
# there are many many a tags with this class
# hence the logical ~ maze ~
num_players = 0
for tr in soup.find_all("a", class_= "AnchorLink"):
    num_spaces = 0
    player_name = tr.text
    for letter in player_name:
        if letter == " ":
            num_spaces += 1
    if (num_spaces == 1 or num_spaces == 2) and num_players < 100 and player_name != "Grand Slam History":
        #print(player_name)
        num_players += 1
        top400.append(player_name)
        csv_writer.writerow([player_name])

#for i in range(len(top400)):
        #print(top400[i])

csv_file.close()
