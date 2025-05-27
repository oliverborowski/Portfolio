#OLIVERBOROWSKI
#INIT

import random

#FUNCTIONS

def create_deck():
    """Creates a deck of 52 cards and shuffles it."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [{'suit': suit, 'value': value} for suit in suits for value in values]
    random.shuffle(deck)
    return deck



def calculate_hand_score(hand):
    score = 0
    aces = 0

    for card in hand:
        value = card['value']
        if value in ['J', 'Q', 'K']:
            score += 10
        elif value == 'A':
            aces += 1
            score += 11
        else:
            score += int(value)


    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score

def display_hand(hand, player_name):

    print("{player_name}'s Hand:")
    for card in hand:
        print(f"{card['value']} of {card['suit']}")
    print(f"Score: {calculate_hand_score(hand)}\n")

# Function to play the blackjack game
def play_blackjack():
    """Main function to run the Blackjack game."""
    print("Welcome to Blackjack!\n")

    # Initialize deck and hands
    while True:
        deck = create_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        # Display initial hands
        display_hand(player_hand, "Player")
        print("Dealer's Hand:")
        print(f"{dealer_hand[0]['value']} of {dealer_hand[0]['suit']}\n[Hidden Card]\n")

        # Player's turn
        while calculate_hand_score(player_hand) < 21:
            action = input("Would you like to (h)it or (s)tand? ").lower()
            if action == 'h':
                player_hand.append(deck.pop())
                display_hand(player_hand, "Player")
            elif action == 's':
                break
            else:
                print("Invalid input. Please choose 'h' to hit or 's' to stand.")

        # Dealer's turn (dealer must hit if score < 17)
        while calculate_hand_score(dealer_hand) < 17:
            dealer_hand.append(deck.pop())

        # Display final hands
        display_hand(dealer_hand, "Dealer")

        # Determine the winner
        player_score = calculate_hand_score(player_hand)
        dealer_score = calculate_hand_score(dealer_hand)

        print("Final Scores:")
        print(f"Player: {player_score}")
        print(f"Dealer: {dealer_score}")

        if player_score > 21:
            print("Player busted! Dealer wins.")
        elif dealer_score > 21:
            print("Dealer busted! Player wins.")
        elif player_score > dealer_score:
            print("Player wins!")
        elif dealer_score > player_score:
            print("Dealer wins!")
        else:
            print("It's a tie!")

        again = input("Would you like to play again? (yes/no): ").lower()
        if again == "yes":
            print("Good luck!")
            deck.clear()
        else:
            print("Thank you for playing blackjack!")
            break

#MAIN


play_blackjack()
