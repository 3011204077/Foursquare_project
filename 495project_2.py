import json
import requests
import csv

testfile = csv.reader(open('LocationID-final-a.csv', 'rb'))
newfile = csv.writer(open('result_2.csv', 'ab'))
checkfile = csv.reader(open('result_2.csv', 'rb'))
count = 0
start_index = 0
for row in checkfile:
    if row != None:
        start_index += 1
#print start_index

for row in testfile:
    if start_index != 0:
        start_index -= 1
        continue
    #count += 1
    ll = str(row[2]) + ',' + str(row[3])
    user1_url = 'https://api.foursquare.com/v2/venues/search?client_id=BWSNEMZEUI5MBVMYKZDAIZPE0YVO2NTQCYPEMZTRL2IVJYFI&client_secret=VD1KYUVLO0IW1XJRYPXUSXRQ3FSMDWSPDHK0J5U5XDXTI211&v=20140815&ll=' + ll
    user2_url = 'https://api.foursquare.com/v2/venues/search?client_id=QRULZKCT34G1A1S0DMM4ME3FZ3F2JW34JSLLYU1FWPXRLT43&client_secret=ND5WDZ0AXR4KDRKKOEUP5PWRTZ1K5W52HRQCIKUR5VQ310HT&v=20140815&ll=' + ll
    user3_url = ''
    #url = user1_url
    if count <= 5000:
        url = user1_url
    if count > 5000 and count <= 10000:
        url = user2_url
    resp = requests.get(url = url)
    data = resp.json()
    print ll
    print data
    #{u'meta': {u'errorType': u'rate_limit_exceeded', u'code': 403, u'requestId': u'57565988498e5729d33e9273', u'errorDetail': u'Quota exceeded'}, u'response': {}}
    if data[u'response'] == {}:
        ur
    if ll == '0,0' or data[u'response'][u'venues'] == []:
        print 'None'
        #nrow = copy.deepcopy(row)
        row.append('None')
        newfile.writerow(row)
    else:
        #print data[u'response'][u'venues']
        #print data[u'response'][u'venues'][0][u'location'][u'formattedAddress']
        #print data[u'response'][u'venues'][0][u'categories'][0][u'shortName']
        pool = {'a': 0, 'c': 0, 'e': 0, 'f': 0, 'n': 0, 'p': 0, 'b': 0, 'r': 0, 's': 0, 't': 0}
        for entry in data[u'response'][u'venues']:
            if entry[u'categories'] != []:
                capital = entry[u'categories'][0][u'icon'][u'prefix'][39]
                pool[capital] += 1
        max_capital = max(pool.values())
        for key in pool.keys():
            if pool[key] == max_capital:
                capital = key
                break
        print capital
        print count
        #capital = data[u'response'][u'venues'][0][u'categories'][0][u'icon'][u'prefix'][39]
        if capital == 'a':
            #print 'Arts & Entertainment'
            row.append('Arts & Entertainment')
        if capital == 'c':
            #print 'College & University'
            row.append('College & University')
        if capital == 'e':
            #print 'Event'
            row.append('Event')
        if capital == 'f':
            #print 'Food'
            row.append('Food')
        if capital == 'n':
            #print 'Nightlife Spot'
            row.append('Nightlife Spot')
        if capital == 'p':
            #print 'Outdoors & Recreation'
            row.append('Outdoors & Recreation')
        if capital == 'b':
            #print 'Professional & Other Places'
            row.append('Professional & Other Places')
        if capital == 'r':
            #print 'Residence'
            row.append('Residence')
        if capital == 's':
            #print 'Shop & Service'
            row.append('Shop & Service')
        if capital == 't':
            #print 'Travel & Transport'
            row.append('Travel & Transport')
        
        #print data[u'response'][u'venues'][0][u'categories'][0][u'icon'][u'prefix'][39:]
        #print data[u'response'][u'venues'][0][u'categories'][0][u'shortName']
        print row
        newfile.writerow(row)
        count += 1

'''
ll = '34.10748083,-118.2544345'
url = 'https://api.foursquare.com/v2/venues/search?client_id=BWSNEMZEUI5MBVMYKZDAIZPE0YVO2NTQCYPEMZTRL2IVJYFI&client_secret=VD1KYUVLO0IW1XJRYPXUSXRQ3FSMDWSPDHK0J5U5XDXTI211&v=20140815&ll=' + ll
resp = requests.get(url = url)
data = resp.json()
if data[u'response'][u'venues'] == []:
    print 666
print data[u'response'][u'venues']
'''