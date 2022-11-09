# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from audioop import ratecv
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

table_rows = soup.findAll("tr")

deathrate_high = 0
deathrate_low = 100

for row in table_rows[2:53]:

    td = row.findAll("td")
    state = td[1].text
    total_cases = int(td[2].text.replace(",",""))
    total_deaths = int(td[4].text.replace(",",""))
    total_test = int(td[10].text.replace(",",""))
    population = int(td[12].text.replace(",",""))

    death_rate = round((total_deaths / total_cases) * 100, 2)
    test_rate = round((total_test / population) * 100)

    print(f"State: {state}")
    print(f"Death Rate: {death_rate}%")

    if death_rate > deathrate_high:

        deathrate_high = death_rate
        highest_state = state

    if death_rate < deathrate_low:

        deathrate_low = death_rate
        lowest_state = state
     
    print()

print('The state with the highest death rate is:' + highest_state)
print('The state with the lowest death rate is:' + lowest_state)

#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

