SNAKE = r""" 
  \
   \    __
    \  {oo}
       (__)\
         ^ \\
           _\\__
          (_____)_
         (________)Ooo
"""

def bubble(message):
    bubble_length = len(message) + 2
    return f"""
{"_" * bubble_length}
( {message} )
{"‾" * bubble_length}"""

def say(message):
    print(bubble(message),end='')
    print(SNAKE)


#if __name__ == "__main__":
    #say("Sleep right, little man-cub")