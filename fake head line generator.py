#import the random module

import random

#create subjects

subjects=[
    "Shahrukhan Khan",
    "Virat Kohali",
    "Nirmala Sitaraman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto riksa Driver Form Delhi"
]

actions=[
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things=[
    "at red fort",
    "in Mumbai local train",
    "a plate of smosa",
    "inside parliment",
    "at ganga ghat",
    "during IPL match",
    "at India Gate"
]

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place_or_thing=random.choice(places_or_things)

    headline=f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)
    user_input=input("\n Do you want another healine? (yes/no)").strip().lower()
    if  user_input=="no":
        break

print("\n Thanks for usng the Fake News Headline Generator. Have a fun day")