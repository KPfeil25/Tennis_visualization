from bs4 import BeautifulSoup
import requests
import csv

###############################################################################
# Names
###############################################################################
source = requests.get('http://tennisabstract.com/reports/atp_elo_ratings.html').text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())
top400 = []

csv_file = open('top400_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name'])

# find all td (table data) elements in the html
for td in soup.find_all('td'):
    if td.a == None:
        # if there is not an anchor tag, essentially skip
        name = None
    else:
        player_name = td.a.text
        #print(player_name)
        #top400.append(player_name)
        csv_writer.writerow([player_name.encode('utf-8')])

#for i in range(len(top400)):
        #print(top400[i])


csv_file.close()
