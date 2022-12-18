# anime_grid_generator
Creates a random grid of anime banners from your MY ANIME LIST account.

![alt text](example.png)

----------------------------------------------------------------

pip install bs4
| :---:   | 

----------------------------------------------------------------

Change parameters and MAL user in __parameters.json__

----------------------------------------------------------------

Run __main.py__ 

__anime_list.py__ and __anime.py__is subrun. 

Screenshot of grid saved in ./COLLAGE

----------------------------------------------------------------

Parameter		    						 |  Default Value | Action|Category
| :---:   | :---: | :---: | :---: |
MAX SEARCHES 	|		      							50		|						Number of downloaded images from list_of_animes.txt.|	anime.py
DELETE_IMAGES |									True	|							Delete images from ./ANIMEIMAGES after making grid.|	grid.py
FULLSCREEN_WINDOW  		|					False	|							Makes tkinter root Fullscreen.|	grid.py
CLOSE_WINDOW_AFTER_SEARCH	|			False	|							Quits window after 2s of showing the grid.|	grid.py
ROW_SIZE				|								5			|							Indicates row length.|	grid.py
COLUMN_SIZE 			|							8			|							Indicates column length.|	grid.py
GRID_SIZE 	|					120			|						Indicates width and height of image canvas resizing in pixels.|grid.py	
PADDING								|					50			|							Indicates window padding in pixels.|	grid.py
PADDING_CELL 	|				0			|							Indicates cell padding in pixels.|	grid.py
BACKGROUND_COLOR 					|	 	 "white"	|						Indicates window background color.|	grid.py
USER 					|	 	 300	|						MY ANIME LIST username|	anime_list.py


----------------------------------------------------------------
