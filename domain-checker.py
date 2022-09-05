#!/usr/bin/python
import whois
#import csv
#import datetime

# Program to collect domains from a text file list,
# output a csv file with headings of Domain Name, Available/Unavailable, Price estimae Low and Price Estimate High

avail = []
domains = []


def getDomains():
    with open('domains.txt','r+') as f:
        for domainName in f.read().splitlines():
            domains.append(domainName)

def run():
    for dom in domains:
        if dom is not None and dom != '':
            try:
                details = whois.whois(dom)
                if "contacts" in details.text or "registrant" in details.text:
                    avail.append('False')
                else:
                    avail.append('True')
            except (whois.parser.PywhoisError):
                avail.append('True')

def OutputCSV():
    with open('persons.csv', 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Domain Name', 'Availability', 'Estimated Low', 'Estimated High', 'Last Checked: ' + datetime.datetime.now().strftime("%x")])

if __name__ == "__main__":
    getDomains()
    run()
    convert()
    #print(dictdomains)
    print(domains)
    print(avail)
    print(dictdomains)
