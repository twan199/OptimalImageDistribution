import glob
import database

a4size = [210, 297]  # mm
margins = [25.4, 12.7]  # mm


def run():
    listofimages = get_images()
    # print(listofimages)
    images = database.db_main(listofimages)
    print(images)


def get_images():
    listofimages = glob.glob("images/*")
    listofimages.sort()
    return listofimages