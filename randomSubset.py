#We want to create a random subset of the VREED data, with the following information
#post ID, user ID, associated emotion, user's number of followers, number of reactions to post

import pandas as pd

vents = pd.read_csv("Vent/vents_metadata.csv.bz2")
emotions = pd.read_csv("Vent/emotions.csv")

df = pd.DataFrame(vents)

ventsMerg = vents.merge(emotions, left_on='emotion_id', right_on='id')

ventswithEmotions = ventsMerg[['id', 'user_id', 'name', 'reactions']]
ventswithEmotions = ventswithEmotions.rename(columns={'id': 'post_id', 'name': 'emotion'})

print(ventswithEmotions.head())