from zad1a import delete_numbers
from zad1b import delete_html
from zad1c import delete_punctuation_marks
from zad2 import extract_hashtags
from zad3 import extract_emoticons


print(delete_numbers('Dzisiaj mamy 4 stopnie na plusie, 1 marca 2022 roku'))

print(delete_html("""<div><h2>Header</h2> <p>article<b>
strong text</b> <a href="">link</a> </p></div> """))

print(delete_punctuation_marks("""Lorem ipsum dolor sit amet, consectetur;
 adipiscing elit. Sed eget mattis sem. Mauris egestas erat quam, ut faucibus
  eros congue et. In
blandit, mi eu porta; lobortis, tortor nisl facilisis leo, at tristique augue
 risus eu risus. """))

extract_hashtags("""Lorem ipsum dolor
sit amet, consectetur adipiscing elit. Sed #texting eget mattis sem. 
Mauris #frasista
egestas erat #tweetext quam, ut faucibus eros #frasier congue et. In blandit,
 mi eu porta
lobortis, tortor nisl facilisis leo, at tristique #frasistas augue risus
 eu risus.""")

extract_emoticons("""Lorem ipsum dolor
 sit amet, consectetur :> adipiscing elit. Sed #texting eget :-) mattis sem.
  Mauris #frasista
egestas erat #tweetext quam, ut faucibus eros ;) #frasier congue et. :)
 In blandit, mi eu porta
lobortis, tortor nisl facilisis leo ;(, at tristique #frasistas augue risus
 :< eu risus. ;< """)
