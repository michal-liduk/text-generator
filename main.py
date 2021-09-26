from nltk import bigrams, Counter, trigrams
import random

filename = input()

with open(f"{filename}", "r", encoding="utf-8") as file:
    all_file = file.read()
    random_list = []
    big = list(bigrams(all_file.split()))
    trig = list(trigrams(all_file.split()))
    head_tail = {}
    endings = [".", "!", "?"]
    counter = 0
    model_trig = []
    for i in trig:
        head = " ".join(i[:2])
        tail = "".join(i[2])
        model_trig.append((head, tail))
        random_list.append(head)

    for head, tail in model_trig:
        head_tail.setdefault(head, []).append(tail)
    while counter < 10:
        random_word = random.choice(random_list)
        splitted_random_word = random_word.split()
        sentence = []
        if random_word[0].isupper() and splitted_random_word[0][-1] not in endings:
            sentence.append(splitted_random_word[0])
            sentence.append(splitted_random_word[1])
        else:
            continue
        while len(sentence) < 5 or sentence[-1][-1] not in endings:
            population_list = []
            weights_list = []
            current_tail = " ".join([sentence[-2], sentence[-1]])
            tails = Counter(head_tail[current_tail])
            for tail, count in tails.most_common(1):
                population_list.append(tail)
                weights_list.append(count)
                next_word = "".join(random.choices(population_list, weights=weights_list))
                sentence.append(next_word)
        counter += 1
        print(" ".join(sentence))
                # print(f"Tail: {tail}\tCount: {int(count)}")
