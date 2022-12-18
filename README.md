# anime_grid_generator
Generates random grid of anime shows from scraping MAL

![alt text](example.png)



----------------------------------------------------------------

Include animes you wish to search for inside _list_of_animes.txt_

Change parameters in __parameters.json__

----------------------------------------------------------------

pip install beautifulsoup4
| :---:   | 

----------------------------------------------------------------

Run __grid.py__ 

__anime.py__ is subrun if there are no images in ./ANIMEIMAGES.

Screenshot of grid saved in ./COLLAGE

----------------------------------------------------------------

Parameter		    						 |  Default Value | Action|Category
| :---:   | :---: | :---: | :---: |
RESIZE 	|		      							True		|						Downloaded images to be resized from original width and height.|	grid.py
DELETE_IMAGES |									True	|							Delete images from folder after making grid.|	grid.py
FULLSCREEN_WINDOW  		|					False	|							Make tkinter root Fullscreen.|	grid.py
CLOSE_WINDOW_AFTER_SEARCH	|			False	|							Quit window after 2s of showing the grid.|	grid.py
ROW_SIZE				|								5			|							Indicate row length.|	grid.py
COLUMN_SIZE 			|							5			|							Indicate column length.|	grid.py
GRID_SIZE 	|					120			|						Indicate width and height of image canvas resizing in pixels.|grid.py	
PADDING								|					50			|							Indicate window padding in pixels.|	grid.py
PADDING_BETWEEN_CELLS 	|				0			|							Indicate cell padding in pixels.|	grid.py
BACKGROUND_COLOR 					|	 	 "white"	|						Indicate window background color.|	grid.py
MAX_SEARCHES 					|	 	 50	|						Indicate amount of aprox images to download for picking randomly.|	anime.py


----------------------------------------------------------------
