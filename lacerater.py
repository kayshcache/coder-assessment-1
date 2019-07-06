#! /usr/local/bin/python3.7
'''
Date: 1st of July 2019
Author: Danxyeal
Contact: @gmail.com
License: GNU
Version: .1
'''
import argparse
import requests
import os
import bs4
import datetime

def main():
    '''
    Takes the arguments from CLI. Uses flow control to construct the output accordingly and prints user-requested information.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='The website address to be scraped.')
    parser.add_argument('--source', help='Print the source of the webpage.', action='store_true')
    parser.add_argument('--text', help='Print all text from the webpage.', action='store_true')
    parser.add_argument('--explore', help='Iterates over response object', action='store_true')
    parser.add_argument('--file', help='Produces a file', action='store_true')
    
    cli_args = parser.parse_args() # Variable of arguments parsed to the ArgeParser object
    url_obj = download_url(cli_args.url)
    output = set()
    # Main control flow
    if cli_args.source:
        output.add(parse_source(url_obj))

    if cli_args.explore:
        output.add(str(url_obj.headers))
        
    if cli_args.text:
        output.add(strip_html(url_obj))

    if cli_args.file:
        filename = make_file(url_obj)
        output.add(f'\n Your file was created with filename: {filename}')
    
    for item in output:
        print(item)

def download_url(url):
    '''
    Takes a URL as a string. Use requests module to get an object of the response from the server.
    '''
    print(f'Downloading page {url}...')
    try:
        url_obj = requests.get(url)
        url_obj.raise_for_status()
        return url_obj
    except Exception as exc:
        print(f'Problem with: {exc}')
        quit() # If any problem occurs with getting the URL data then the program just quits, usr can try again

def parse_source(response_obj):
    '''
    Take the response from the server, return the HTML source.
    '''
    return bs4.BeautifulSoup(response_obj.text, features='html.parser')

def strip_html(url_obj):
    '''
    Take the url response object, remove HTML tags and return text only.
    '''
    html_source = parse_source(url_obj)
    return html_source.getText()

def make_file(data):
    '''
    Takes the output set from main,
    Writes all to file, returns the filename
    '''
    filename = f'lacerated{datetime.datetime.now()}'
    with open(filename, 'wb') as data_file:
        for portion in data.iter_content(50000):
            # Writes the data in smaller portions to avoid memory problems that might occur attempting to save large files.
            data_file.write(portion)
    return filename

if __name__ == "__main__":
    main()
