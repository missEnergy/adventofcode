from aocd import get_data, submit

year, day = 2023, 7


def count_cards(hand: str):
    count_array = []
    for i in range(1, 10):
        count_array.append(hand.count(str(i)))
    for i in ["T", "J", "Q", "K", "A"]:
        count_array.append(hand.count(str(i)))
    return count_array


def determine_type(count_array: str):
    if 5 in count_array:
        return 7  # 5 of a kind
    elif 4 in count_array:
        return 6  # 4 of a kind
    elif 3 in count_array and 2 in count_array:
        return 5  # full house
    elif 3 in count_array:
        return 4  # 3 of a kind
    elif len([i for i in count_array if i > 1]) == 2:
        return 3  # 2 pair
    elif 2 in count_array:
        return 2  # 1 pair
    else:
        return 1  # high card

# part A
data = get_data(year=year, day=day).split("\n")
hands = []
for line in data:
    hand = line.split(" ")
    count_array = count_cards(hand[0])
    type = determine_type(count_array)
    item = {
        "cards": hand[0],
        "bid": int(hand[1]),
        "count_array": count_array,
        "type": type
    }
    hands.append(item)

def better_hand(hand1, hand2):
    hand1_cards_subst = (
        hand1['cards']
        .replace("T", "B")
        .replace("J", "C")
        .replace("Q", "D")
        .replace("K", "E")
        .replace("A", "F")
    )
    hand2_cards_subst = (
        hand2['cards']
        .replace("T", "B")
        .replace("J", "C")
        .replace("Q", "D")
        .replace("K", "E")
        .replace("A", "F")
    )

    if not hand1['type'] == hand2['type']:
        return hand1['type'] > hand2['type']
    elif not hand1_cards_subst[0] == hand2_cards_subst[0]:
        return hand1_cards_subst[0] > hand2_cards_subst[0]
    elif not hand1_cards_subst[1] == hand2_cards_subst[1]:
        return hand1_cards_subst[1] > hand2_cards_subst[1]
    elif not hand1_cards_subst[2] == hand2_cards_subst[2]:
        return hand1_cards_subst[2] > hand2_cards_subst[2]
    elif not hand1_cards_subst[3] == hand2_cards_subst[3]:
        return hand1_cards_subst[3] > hand2_cards_subst[3]
    elif not hand1_cards_subst[4] == hand2_cards_subst[4]:
        return hand1_cards_subst[4] > hand2_cards_subst[4]
    else:
        raise Exception('same hand!')



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):

            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found
            # is greater than the adjacent element
            if better_hand(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


bubble_sort(hands)

# for i in hands:
#     print(i)

answer_a = 0
for idx, hand in enumerate(hands):
    rank = idx + 1
    answer_a = answer_a + rank * hand['bid']

print(answer_a)
# submit(answer_a, part="a", day=day, year=year)

# part B
def count_cards(hand: str):
    count_array = []
    for i in range(1, 10):
        count_array.append(hand.count(str(i)))
    for i in ["T", "J", "Q", "K", "A"]:
        count_array.append(hand.count(str(i)))
    return count_array


def determine_type(count_array: str):
    if 5 in count_array:
        type = 7  # 5 of a kind
    elif 4 in count_array:
        type = 6  # 4 of a kind
        if count_array[10] == 1 or count_array[10] == 4:
            type = 7
    elif 3 in count_array and 2 in count_array:
        type = 5  # full house
        if count_array[10] == 2 or count_array[10] == 3:
            type = 7
    elif 3 in count_array:
        type = 4  # 3 of a kind
        if count_array[10] == 1 or count_array[10] == 3:
            type = 6
    elif len([i for i in count_array if i > 1]) == 2:
        type = 3  # 2 pair
        if count_array[10] == 1:
            type = 5
        elif count_array[10] == 2:
            type = 6
    elif 2 in count_array:
        type = 2  # 1 pair
        if count_array[10] == 1 or count_array[10] == 2:
            type = 4
    else:
        type = 1  # high card
        if count_array[10] == 1:
            type = 2
    return type

# part B
data = get_data(year=year, day=day).split("\n")
hands = []
for line in data:
    hand = line.split(" ")
    count_array = count_cards(hand[0])
    type = determine_type(count_array)
    item = {
        "cards": hand[0],
        "bid": int(hand[1]),
        "count_array": count_array,
        "type": type
    }
    hands.append(item)

def better_hand(hand1, hand2):
    hand1_cards_subst = (
        hand1['cards']
        .replace("T", "B")
        .replace("J", "0")
        .replace("Q", "D")
        .replace("K", "E")
        .replace("A", "F")
    )
    hand2_cards_subst = (
        hand2['cards']
        .replace("T", "B")
        .replace("J", "0")
        .replace("Q", "D")
        .replace("K", "E")
        .replace("A", "F")
    )

    if not hand1['type'] == hand2['type']:
        return hand1['type'] > hand2['type']
    elif not hand1_cards_subst[0] == hand2_cards_subst[0]:
        return hand1_cards_subst[0] > hand2_cards_subst[0]
    elif not hand1_cards_subst[1] == hand2_cards_subst[1]:
        return hand1_cards_subst[1] > hand2_cards_subst[1]
    elif not hand1_cards_subst[2] == hand2_cards_subst[2]:
        return hand1_cards_subst[2] > hand2_cards_subst[2]
    elif not hand1_cards_subst[3] == hand2_cards_subst[3]:
        return hand1_cards_subst[3] > hand2_cards_subst[3]
    elif not hand1_cards_subst[4] == hand2_cards_subst[4]:
        return hand1_cards_subst[4] > hand2_cards_subst[4]
    else:
        raise Exception('same hand!')



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):

            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found
            # is greater than the adjacent element
            if better_hand(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


bubble_sort(hands)

for i in hands:
    print(i)

answer_b = 0
for idx, hand in enumerate(hands):
    rank = idx + 1
    answer_b = answer_b + rank * hand['bid']

print(answer_b)
# submit(answer_b, part="b", day=day, year=year)