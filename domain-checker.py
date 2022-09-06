#!/usr/bin/python
import whois
import csv
import datetime

# Program to collect domains from a text file list,
# output a csv file with headings of Domain Name, Available/Unavailable, Price estimae Low and Price Estimate High

avail = []
domains = []


def getDomainList():
    with open('domains.txt','r+') as f:
        for domainName in f.read().splitlines():
            domains.append(domainName)

def runAvailabilityCheck():
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

def runOutputCSV():
    with open('persons.csv', 'w') as f:
        filewriter = csv.writer(f)
        filewriter.writerow(['Domain Name', 'Availble'])
        for dom in domains:
            if dom is not None and dom != '':
                for ava in avail:
                    if ava is not None and dom != '':
                        filewriter.writerow([dom, ava])

if __name__ == "__main__":
    getDomainList()
    runAvailabilityCheck()
    runOutputCSV()
    
    #print(dictdomains)
    print(domains)
    print(avail)
