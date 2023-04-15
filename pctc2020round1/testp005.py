poem = "wibble wobble wibble wobble jelly on the plate"

word = input()
n = int(input())

words = poem.split()

index = words.index(word)

print(" ".join(words[index+1:index+1+n]))
