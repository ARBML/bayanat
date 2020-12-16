from collections import Counter
import re
import numpy as np
import random 

class bayanat:

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

  def _get_all_puncts():
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
