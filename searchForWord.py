from bs4 import BeautifulSoup
import urllib.request
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Count the word frequency
# then for the searched word return the frequency
def countSearchWord(clean_tokens, searchWord):
    freq = nltk.FreqDist(clean_tokens)
    for key,val in freq.items(): 
        if str(key) == searchWord:
            return val

# Need to run these only once
#nltk.download("stopwords")
#nltk.download("wordnet")
#nltk.download('punkt')

# Read html document and remove the html tags
response = urllib.request.urlopen('https://en.wikipedia.org/wiki/Paris')
soup = BeautifulSoup(response.read(),"html.parser")
text = soup.get_text(strip=True)
tokens = word_tokenize(text)
clean_tokens = tokens[:]

# Remove English stop words
stopwords = stopwords.words("english")
for token in tokens:
   if token in stopwords:
      clean_tokens.remove(token)

searchWord = input("Enter Search Term->")
count = countSearchWord(clean_tokens, searchWord)
print(searchWord + " occurred " + str(count) + " times ")