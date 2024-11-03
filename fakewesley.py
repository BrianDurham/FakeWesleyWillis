import random

# Opening line used for every song generated
opening_line = "Once upon a time in "

# List of possible places to use in the opening line
places = [
    "Chicago", "New York City", "Hollywood", "Detroit", "San Francisco",
    "Miami", "Boston", "Austin", "Los Angeles", "Seattle"
]

# List of topics for song verses; each represents a unique "Wesley Willis" experience
topics = [
    "I rode a dolphin", "I went to the arcade", "I rocked the guitar",
    "I drove a bus", "I flew in a plane", "I jammed with a rock band",
    "I watched the police", "I saw a cool car", "I ran with my dog",
    "I punched a zebra"
]

# List of phrases to end each verse, mimicking the high-energy style of Willis's lyrics
phrases = [
    "It was a real jam", "The music was kicking", "The crowd was jumping",
    "I screamed like a rock star", "The bass was booming", "The guitar was loud",
    "I was headbanging hard", "The speakers were blasting", "It was a great show",
    "People were going wild"
]

# List of advertising slogans for song endings, like Wesley Willis's iconic outro style
slogans = [
    "Rock over London - Rock on Chicago",
    "Wheaties - Breakfast of Champions",
    "Folgers - The best part of waking up",
    "Pepsi - The choice of a new generation",
    "McDonald's - I'm lovin' it",
    "Coca-Cola - Always Coca-Cola",
    "Nike - Just do it",
    "Burger King - Have it your way",
    "Taco Bell - Think outside the bun",
    "Subway - Eat fresh"
]

def generate_song():
    """
    Generates a fake Wesley Willis song using random phrases and slogans.
    The song starts with a line about a random place, followed by four verses
    combining topics and phrases, and ends with an advertising slogan.
    
    Returns:
        str: A formatted string representing the generated song.
    """
    
    # Start with the opening line, selecting a random place
    song = opening_line + random.choice(places) + ".\n\n"

    # Add four verses to the song by combining a random topic and a random phrase
    for _ in range(4):
        song += random.choice(topics) + ".\n"
        song += random.choice(phrases) + ".\n\n"

    # End the song with a random advertising slogan
    song += random.choice(slogans) + "."
    
    return song

# Run the song generator and print the result
fake_song = generate_song()
print(fake_song)
