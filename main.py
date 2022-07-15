# import libraries
import requests
from bs4 import BeautifulSoup
from getpass import getpass
from Users import secrets
import os


# function for user creation
def user():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    while True:
        print("Please confirm your username and password")
        print("Username: %s\nPassword: %s" %(username, password))
        print("[Enter to continue]")
        choice = input("\n: ")
        
        if choice == '':
            break
        else:
            print('Enter valid choice')
            continue

    f = secrets.File()
    u = secrets.User(username=username, password=password)
    u_dict = {'user' : u}
    f.write_dict(u_dict)

# function for webscraping
def scrape():
    # url = "https://www.cdc.com.sg/"
    url = "https://bookingportal.cdc.com.sg:8443/NewPortal/Booking/BookingTT.aspx"

    payload = {
        'LearnerID' : 'P0122546',
        'Pswd' : '30282319'
    }

    r = requests.get(url, payload)

    soup = BeautifulSoup(r.content, 'html')

    table = soup.find_all('table', attrs={'id' : 'ctl00_ContentPlaceHolder1_gvLatestav'})
    print(soup.prettify())

if __name__ == "__main__":
    f = secrets.File()
    if f.check():
        user()
    user_dict = f.read()
    u = user_dict['user']
    
    scrape()