from assignment import game,person,card,deck_of_cards
import unittest

test_case1=[
person(0,[(4,'h'),(5,'s'),(6,'j')]),
person(1,[(2,'h'),(5,'c'),(8,'j')]),
person(2,[(3,'c'),(7,'s'),(12,'j')]),
person(3,[(5,'h'),(10,'h'),(12,'j')])
]
test_case2=[
person(0,[(4,'h'),(5,'s'),(9,'j')]),
person(1,[(1,'h'),(5,'s'),(8,'j')]),
person(2,[(10,'h'),(10,'s'),(10,'j')]),
person(3,[(5,'h'),(5,'s'),(6,'j')])
]
test_case3=[
person(0,[(4,'j'),(5,'c'),(9,'j')]),
person(1,[(2,'h'),(5,'s'),(8,'h')]),
person(2,[(8,'c'),(10,'j'),(12,'j')]),
person(3,[(5,'h'),(5,'s'),(6,'c')])
]
test_case4=[
(9, 's'), (2, 's'), (12, 'j'), (13, 'h'),
 (2, 'h'), (1, 'j'),(4, 's'), (7, 'j'),
 (8, 'c'), (1, 's'), (6, 'j'), (13, 'c'), 
(5, 'c'), (1, 'h'), (10, 's'), (3, 'c'),
 (11, 'h'), (5, 'h'), (10, 'c'), 
(7, 'h'), (12, 'h'), (9, 'c'), (4, 'h'), (3, 'h'), (3, 'j'), (4, 'j'), (8, 'h'), (7, 'c'), (10, 'j'), 
(12, 'c'), (13, 's'), (7, 's'), (6, 'c'), (2, 'j'), (13, 'j'), (11, 's'), (3, 's'), (5, 's'), (8, 'j'), 
(11, 'j'), (6, 's'), (4, 'c'), (1, 'c'), (9, 'h'), (11, 'c'), (8, 's'), (10, 'h'), (9, 'j'), (12, 's'), 
(5, 'j'), (2, 'c'), (6, 'h')
]
output_4=[
    [(2,'h'),(8,'c'),(9,'s')],
    [(1,'j'),(1,'s'),(2,'s')],
    [(4,'s'),(6,'j'),(12,'j')],
    [(7,'j'),(13,'c'),(13,'h'),]
]
test_case5=[
    person(0,[(1,'j'),(5,'c'),(9,'j')]),
    person(1,[(1,'h'),(5,'s'),(8,'h')]),
    person(2,[(1,'c'),(10,'j'),(12,'j')]),
    person(3,[(1,'h'),(5,'s'),(6,'c')])
]

class test_game_class(unittest.TestCase):
    def setUp(self):
        pass

    def test_sequence_present_function(self):
        new_game=game()
        self.assertEqual(new_game.is_sequence_present(test_case1),(True,0))
        self.assertEqual(new_game.is_sequence_present(test_case2),(None,None))
    
    def test_three_numbers_same_function(self):
        new_game=game()
        self.assertEqual(new_game.is_three_numbers_same(test_case1),(None,None))
        self.assertEqual(new_game.is_three_numbers_same(test_case2),(True,2))

    def test_check_pair_cards_function(self):
        new_game=game()
        self.assertEqual(new_game.check_pair_cards(test_case1),(None,None))
        self.assertEqual(new_game.check_pair_cards(test_case2),(None,None))
        self.assertEqual(new_game.check_pair_cards(test_case3),(True,3))
    
    def test_check_top_card(self):
        new_game=game()
        self.assertEqual(new_game.check_top_card(test_case1),([2,3],None))
        self.assertEqual(new_game.check_top_card(test_case2),(None,1))
        self.assertEqual(new_game.check_top_card(test_case3),(None,2))
    
    def test_deal_cards_function(self):
        new_game=game()
        out=new_game.deal_cards(test_case4)
        output_list=[]
        for p in out:
            output_list.append(p.get_cards())
        self.assertEqual(output_list,output_4)

    def test_check_winner_function(self):
        new_game=game()
        self.assertEqual(new_game.check_winner(test_case1),0)
        self.assertEqual(new_game.check_winner(test_case2),2)
        self.assertEqual(new_game.check_winner(test_case3),3)
        self.assertEqual(new_game.check_winner(test_case5),None)

if __name__ == '__main__': 
    unittest.main()