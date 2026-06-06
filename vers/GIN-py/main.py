# py main

import sdl2
import sdl2.ext

# vars
class Win:
    window = None
    title  = ""
    w      = 0
    h      = 0
    GAFICS = {
        "CAP":[],
        "ASS":{
            "MOD":{},
            "IMG":{},
            "CAM":{}
        }
    }

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

def Win_clear():
    pass #; clear

def Win_render():
    for cap in Win.GAFICS["CAP"]:
        if not cap[0]:continue
        for inst in cap[2]:
            match cap[1]:
                case 0: #; ui layer
                    if inst[0] == "T": pass #; render text
                case 1: #; 2D
                    pass #; render image
                case 3: #; 3D
                    pass #; render 3D scene

class GApi:
    @staticmethod
    def new_img(obj):
        imgs = Win.GAFICS["ASS"]["IMG"]

        idx = 0
        while idx in imgs:
            idx += 1

        imgs[idx] = obj
        return idx
    @staticmethod
    def del_img(idx):
        Win.GAFICS["ASS"]["IMG"].pop(idx, None)