import random
class card:
    def __init__(self,val,card_type):
        self.val=val
        self.card_type=card_type
    def get_val(self):
        return self.val
    def get_card_type(self):
        return self.card_type

class deck_of_cards:
    card_types=['h','c','j','s']
    def __init__(self):
        temp=[]
        tuples=[]
        for card_type in deck_of_cards.card_types:
            for num in range(1,14):
                new_card=card(num,card_type)
                temp.append(new_card)
                tuples.append((num,card_type))
        self.cards=temp
        self.tuples=tuples
    def get_deck_as_card_class(self):
        return self.cards
    def get_card_as_tuples(self):
        return self.tuples

class person:
    def __init__(self,num,recieved_cards):
        self.num=num
        self.recieved_cards=recieved_cards
    def get_cards(self):
        return self.recieved_cards
    def get_person_num(self):
        return self.num

class game:
    
    def __init__(self):
        self.winner="None"
        self.player_count=4
        self.card_deck=[]
    def simulate_new_game(self):
        #create a deck of cards
        card_deck_obj=deck_of_cards()
        #get the 52 cards
        card_deck=card_deck_obj.get_card_as_tuples()
        #shuffle the cards
        random.shuffle(card_deck)
        self.card_deck=card_deck
        #find the winner and return
        return self.get_winner(card_deck)
    
    def get_winner(self,cards):
        dealt_cards=self.deal_cards(cards)
        return self.check_winner(dealt_cards)
    
    def deal_cards(self,cards):
        #create a list to store person object
        cards_with_person=[]
        no_of_players=self.player_count
        for i in range(no_of_players):
            #while dealing cards with 4, each person gets a card after 3 deals 
            card_indices_for_this_person=[j for j in range(i,12,no_of_players)]
            #create a dictionary to store the card
            cards_for_this_person=[(cards[k][0],cards[k][1]) for k in card_indices_for_this_person]
            #sort the list
            cards_for_this_person.sort()
            # print(cards_for_this_person)
            #create a person with person number and recieved cards
            p1=person(i,cards_for_this_person)
            #append p1 to the list
            cards_with_person.append(p1)
        #return the cards with 4 persons
        return cards_with_person
    
    def check_winner(self,dealt_cards):
        check1,winner=self.is_three_numbers_same(dealt_cards)
        if check1!=None:
            return winner
        check2,winner=self.is_sequence_present(dealt_cards)
        if check2!=None:
            return winner
        check3,winner=self.check_pair_cards(dealt_cards)
        if check3!=None:
            return winner
        tied_players,check4=self.check_top_card(dealt_cards)
        if tied_players==None and check4!=None:
            return check4
        elif tied_players!=None:
            check4,winner=self.random_pick(tied_players)
            if check4:
                return winner
        return None
    
    def is_three_numbers_same(self,cards_with_person):
        count=0
        winner=None
        for i in range(len(cards_with_person)):
            cards=cards_with_person[i].get_cards()
            if cards[0][0]==cards[1][0] and cards[1][0]==cards[2][0]:
                count+=1
                winner=i
        if count!=1:
            return None,None
        return True,winner
    
    def is_sequence_present(self,cards_with_person):
        count=0
        winner=None
        for i in range(len(cards_with_person)):
            cards=cards_with_person[i].get_cards()
            # print(cards)
            if cards[0][0]==cards[1][0]-1 and cards[1][0]==cards[2][0]-1:
                count+=1
                winner=i
        # print(count)
        if count!=1:
            return None,None
        return True,winner
    
    def check_pair_cards(self,cards_with_person):
        count=0
        winner=None
        for i in range(len(cards_with_person)):
            cards=cards_with_person[i].get_cards()
            if cards[0][0]==cards[1][0] or cards[1][0]==cards[2][0]:
                count+=1
                winner=i
        if count!=1:
            return None,None
        return True,winner
    
    def check_top_card(self,cards_with_person):
        #List to store the top card of each player
        top_cards=[]
        #since a is top card in face off let's change the value of a to 13
        max_top_card_value=0
        for i in range(len(cards_with_person)):
            cards=cards_with_person[i].get_cards()
            if cards[0][0]==1 or cards[1][0]==1 or cards[2][0]==1:
                max_val=13
                top_cards.append(max_val)
                max_top_card_value=max(max_top_card_value,max_val)
            else:
                max_val=max([cards[0][0],cards[1][0],cards[2][0]])
                top_cards.append(max_val)
                max_top_card_value=max(max_top_card_value,max_val)
        winner=None
        tied_players=[]
        for i in range(len(top_cards)):
            if top_cards[i]==max_top_card_value:
                tied_players.append(i)
                winner=i
        count=len(tied_players)
        if count>1:
            return tied_players,None
        return None,winner

    def random_pick(self,tied_players):
        #since 12 cards have been dealt already, we have to start picking from 13th card from deck
        #print(tied_players)
        card_deck=self.card_deck
        tied_player_count=len(tied_players)
        for i in range(12,52,tied_player_count):
            max_value=0
            picked_cards=[]
            if i+tied_player_count>=52:
                break
            for j in range(i,i+tied_player_count):
                card_1=card_deck[j][0]
                if card_1==1:
                    card_1=13
                picked_cards.append(card_1)
                max_value=max(max_value,card_1)
            count=0
            winner=None
            for k in range(len(picked_cards)):
                if picked_cards[k]==max_value:
                    count+=1
                    winner=tied_players[k]
            if count==1:
                 return True,winner
        return False,None
    
    