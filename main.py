import requests
from bs4 import BeautifulSoup
from getpass import getpass
from Users import secrets
import os

f = secrets.File()

def scrape():
    url = "https://www.cdc.com.sg/"

    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html')
    print(soup.prettify())



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


    u = secrets.User(username=username, password=password)
    u_dict = {'user' : u}
    f.write_dict(u_dict)
    print(f.read())



if __name__ == "__main__":
    f = secrets.File()
    if f.check():
        user()
    