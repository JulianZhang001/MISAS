import pandas as pd

# Create the dataset
data = {
    'Participant ID': [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3],
    'Domain': ['Communication', 'Communication', 'Communication', 'Communication', 'Communication', 'Communication',
               'Daily Living Skills', 'Daily Living Skills', 'Daily Living Skills', 'Daily Living Skills', 'Daily Living Skills', 'Daily Living Skills',
               'Socialization', 'Socialization', 'Socialization', 'Socialization', 'Socialization', 'Socialization'],
    'Subdomain': ['Receptive', 'Receptive', 'Expressive', 'Expressive', 'Written', 'Written',
                  'Personal (Self-care)', 'Personal (Self-care)', 'Home (Home Management)', 'Home (Home Management)', 'Community (Community Use)', 'Community (Community Use)',
                  'Interpersonal Relationships', 'Interpersonal Relationships', 'Leisure/Play', 'Leisure/Play', 'Leisure/Play', 'Leisure/Play'],
    'Scenario': ['Going to and from School', 'Going to and from School', 'I Want to Go to the Bathroom', 'I Want to Go to the Bathroom', 'Reading and Writing Class', 'Reading and Writing Class',
                 'Morning Check-in at School', 'Morning Check-in at School', 'Packing My Bag for School', 'Packing My Bag for School', 'Taking the Light Rail', 'Taking the Light Rail',
                 "Let's Make a Friend", "Let's Make a Friend", 'At the Playground', 'At the Playground', 'At the Playground', 'At the Playground'],
    'Utterance': ["I'm ready to go to school now.", "It's time to come home from school.", "Excuse me, I need to go to the bathroom.", "Can you help me find the bathroom?", "I love reading and writing class!", "I'm going to read this book during our reading time.",
                  "Good morning, teacher! I'm here for the morning check-in.", "I feel well today.", "I'm going to pack my schoolbag now.", "Can you help me check if I have everything I need for school?", "Let's take the light rail to school today.", "I need to know how to get on and off the light rail safely.",
                  "Hi, can I be your friend?", "I'm looking for someone to play with.", "I want to play on the swings at the playground.", "Can we play tag at the playground?", "I want to play on the swings at the playground.", "Can we play tag at the playground."]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the dataset
print(df)

# Analyze the dataset, for example, calculate the number of participants in each subdomain
participant_count = df.groupby('Subdomain')['Participant ID'].nunique()
print("\nNumber of participants grouped by Subdomain:\n", participant_count)