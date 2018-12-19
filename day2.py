

def InventoryManagementSystemChecksum():
    filename = 'input_day2.txt'
    words_two = 0
    words_three = 0
    with open(filename, 'r') as input:
        for line in input:
            word = line.split()[0]
            found_two = False
            found_three = False
            for letter in word:
                c = word.count(letter)
                if c == 2:
                    found_two = True
                elif c == 3:
                    found_three = True

            if found_two:
                words_two += 1
            if found_three:
                words_three += 1

    print('Number of words with two {} and with three {}'.format(words_two, words_three))
    print('This gives a checksum of {}'.format(words_two*words_three))


def InventoryManagementSystemDiffByOne():
    filename = 'input_day2.txt'
    words = []
    similar_id = []
    with open(filename, 'r') as input:
        for line in input:
            word = line.split()[0]
            words.append(word)

    for i in range(len(words)):
        for j in range(i, len(words)):
            s1 = words[i]
            s2 = words[j]

            diff = sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))
            if diff == 1:
                similar_id.append((i,j))

    print(similar_id)
    s1 = words[similar_id[0][0] ]
    s2 = words[similar_id[0][1] ]
    print(s1, s2)
    similar_letters = ''
    for ch1, ch2 in zip(s1, s2):
        if ch1 == ch2:
            similar_letters += ch1

    print('They have letters {} in common'.format(similar_letters))