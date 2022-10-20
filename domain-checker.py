#!/usr/bin/python
import whois
import csv
import datetime

# Program to collect domains from a text file list,
# output a csv file with headings of Domain Name, Available/Unavailable, Price estimae Low and Price Estimate High

avail = []
domains = []


def getDomainList():
    textfile = input("Enter file with a list of domains:")
    with open(textfile,'r+') as f:
        for domainName in f.read().splitlines():
            domains.append(domainName)
    return domains

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
    return avail

def runOutputCSV():
    with open('DomainAvail.csv', 'w', newline='') as f:
        filewriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE, skipinitialspace=True)
        filewriter.writerow(['Domain Name', 'Available'])
        filewriter.writerows(zip(domains,avail))

if __name__ == "__main__":
    try:
        getDomainList()
        runAvailabilityCheck()
        runOutputCSV()
    except TypeError as e:
        print(e)
    except UnicodeDecodeError as e: 
        print(e)
    except FileNotFoundError as e:
        print(e)
    except:
        raise
