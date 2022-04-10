import string
# Nice. I would like to implement this from scratch
from collections import Counter # counter
import re # string manipulation

def word_count_engine(document):
  
  document = re.sub('[!,.,?,!,/,\',:,;,\,]',"",document.lower()) # Nice!
  new_document = document.split()
  new_document.reverse()
  counter = Counter(new_document)
  #print(' '.join(new_document))
  word_count = [[k,counter[k]] for k in set(counter)]
  for i, k in enumerate(word_count):
    idx = 0
    for j in range(len(new_document)):
      if new_document[j] == k[0]:
         idx = j
    word_count[i].append(idx)
  #print(word_count)
  #print(list(map(lambda i: (i[0], i[1], i[2]), word_count)))
  word_count.sort(key = lambda i: (i[1],i[2]),reverse = True)
  word_count_engine = [[word,str(count)] for word,count,_ in word_count]
  #convert = json.dumps(word_count_engine) # Nice
  # From my tests I think that it isn't need to sort

  # My output: [["graco", "2"], ["ola", "1"], ["mundo", "1"]]
  #return word_count_engine 
  # Nice! Thanks
  # Sorry for don't pass the solution of time planner
  # I can send you a email with this
   
  # I tested with json.dumps and it worked
  return word_count_engine
  # That was my first thought, but it doesnt work the way we want, it leaves the single quotes on the end   '"practice"', possibly beacause of the f'string
  # Can it be in this manner?
  # Hum...Ok

doc1 = "Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"
doc2 = "To be, or not to be, that is the question:"
doc3 = "Look If you had One shot, Or one opportunity, To seize everything you ever wanted, In one moment, Would you capture it, Or just let it slip?"
doc4 = "I have failed over and over and over again in my life and that is why I succeed."
#word_count_engine(doc4)
print(word_count_engine(doc2))
#print(word_count_engine(doc2))
