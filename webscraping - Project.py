from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import csv
import keys2
from twilio.rest import Client



url = 'https://crypto.com/price/showroom/biggest-gainers'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

count = 0

tablerows = soup.findAll('tr')

for row in tablerows[1:6]:

    td = row.findAll("td")

    price = td[3].text.split('$')
    price_change = float(td[4].text.replace("+","").replace("%","")) * .01 * float(price[1].replace(",",""))

    name = soup.findAll('span', attrs = {'class':'chakra-text css-eb93p1'})
    symbol = soup.findAll('span', attrs = {'class':'chakra-text css-1jj7b1a'})

    print()
    print('Name:', name[count].text)
    print('Symbol:', symbol[count].text)
    print('Current Price:', '$' + price[1])
    print('24H Change:', td[4].text)
    print('Price Change:', '$' + str(round(price_change, 4)))
    print()

    count += 1




url2 = 'https://crypto.com/price'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url2, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')



client = Client(keys2.accountSID, keys2.authToken)

TwilioNumber = "+19293232842"
myCellphone = "+12544955113"

tr = soup.findAll('tr')

bitcoin_price = tr[1].text.split('$')
ethereum_price = tr[2].text.split('$')

bprice = float(bitcoin_price[1].replace(",",""))
eprice = float(ethereum_price[1].replace(",",""))

if bprice < 40000:

    textmsg = client.messages.create(to = myCellphone, from_ = TwilioNumber, body = 'Bitcoin is below $40,000!')

    print(textmsg.status)

if eprice < 3000:

    textmsg = client.messages.create(to = myCellphone, from_ = TwilioNumber, body = 'Ethereum is below $3,000!')

    print(textmsg.status)

