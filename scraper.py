import requests # importing a package we downloaded to allow us to make a get request
from bs4 import BeautifulSoup as bs 

github_user = input('Input your Github Username: ') #taking a user input

url = 'https://github.com/' + github_user #the user input is a github username we concatenate the username and url here 

r = requests.get(url) # we make a get request to grab the url we concatenated
soup = bs (r.content, 'html.parser') #grab the html of the url we request to get 

profile_image = soup.find('img', {'alt' : 'Avatar'})['src'] #on the url we get find these tags and it will assign to our target
print(profile_image) # print our result 