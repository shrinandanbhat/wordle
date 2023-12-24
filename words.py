import random

words = """
light
heart
ocean
dance
dreams
music
stars
peace
trees
brush
laugh
space
color
grace
bloom
quiet
bliss
smile
warmth
float
carve
glide
blend
trust
unity
spark
flame
pulse
dream
faith
seren
magic
water
cloud
charm
carve
pulse
faith
peace
"""

wordslist = words.split('\n')
outputwordslist = []

for i in range(len(wordslist)-1):

    selected = wordslist[i]

    if "".join(dict.fromkeys(selected)) == selected and len(selected) == 5:
    

        outputwordslist.append(selected)

def get_word():
    return random.choice(outputwordslist)
