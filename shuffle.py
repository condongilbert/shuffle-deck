import random
import matplotlib.pyplot as plt

# Define the deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

def shuffle_deck(deck):
    shuffled = deck.copy()
    random.shuffle(shuffled)
    return shuffled

def visualize_deck(deck, title='Shuffled Deck'):
    plt.figure(figsize=(14, 4))
    plt.xlim(-1, 13)
    plt.ylim(-1, 4)
    plt.axis('off')
    
    for i, card in enumerate(deck):
        x = i % 13
        y = 3 - (i // 13)  # Invert y to have Spades at bottom
        plt.text(x, y, card, fontsize=8, ha='center', va='center',
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'))

    plt.title(title, fontsize=14)
    plt.show()

# Shuffle and visualize
shuffled_deck = shuffle_deck(deck)
visualize_deck(shuffled_deck)