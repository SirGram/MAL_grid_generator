import tkinter as tk
from PIL import Image,ImageTk,ImageGrab
import glob
import os
import random
import anime
import json
import anime_list

canvas_list = []
coord_list = []

def init_param():
    # PARAMETERS
    with open("parameters.json") as f:
        data = json.load(f)
        h = data["grid.py"]
        g = data["anime.py"]
        i= data["anime_list.py"]

        global BACKGROUND_COLOR
        global DELETE_IMAGES
        global PADDING
        global ROW_SIZE
        global COLUMN_SIZE
        global GRID_SIZE
        global PADDING_CELL
        global FULL_SCREEN_WINDOW

        BACKGROUND_COLOR = h["BACKGROUND_COLOR"]
        DELETE_IMAGES = h["DELETE_IMAGES"]
        PADDING = h["PADDING"]
        ROW_SIZE = h["ROW_SIZE"]
        COLUMN_SIZE = h["COLUMN_SIZE"]
        GRID_SIZE = h["GRID_SIZE"]
        PADDING_CELL = h["PADDING_CELL"]
        FULL_SCREEN_WINDOW = h["FULL_SCREEN_WINDOW"]

        anime.MAX_SEARCHES = g["MAX_SEARCHES"]

        anime_list.user=i["USER"]


def init():

    global window
    window = tk.Tk()
    window.config(background=BACKGROUND_COLOR, padx=PADDING, pady=PADDING)
    if FULL_SCREEN_WINDOW:
        window.attributes("-fullscreen", True)
    window.title("Grid Generator")
    global image_list
    image_list = list(glob.glob(os.path.join("./ANIMEIMAGES", '*.*')))
    random.shuffle(image_list)

def make_type():
    #2 resize types
    num=random.randint(0,1)
    if num==1:
        return "big"
    else:
        return "small"
def append_coord(i, j, type):
    coord_list.append((i, j))
    if type == "big":
        coord_list.append((i, j + 1))
        coord_list.append((i + 1, j))
        coord_list.append((i + 1, j + 1))
def check_coord(i,j,type):
    #Check taken coord
    if type == "big":
        if (i, j) not in coord_list and (i + 1, j + 1) not in coord_list and (i + 1, j) not in coord_list and (
                i, j + 1) not in coord_list and j != COLUMN_SIZE-1 and i != ROW_SIZE-1:
            print("big fit")
            return True
        else:
            print("big no fit")
            return False
    elif type=="small":
        if (i, j) not in coord_list :
            print("small fit")
            return True
        else:
            print("small no fit")
            return False
def screenshot():
    #Screenshot window
    box = (window.winfo_rootx(), window.winfo_rooty(), window.winfo_rootx() + window.winfo_width(),
            window.winfo_rooty() + window.winfo_height())
    screenshot = ImageGrab.grab(bbox=box)
    # Creates COLLAGE dir
    dir = os.path.join("./", "COLLAGE")
    if not os.path.exists(dir):
        os.mkdir(dir)
    screenshot.save(f"./COLLAGE/{random.randrange(1000)}.png")
    print("Image saved in ./COLLAGE ")
def delete_images():
    if DELETE_IMAGES:
        files = glob.glob("./ANIMEIMAGES/*")
        for f in files:
            os.remove(f)

def main():
    #Makes grid
    i=0
    while i<ROW_SIZE:
        j=0
        while j<COLUMN_SIZE:
            type=make_type()

            # Check coord
            if not check_coord(i,j,type):
                if type=="big":
                    continue
                if type=="small":
                    j+=1
                    continue

            item=image_list[-1]
            print(f"Check {item}")
            canvas=CreateLabel(item, i, j, type)
            canvas_list.append(canvas)
            append_coord(i,j, type)


            if type=="big":
                j+=2
            else:
                j+=1
            image_list.remove(item)
        i+=1
    window.after(1000, screenshot)
    window.mainloop()


class CreateLabel():
    #Separated Image canvases
    def __init__(self, item, row, column,type):
        self.image = Image.open(item)
        if type=="big":
            self.size=(GRID_SIZE*2,int(GRID_SIZE+(GRID_SIZE/2))*2)
            self.image = self.image.resize(size=self.size)
            self.img = ImageTk.PhotoImage(image=self.image)
            self.label = tk.Label(window, image=self.img, background=window["bg"],anchor="nw")
            self.label.grid(row=row, column=column, padx=PADDING_CELL,pady=PADDING_CELL, columnspan=2,rowspan=2)
        elif type=="small":
            self.size = (GRID_SIZE, int(GRID_SIZE  + (GRID_SIZE / 2) ))
            self.image = self.image.resize(size=self.size)
            self.img = ImageTk.PhotoImage(image=self.image)
            self.label = tk.Label(window, image=self.img, background=window["bg"], anchor="nw")
            self.label.grid(row=row, column=column, padx=PADDING_CELL, pady=PADDING_CELL, columnspan=1, rowspan=1)

if __name__=="__main__":
    init_param()
    #Search user MALanime list
    anime_list.init()
    anime_list.main()
    #Web scrape MAL
    anime.init()
    if len(os.listdir("./ANIMEIMAGES/"))==0:
        anime.main()
    #Order images into grid
    init()
    main()
    delete_images()

