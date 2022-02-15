#pip install pillow
#pip install scikit-image numpy pillow

from mosaic import create_mosaic

imgSource="test.jpg" #The name of the picture file
w=450 #The width of the picture
h=600 #The height of the picture

create_mosaic(
    source_path=imgSource,
    target="test-output.png", #The name of the file you will get after the proccessing
    tile_paths=["pics/1.png", # an array of tiles that will construct the new image
    "pics/2.png",
    "pics/3.png",
    "pics/4.png",
    "pics/5.png",
    "pics/6.png",
    "pics/7.png",
    "pics/8.png",
    "pics/9.png",
    "pics/10.png",
    "pics/11.png"],
    tile_ratio=w/h, # Crop tiles to be height/width ratio
    tile_width=2, # Tile will be scaled / The little the value, the most defined is the image
    # and time consumer the proccessing 
    enlargement=1, # Mosiac will be this times larger than original
    reuse=True, # Should tiles be used multiple times?
    color_mode='RGB',  # RGB (color) L (greyscale)
)

