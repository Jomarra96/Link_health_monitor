import csv
import requests


def check_url(url):

    custom_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    

    try:
        response = requests.get(url, timeout = 5)
        if response.status_code == 404:
            return 'Failure'
        else:
            return 'Success'
    except requests.exceptions.RequestException as e:
        return 'Error: ' + str(e)

def check_urls_from_csv(file_name, url_column):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        row_number = 0
        websites_down = 0
        for row in reader:
            row_number += 1
            url = row[url_column]
            status = check_url(url)
            if(status == 'Failure'):
                websites_down += 1
                print(f'Row: {row_number}, URL: {url}, Status: {status}')
            elif(row_number%10 == 0):
                print(f'Current row: {row_number}')
    
        print(f'Done! Found {websites_down} website/s down\r\n')

# Replace with the name of your CSV file (same directory than py file)
# And the name of the column that contains the URLs
check_urls_from_csv('urls.csv', 'URL')
