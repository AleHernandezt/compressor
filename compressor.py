from PIL import Image
import os 
#how to use
downloadsFolder = "C:/Users/"
#copy th path in downloadsFolder
#put .jpg, .jpeg or .png in the folder
#open terminal
#paste "python compressor.py"
#check the folder

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(downloadsFolder + "compressed_"+filename, optimize=True, quality=60)