#We want to create a random subset of the VREED data, with the following information
#post ID, user ID, associated emotion, user's number of followers, number of reactions to post

import pandas as pd

vents = pd.read_csv("Vent/vents_metadata.csv.bz2")

df = pd.DataFrame(vents)
print(df.head())