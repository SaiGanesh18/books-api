import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv('api_key')

def best_seller_list_names(api_key):
    # URL to fetch best-seller list names
    url = f'https://api.nytimes.com/svc/books/v3/lists/names.json?api-key={api_key}'
    
    response = requests.get(url)

    if response.status_code == 200:
        print("Request successful!")
        #print(response.json())  # Print the JSON response
    else:
        print(f"Error: {response.status_code}")
        print(response.text)  # Print error message from the API

best_seller_list_names(api_key)

def get_review_of_a_book(api_key, isbn, title, author):

    url = f'https://api.nytimes.com/svc/books/v3/reviews.json?isbn={isbn}&title={title}&author={author}&api-key={api_key}'


    response = requests.get(url)

    if response.status_code == 200:
        print("Request successful!")
        #print(response.json())  # Print the JSON response containing the review
    else:
        print(f"Error: {response.status_code}")
        print(response.text)  # Print error message from the API

get_review_of_a_book(api_key, '0316066524', 'CURIOUS TIDES', 'Pascale Lacelle')

def get_best_sellers_by_date(api_key, date):
    url = f'https://api.nytimes.com/svc/books/v3/lists/{date}/hardcover-fiction.json?offset=20&api-key={api_key}'
    
    response = requests.get(url)

    if response.status_code == 200:
        print("Request successful!")
        #print(response.json())  # Print the JSON response containing the best-sellers
    else:
        print(f"Error: {response.status_code}")
        print(response.text)  # Print error message from the API

# Example: Call the get_best_sellers_by_date function with your desired date
get_best_sellers_by_date(api_key, '2024-11-01')

def get_best_sellers_history(api_key, date):
    url = f'https://api.nytimes.com/svc/books/v3/lists/full-overview.json?published_date=2024-11-02&api-key={api_key}'
    
    response = requests.get(url)

    if response.status_code == 200:
        print("Request successful!")
        #print(response.json())  # Print the JSON response containing the best-sellers
    else:
        print(f"Error: {response.status_code}")
        print(response.text)  # Print error message from the API

# Example: Call the get_best_sellers_by_date function with your desired date
get_best_sellers_history(api_key, '2024-11-01')


def get_all_books_by_specific_date(api_key, date):
    url = f'https://api.nytimes.com/svc/books/v3/lists/overview.json?published_date=2024-11-22&api-key={api_key}'
    
    response = requests.get(url)

    if response.status_code == 200:
        print("Request successful!")
        #print(response.json())  # Print the JSON response containing the best-sellers
    else:
        print(f"Error: {response.status_code}")
        print(response.text)  # Print error message from the API

# Example: Call the get_best_sellers_by_date function with your desired date
get_all_books_by_specific_date(api_key, '2024-11-01')

def get_bestseller_list(api_key):
    url = f'https://api.nytimes.com/svc/books/v3/lists.json?list=hardcover-fiction&bestsellers-date=3596-14-26&published-date=3596-14-26&offset=20&api-key={api_key}'
    
    response = requests.get(url)

    if response.status_code == 200:
        print("Request successful!")
        #print(response.json())  # Print the JSON response containing the best-sellers
    else:
        print(f"Error: {response.status_code}")
        print(response.text)  # Print error message from the API

get_bestseller_list(api_key) 

def get_top_5_best_sellers(api_key):
    url = f'https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?age-group=14&author=Michael Connelly&contributor=iraguha&isbn=0316066524&offset=20&price=2345&publisher=alexis&title=Great signs&api-key={api_key}'
    
    response = requests.get(url)

    if response.status_code == 200:
        print("Request successful!")
        #print(response.json())  # Print the JSON response containing the best-sellers
    else:
        print(f"Error: {response.status_code}")
        print(response.text)  # Print error message from the API

get_top_5_best_sellers(api_key)