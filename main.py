from zad1 import clear_text
from zad2 import remove_stop_words
from zad3 import *


print(clear_text("""<div>Lorem IPSUM dolor 11 sit amet, consectetur :>
adipiscing elit.      Sed #texting eget :-) mattis sem. <a> Mauris #frasista 
egestas erat #tweetext quam, ut faucibus eros ;) 12 #frasier </a> congue :) et. 
In blandit,           mi eu porta lobortis, tortor nisl facilisis <b>leo</b> ;(,
at tristique 15        #frasistas augue risus       :< eu risus. ;< </div> """))


text_cleared = clear_text("""When I first met her she was very quiet.
    She remained quiet during the entire two hour long journey from Stony Brook
                                to New York.""")

print(remove_stop_words(text_cleared))

stemmer('programmer developed function for stemming words')
