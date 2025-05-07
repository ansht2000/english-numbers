def words_to_numbers(input: str) -> int:
    digits = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9
    }

    teens = {
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16,
        "seventeen": 17, "eighteen": 18, "nineteen": 19
    }

    tens = {
        "twenty": 20, "thirty": 30, "forty": 40, "fourty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }

    scales = {
        "hundred": 100, "thousand": 1_000, "million": 1_000_000,
        "billion": 1_000_000_000, "trillion": 1_000_000_000_000,
        "quadrillion": 10**15, "quintillion": 10**18,
        "sextillion": 10**21, "septillion": 10**24,
        "octillion": 10**27, "nonillion": 10**30,
        "decillion": 10**33
    }
    words = input.replace(",", "").replace("-", " ").lower().split()
    words = [w for w in words if (w != "and" and w != "a")]
    # could be unecessary to parse lone scale numbers
    # TODO: figure out if you wanna keep this
    negative = False
    if words[0] in scales:
        words.insert(0, "one")
    if words[0] == "negative":
        negative = True
            
    print(words)
    current, total = 0, 0
    for word in words:
        if word in digits:
            current += digits[word]
        elif word in teens:
            current += teens[word]
        elif word in tens:
            current += tens[word]
        elif word == "hundred":
            current *= scales[word]
        elif word in scales:
            current *= scales[word]
            total += current
            current = 0
    if current != 0:
        total += current
        current = 0
    return -total if negative else total

    
def main() -> None:
    while True:
        num_in = input("Enter an english number written out in words: ")
        num = words_to_numbers(num_in)
        print(num)

if __name__ == "__main__":
    main()