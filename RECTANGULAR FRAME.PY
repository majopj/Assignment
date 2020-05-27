print("RECTANGULAR FRAME")
print()
def word_frame(words):
    size = max(len(x) for x in words)
    print('*' * (size + 4))
    for x in words:
        print('* {:{}} *'.format(x,size))
    print('*' * (size + 4))
word_frame(["Hello", "World", "in", "a", "frame"])