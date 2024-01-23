import random

def love_or_hate():
    intensity = random.randint(1, 100)  # Random intensity between 1 and 100

    love_emojis = ["❤️", "😍", "🥰", "💖", "💕", "😘", "💑", "💞", "💓", "💌"]
    hate_emojis = ["💔", "😠", "👿", "💢", "😡", "🖤", "👎", "💀", "🔥", "🤬"]

    if random.choice([True, False]):  # Randomly choosing between love and hate
        emotion = "love"
        emoji = random.choice(love_emojis)
    else:
        emotion = "hate"
        emoji = random.choice(hate_emojis)

    return f"You {emotion} me {intensity}% {emoji}"

