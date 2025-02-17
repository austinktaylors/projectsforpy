#if we dont know the amount we want to loop, use while, if we have a number in mind, use for.
# game loop//game number will be while loops
import p1_random as p1
rng = p1.P1Random()

#we set some variables to 0 because these don't loop/reset.
game_num = 0
player_win = 0
dealer_win = 0
game_ties = 0
in_progress = True

while in_progress:
    #new game loop
    game_num += 1
    print(f"START GAME #{game_num}")
    card = rng.next_int(13) + 1 #(0,12)
    if card <=10:
        hand = card
    else:
        hand = 10
    print(f"Your card is a {card}!")
    print(f"Your hand is: {hand}\n")
    while True:
        choice = int(input("Please enter an integer value between 1 and 4.\n\n1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n\nChoose an option: "))
        if choice == 1:
            card = rng.next_int(13) + 1
            if card == 1:
                hand += 1
                print(f"Your card is a ACE!")
                print(f"Your hand is {hand}")
            elif card == 2-10:
                print(f"Your card is a {card}!")
                print(f"Your hand is {hand}")
            elif card == 11:
                hand += 10
                print(f"Your card is a JACK!")
                print(f"Your hand is {hand}")
            elif card == 12:
                hand += 10
                print(f"Your card is a QUEEN!")
                print(f"Your hand is {hand}")
            elif card == 13:
                hand += 10
                print(f"Your card is a KING!")
                print(f"Your hand is {hand}")
        elif choice == 2:
            #dealer's draw
            dealer_hand = rng.next_int(11) + 16
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {hand}")
            if dealer_hand == 21:
                dealer_win += 1
                print("Dealer Wins")
                break
            elif dealer_hand > 21:
                player_win += 1
                print("You win!")
                break
            elif hand == dealer_hand:
                game_ties += 1
                print("It's a tie")
                break
            elif hand > dealer_hand:
                player_win += 1
                print("You win!")
                break
            elif dealer_hand > hand:
                dealer_win += 1
                print("Dealer Wins")
                break

            if hand ==  21:
                player_win += 1
                print("BLACKJACK! You win!")
                break
            elif hand > 21:
                dealer_win += 1
                print("You exceeded 21! You lose.")
                break

        elif choice == 3:
            #print stats
            if game_num == 0:
                print("You haven't played any games!")
                break
            else:
                percentage_won = (player_win / game_num) * 100
            print(f"Number of Player wins: {player_win}")
            print(f"Number of Dealer wins: {dealer_win}")
            print(f"Number of tie games: {game_ties}")
            print(f"Total # of games played is: {game_num}")
            print(f"Percentage of Player wins: {percentage_won:.1f}")


        elif choice == 4:
            #exit program
            in_progress = False
            break
        else:
            print("Invalid input!")




# def game_number():
# def player_win():
# def dealer_win():
# def current_card():
# def total_card_val():
# def games_tied():