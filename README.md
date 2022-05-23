
**bayanat** is a simple library for gathering statistics about Arabic text.

## Examples

```python
from bayanat import Bayanat
dataset = Bayanat(path)
```
Functions

* `get_top_freq_words` retrieves n most frequent words.
* `get_top_freq_chars`  retrieves n most chars chars.
* `get_largest_word` get the largest word in the corpus. 
* `get_top_longest_words` get the top longest words in the corpus.
* `sample_words_by_char` sample words by character. 
* `sample_random_sentence` sample a sentence with a given size. 
* `get_ratio_of_non_arabic` show percentage of non Arabic chars. 
* `get_ratio_of_english` show percentage of English chars.
* `get_ratio_of_arabic` show percentage of Arabic chars.  
* `get_stats` print number of chars, words and lines. 
* `get_size_vocab` gets the number of unique words in the text.  
* `plot_top_freq_words` plots n most frequent words a bar graph. 
* `plot_top_freq_words` plots n most frequent chars a bar graph. 
* `plot_embeddings` given some words it plots the words using embeddings. This uses `AraVec` model. 
* `plot_word_cloud` plots the word cloud of a given text

## Demo 
Run directly on [Colab](https://colab.research.google.com/github/ARBML/bayanat/blob/main/demo.ipynb). 
## Contribution 
This is an open source project where we encourage contributions from the community. 

## License
[MIT](LICENSE) license. 

## Citation
```
@misc{bayanat2020,
  author = {Zaid Alyafeai and Maged Saeed},
  title = {bayanat: Statistics of Arabic Text.},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/ARBML/bayanat}}
}
```



