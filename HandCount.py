from re import search

# tens digit --> card number
# ones digit --> card suit // CHaSeD order --> 1 - Clubs, 2 - Hearts, 3 - Spades, 4 - Diamonds
deck = [
    'c1', 'h1', 's1', 'd1',
    'c2', 'h2', 's2', 'd2',
    'c3', 'h3', 's3', 'd3',
    'c4', 'h4', 's4', 'd4',
    'c5', 'h5', 's5', 'd5',
    'c6', 'h6', 's6', 'd6',
    'c7', 'h7', 's7', 'd7',
    'c8', 'h8', 's8', 'd8',
    'c9', 'h9', 's9', 'd9',
    'c10', 'h10', 's10', 'd10',
    'c11', 'h11', 's11', 'd11',
    'c12', 'h12', 's12', 'd12',
    'c13', 'h13', 's13', 'd13',
]

# card1 = fromPHP
# card2 = fromPHP
# deck.remove(card1)
# deck.remove(card2)
# example:
card1 = "h1"
card2 = "h13"
deck.remove(card1)
deck.remove(card2)

flop1 = 0
flop2 = 0
flop3 = 0
turn = 0
river = 0

royalFlush = 0
straightFlush = 0
quads = 0
full = 0
flush = 0
straight = 0
trips = 0
twoPair = 0
pair = 0
high = 0
other = 0

for flop1 in deck:
    a = deck.index(flop1)
    deck.pop(a)
    for flop2 in deck:
        b = deck.index(flop2)
        deck.pop(b)
        for flop3 in deck:
            c = deck.index(flop3)
            deck.pop(c)
            for turn in deck:
                d = deck.index(turn)
                deck.pop(d)
                for river in deck:
                    hand = card1 + card2 + flop1 + flop2 + flop3 + turn + river
                    if search("c10" and "c11" and "c12" and "c13" and "c1", hand) or search("h10" and "h11" and "h12" and "h13" and "h1", hand) or search("s10" and "s11" and "s12" and "s13" and "s1", hand) or search("d10" and "d11" and "d12" and "d13" and "d1", hand):
                        royalFlush += 1
                    else:
                        other += 1
                deck.insert(d, turn)
            deck.insert(c, flop3)
        deck.insert(b, flop2)
    deck.insert(a, flop1)

print(royalFlush)
print(other)
