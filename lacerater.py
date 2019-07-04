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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='The website address to be scraped.')
    parser.add_argument('--source', help='Print the source of the webpage.', action='store_true')
    parser.add_argument('--text', help='Print all text from the webpage.', action='store_true')
    parser.add_argument('--explore', help='Iterates over response object', action='store_true')
    
    cli_args = parser.parse_args()
    url_obj = download_url(cli_args.url)
    output = ''
    
    if cli_args.source:
        output = parse_source(url_obj)

    if cli_args.explore:
        response_list = list(url_obj)
        print(url_obj.headers)
        # print(response_list)
        # for k in response_list:
        #     print(k,'\n')
        
    if cli_args.text:
        output = strip_html(url_obj)

    print(output)

def download_url(url):
    '''
    Takes a URL as a string. Use requests to get an object of the response from the server.
    '''
    print('Downloading page %s...' % url)
    try:
        url_obj = requests.get(url)
        url_obj.raise_for_status()
        return url_obj
    except Exception as exc:
        print('Problem with: %s' % (exc))
        quit()

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



if __name__ == "__main__":
    main()
