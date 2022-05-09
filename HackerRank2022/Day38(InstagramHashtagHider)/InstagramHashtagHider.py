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

'''add length modifier based on spacing and number of hashtags'''

# def instagramHashtagHider(numberOfRandomWords, yourHashtags):
#     placeholder = 0
#     r = randomWords(numberOfRandomWords)
#     a = int(len(r)/5)
#     for i in yourHashtags:
#         r[a + placeholder] = i
#         placeholder += 3
#     string1 = ''
#     for i in r:
#         string1 += i
#     return string1
#
# hashtagStr = '#facebookmemes #facebookmeme #facebookmemesaretherapy #badlyeditedfacebookmemes #facebookmemetemplate #fbmemes #pinterestinspired #pinterestmemes #reactionpics #wholesomememes #memes #mommy #cursedimages #cursed #cursedmemes #explore #explorepage #cursedimage #cod #codmemes #callofduty #callofdutymemes '
# x = hashtagStr.split()
# editedList = []
# '''Converting all values to alphanumeric only'''
# pattern = re.compile('[\W_]+')
# for i in x:
#     j =pattern.sub('', i)
#     edited = '#' + j +' '
#     editedList.append(edited)
#
# editedList
#
# myHashtags = editedList

def instagramHashtagHider(yourHashtags):
    placeholder = 0
    x = yourHashtags.split()
    r = randomWords(max(len(x)*5, 100))
    a = int(len(r) / 5)
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

myHashtags = '#facebookmemes #facebookmeme #facebookmemesaretherapy #badlyeditedfacebookmemes #facebookmemetemplate #fbmemes #pinterestinspired #pinterestmemes #reactionpics #wholesomememes #memes #mommy #cursedimages #cursed #cursedmemes #explore #explorepage #cursedimage #cod #codmemes #callofduty #callofdutymemes '
# x = hashtagStr.split()
# editedList = []
'''Converting all values to alphanumeric only'''
# pattern = re.compile('[\W_]+')
# for i in x:
#     j =pattern.sub('', i)
#     edited = '#' + j +' '
#     editedList.append(edited)

    
# editedList
#
# myHashtags = editedList

print(instagramHashtagHider(myHashtags))

'''Create uniformity in the inputs by splitting at spaces, removing non-alphanumeric characters, add hashtags at front'''
'''Auto size based on number of input hashtags'''

myHashtags = 'rocket jim808 crac###2@#!#@#%#'

x = myHashtags.split()
myHashtags = []
pattern = re.compile('[\W_]+')
for i in x:
    j = pattern.sub('', i)
    edited = '#' + j + ' '
    myHashtags.append(edited)

print(myHashtags)
print(x)