from urllib.parse import unquote, quote
import re
import json
from urllib.request import urlopen
import doctest

# query = "kurdistan"


def main():
    query = input('start your search here:   ')
    response = grab_response(query)
    print('BBC search engine suggests:')
    for line in response_parser(response):
        print(line)


def grab_response(input_text):
    """
    inserts input_text into the example url string
        quotes it (hello json)
        and returns the search engine's response, decoded.
    """
    request_url = ('http://data.bbc.co.uk/search-suggest/'
                   'suggest?q={}&format=blq-1&'
                   'apikey=A4LBTSY4hzZ7IpArvqO8XET4vnxajqWo&'
                   'scope=all&'
                   'callback=jQuery17203559288482647389_1419105175525'
                   )
    quoted_query = quote(input_text)
    url = request_url.format(quoted_query)
    response = urlopen(url).read().decode('utf-8')
    # print('response', response)
    return response
    # unquoted = unquote(request_url)
    # print(unquoted)



def response_parser(response):
    """
    parses bbc search suggestions forming a list of strings

    Example:
    >>> response = 'jQuery17203815351417288184_1419116101558(' \
               '[' \
                   '"doctor who",' \
                   '[' \
                       '{' \
                           '"id" : "tleo:b006q2x0",' \
                           '"ids" : "bbc:doctorwho sp:doctor_who tleo:b006q2x0 tleo:b009szrh",' \
                           '"title" : "Doctor Who","type" : "tleo",' \
                           '"types" : "bbc searchplus tleo"' \
                           '},' \
                       '{' \
                           '"id" : "tleo:b03phwzl",' \
                           '"ids" : "tleo:b03phwzl",' \
                           '"title" : "Doctor Who: The Ultimate Guide",' \
                           '"type" : "tleo","types" : "tleo"' \
                        '}' \
                   ']' \
               ']' \
               ');'
    >>> response_parser(response)
    ['Doctor Who', 'Doctor Who: The Ultimate Guide']

    """

    notitle = re.sub('^[^(]*[(]', '[', response)
    text = re.sub('[)][^)]*$', ']', notitle)
    # print(text)
    data = json.loads(text)
    data = data[0]
    requested = data[0]
    noisy_suggestions = data[1]
    # print('request', requested)
    # print('suggestions', noisy_suggestions)

    result = []
    for item in noisy_suggestions:
        # print(item)
        result.append(item['title'])
        # print('result', result)
    # print('result', result)
    return result

if __name__ == "__main__":
    print(doctest.testmod())
    main()





