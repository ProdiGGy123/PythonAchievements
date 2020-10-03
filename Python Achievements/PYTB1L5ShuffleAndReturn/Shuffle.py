import random

original = "hallo"

def FunctionShuffler(original):
    randomised = ''.join(random.sample(original, len(original)))
    return str(randomised)
    

print(FunctionShuffler("madlynislief"))
print(FunctionShuffler("madlynisaardig"))
print(FunctionShuffler("jaydenisslordig"))