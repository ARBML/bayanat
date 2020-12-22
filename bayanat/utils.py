from tqdm import tqdm
import urllib.request
import requests
from io import BytesIO
from zipfile import ZipFile
import os

# https://stackoverflow.com/a/53877507
class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_and_extract_model(url, output_path):
  file_name = 'full_grams_cbow_300_twitter.mdl'
  zip_file_name = 'full_grams_cbow_300_twitter.zip'

  if os.path.exists(file_name):
    return file_name

  if not os.path.exists(zip_file_name):
    with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=url.split('/')[-1]) as t: 
      urllib.request.urlretrieve(url, filename=output_path, 
                                                           reporthook=t.update_to)
  
  with ZipFile(zip_file_name) as zf:
      zf.extractall()
      
  return file_name

# https://github.com/bakrianoo/aravec/blob/79d7f0011ecd79e4f60d33c82514ee44dfa0ad92/utilities.py#L8
def clean_str(text):
    search = ["أ","إ","آ","ة","_","-","/",".","،"," و "," يا ",'"',"ـ","'","ى","\\",'\n', '\t','&quot;','?','؟','!']
    replace = ["ا","ا","ا","ه"," "," ","","",""," و"," يا","","","","ي","",' ', ' ',' ',' ? ',' ؟ ',' ! ']
    
    #remove tashkeel
    p_tashkeel = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
    text = re.sub(p_tashkeel,"", text)
    
    #remove longation
    p_longation = re.compile(r'(.)\1+')
    subst = r"\1\1"
    text = re.sub(p_longation, subst, text)
    
    text = text.replace('وو', 'و')
    text = text.replace('يي', 'ي')
    text = text.replace('اا', 'ا')
    
    for i in range(0, len(search)):
        text = text.replace(search[i], replace[i])
    
    #trim    
    text = text.strip()

    return text