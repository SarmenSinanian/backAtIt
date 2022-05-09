from flask import Flask, request
import random
import requests
import re

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

wordsCleaned = []
encoding = 'utf-8'

for i in WORDS:
    wordsCleaned.append(str(i, encoding))

hashtaggedSpacedWords = []
for i in wordsCleaned:
    x = i+('# ')
    hashtaggedSpacedWords.append(x)

def randomWords(length):
    result_str = [random.choice(hashtaggedSpacedWords) for x in range(length)]
    return result_str

def instagramHashtagHider(numberOfRandomWords, yourHashtags):
    placeholder = 0
    r = randomWords(numberOfRandomWords)
    a = int(len(r)/5)
    x = yourHashtags.split()
    editedList = []
    pattern = re.compile('[\W_]+')
    for i in x:
        j = pattern.sub('', i)
        edited = '#' + j + ' '
        editedList.append(edited)
    for i in editedList:
        r[a + placeholder] = i
        placeholder += 3
    string1 = ''
    for i in r:
        string1 += i
    return string1

instagramHashtagHider(100, )

# app = Flask(__name__)
#
# @app.post('/input')
# def do_input():
# #    data = request.form.get('data')
# #    myHashtags = data.split(",")
#     return instagramHashtagHider(50, myHashtags)

# @app.route('/')
# def index():
#     return """
# <html>
# <head><title>Test</title></head>
# <body>
#
# <form method="POST" action="/input">
#     <input name="data" type="text">
# </form>
#
# </body>
# </html>
#     """
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)
