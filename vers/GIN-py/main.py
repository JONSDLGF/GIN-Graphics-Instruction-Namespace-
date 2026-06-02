# py main

import sdl2
import sdl2.ext

# vars
class Win:
    window = None
    title  = ""
    w      = 0
    h      = 0

def Win_new(title,w,h):
    Win.title=title
    Win.w=w
    Win.h=h

def Win_start():
    sdl2.ext.init()

    Win.window = sdl2.ext.Window(
        Win.title,
        size=(Win.w, Win.h)
    )

    Win.window.show()