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
csv_writer.writerow('Name')

# find all td (table data) elements in the html
for td in soup.find_all('td'):
    if td.a == None:
        # if there is not an anchor tag, essentially skip
        name = None
    else:
        player_name = str(td.a.text)
        #print(player_name)
        top400.append(player_name)

for i in range(len(top400)):
        print(str(top400[i]))
        csv_writer.writerow(top400[i])

#print(top400[200])
csv_file.close()