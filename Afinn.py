#make sure to install afinn before proceeding further

from afinn import Afinn

afinn = Afinn()

def get_sentiment(text):
    score = afinn.score(text)
    if score > 0:
        return 'positive'
    elif score < 0:
        return 'negative'
    else:
        return 'neutral'

new_statements = [
    "I am very happy with the service.",
    "This is the worst experience ever.",
    "I am confident",
]

for statement in new_statements:
    sentiment = get_sentiment(statement)
    print(f"statement: {statement} | sentiment: {sentiment}")

