# We create a language called Giraffe
# such that each vowel is mapped to g
# ex: dog -> dgg, dune -> dgng

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        # if letter in "AEIOUaeiou":
            # We can loop through and check against a set of characters.
        #    translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))

