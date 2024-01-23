import random

def generate_iq_and_message():
    # Generate a random IQ score between 70 and 130
    iq_score = random.randint(70, 130)

    # Determine the message based on the IQ score
    if iq_score < 85:
        message = "Below average intelligence."
    elif 85 <= iq_score < 115:
        message = "Average intelligence."
    elif 115 <= iq_score < 130:
        message = "Above average intelligence."
    else:
        message = "Highly intelligent."

    return iq_score, message
