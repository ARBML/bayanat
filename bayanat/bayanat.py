from collections import Counter
import re
from sklearn.decomposition import PCA
import numpy as np
import random 
import matplotlib.pyplot as plt
import gensim
from arabic_reshaper import ArabicReshaper
from bidi.algorithm import get_display
from bayanat.utils import * 

class Bayanat:

  def __init__(self, file_name):
    self.data = open(file_name, 'r').read()
  
  def get_top_n_words(self, n = 10):
    freq = Counter()
    for word in self.data.split():
      freq[word] += 1
    return freq.most_common(n = n)
  
  def get_chars(self):
    return set(self.data)

  def _get_all_alphabets(self):
    return set('ةءاأإبتثجحخدذرزسشصضطظعغفقكلمنهوؤيئى')

  def _get_all_puncts(self):
    return set('?؟!:;-.,،')

  def get_non_alphabets(self):
    return self.get_chars() - self._get_all_alphabets()
  
  def _get_all_special_chars(self):
    ords = list(range(33, 48)) + list(range(58, 65)) + \
           list(range(91, 97)) + list(range(123, 127)) + [1567, 1548]
    chars = [chr(num) for num in ords]
    return set(chars)

  def _get_english_chars(self):
    return set('abcdefghijklmnopqrstuvwxyz')

  def get_puncts(self):
    return self._get_all_puncts() & self.get_chars() 
  
  def get_stats(self):
    print('Number of words ', len(self.data.split()))
    print('Number of chars ', len(self.data))
      
  def get_ratio_of_arabic(self):
    count = 0 
    for char in self._get_all_alphabets():
      count += self.data.count(char)
    return count/len(self.data)
  
  def get_ratio_of_english(self):
    count = 0 
    for char in self._get_english_chars():
      count += self.data.lower().count(char)
    return count/len(self.data)
  
  def get_ratio_of_non_arabic(self):
    count = 0 
    for char in self.get_non_alphabets():
      count += self.data.lower().count(char)
    return count/len(self.data)
  
  def get_freq_of_chars(self):
    freq = Counter()
    for char in self.data:
      freq[char] += 1
    return freq
  
  def get_largest_word(self):
    largest_word = ''
    for word in self.data.split():
      if len(word) > len(largest_word):
        largest_word = word
    return largest_word
  
  def sample_random_sentence(self, size = 128):
    words = self.data.split()
    i = random.randint(0, len(words) - size)
    return (' ').join(words[i:i+size])

  def get_number_of_lines(self):
    return len(self.data.split('\n'))

  def sample_words_by_char(self, char, n = 10):
    occurs = re.findall('\w*'+char+'\w*', self.data)
    return np.random.choice(occurs, size = n)
  
  def get_top_largest_words(self, n = 10):
    freq = Counter()
    for word in self.data.split():
      freq[word] = len(word)
    return freq.most_common(n = n)
  
  def plot_top_largets_words(self, n = 100, log_scaled = False):
    data =  self.get_top_n_words(n = n)
    x = np.asarray(range(len(data)))
    if log_scaled == True:
      y = np.asarray([np.log(tp[1])for tp in data])
    else:
      y = np.asarray([tp[1] for tp in data])
    plt.plot(x,y)
    plt.xlabel('Data point')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()
  
  # https://stackabuse.com/python-for-nlp-working-with-facebook-fasttext-library/
  def plot_embeddings(self, words = ['سلام']):
    model_path = download_and_extract_model('https://bakrianoo.s3-us-west-2.amazonaws.com/aravec/full_grams_cbow_300_twitter.zip',
             'full_grams_cbow_300_twitter.zip')
    ft_model = gensim.models.Word2Vec.load(model_path)
    words = [clean_str(word).replace(" ", "_") for word in words]
    word_vectors = ft_model.wv[words]

    pca = PCA(n_components=2)

    p_comps = pca.fit_transform(word_vectors)
    word_names = [get_display(arabic_reshaper.reshape(word)) for word in words]

    plt.figure(figsize=(15, 10))
    plt.scatter(p_comps[:, 0], p_comps[:, 1], c='red')

    for word_names, x, y in zip(word_names, p_comps[:, 0], p_comps[:, 1]):
        plt.annotate(word_names, xy=(x+0.06, y+0.03), xytext=(0, 0), textcoords='offset points')