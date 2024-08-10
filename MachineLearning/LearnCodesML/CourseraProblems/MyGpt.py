from transformers import pipeline

# Load a pre-trained language model pipeline
generator = pipeline('text-generation', model='gpt2')

# Define favorite items
favorite_game = "Cricket"
favorite_movie = "Gladiator"
favorite_food = "beef kebab"

# Generate a response
response = generator(f"""
My favorite game and movie are {favorite_game} and {favorite_movie}, and I love to watch it over my favorite food {favorite_food}.
What songs would you recommend based on my likes?
""", max_length=150)

# Print the response
print(response[0]['generated_text'])
