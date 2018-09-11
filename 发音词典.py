import nltk
import re

# 发音的词典
entries = nltk.corpus.cmudict.entries()
print(len(entries)) # 133737
for entry in entries[39943:39951]:
    print(entry)
'''
('explorer', ['IH0', 'K', 'S', 'P', 'L', 'AO1', 'R', 'ER0'])
('explorers', ['IH0', 'K', 'S', 'P', 'L', 'AO1', 'R', 'ER0', 'Z'])
('explores', ['IH0', 'K', 'S', 'P', 'L', 'AO1', 'R', 'Z'])
('exploring', ['IH0', 'K', 'S', 'P', 'L', 'AO1', 'R', 'IH0', 'NG'])
('explosion', ['IH0', 'K', 'S', 'P', 'L', 'OW1', 'ZH', 'AH0', 'N'])
('explosions', ['IH0', 'K', 'S', 'P', 'L', 'OW1', 'ZH', 'AH0', 'N', 'Z'])
('explosive', ['IH0', 'K', 'S', 'P', 'L', 'OW1', 'S', 'IH0', 'V'])
('explosively', ['EH2', 'K', 'S', 'P', 'L', 'OW1', 'S', 'IH0', 'V', 'L', 'IY0'])
'''

for word, pron in entries:
    if len(pron) == 3:
        ph1, ph2, ph3 = pron
        if ph1 == 'P' and ph3 == 'T':
            print(word, ph2)
'''
pait EY1
pat AE1
...
put UH1
putt AH1
'''

syllable = ['N', 'IHO', 'K', 'S']
res = [word for word, pron in entries if pron[-4:] == syllable]
print(res)
'''[]'''
res = [w for w, pron in entries if pron[-1] == 'M' and w[-1] == 'n']
print(res)
'''['autumn', 'column', 'condemn', 'damn', 'goddamn', 'hymn', 'solemn']'''
res = sorted(set(w[:2] for w, pron in entries if pron[0] == 'N' and w[0] != 'n'))
print(res)
'''['gn', 'kn', 'mn', 'pn']'''

def stress(pron):
    return [char for phone in pron for char in phone if char.isdigit()]
res = [w for w, pron in entries if stress(pron) == ['0', '1', '0', '2', '0']]
print(res)
'''['abbreviated', 'abbreviated', 'abbreviating', ..., 'vocabulary', 'voluntarism']'''
res = [w for w, pron in entries if stress(pron) == ['0', '2', '0', '1', '0']]
print(res)
'''['abbreviation', 'abbreviations', 'abomination', ..., 'wakabayashi', 'yekaterinburg']'''

p3 = [(pron[0] + '-' + pron[2], word)
      for (word, pron) in entries
      if pron[0] == 'P' and len(pron) == 3]
cfd = nltk.ConditionalFreqDist(p3)
for template in cfd.conditions():
    if len(cfd[template]) > 10:
        words = cfd[template].keys()
        wordlist = ' '.join(words)
        print(template, wordlist[:70] + "...")
'''
P-P paap paape pap pape papp paup peep pep pip pipe pipp poop pop pope pop...
P-R paar pair par pare parr pear peer pier poor poore por pore porr pour...
P-K pac pack paek paik pak pake paque peak peake pech peck peek perc perk ...
P-S pace pass pasts peace pearse pease perce pers perse pesce piece piss p...
P-L pahl pail paille pal pale pall paul paule paull peal peale pearl pearl...
P-N paign pain paine pan pane pawn payne peine pen penh penn pin pine pinn...
P-Z pais paiz pao's pas pause paws pays paz peas pease pei's perz pez pies...
P-T pait pat pate patt peart peat peet peete pert pet pete pett piet piett...
P-CH patch pautsch peach perch petsch petsche piche piech pietsch pitch pit...
P-UW1 peru peugh pew plew plue prew pru prue prugh pshew pugh...
'''

prondict = nltk.corpus.cmudict.dict()
print(prondict['fire']) # [['F', 'AY1', 'ER0'], ['F', 'AY1', 'R']]
# print(prondict['blog']) # KeyError: 'blog'
prondict['blog'] = [['B', 'L', 'AA1', 'G']]
print(prondict['blog']) # [['B', 'L', 'AA1', 'G']]

text = ['natural', 'language', 'processing']
res = [ph for w in text for ph in prondict[w][0]]
print(res)
'''
['N', 'AE1', 'CH', 'ER0', 'AH0', 'L', 'L', 'AE1', 'NG', 'G', 'W', 'AH0', 'JH', 'P', 
'R', 'AA1', 'S', 'EH0', 'S', 'IH0', 'NG']
'''