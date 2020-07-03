import glob

a4size = [210, 297]  # mm
margins = [25.4, 12.7]


def get_images():
    print(glob.glob("images/*"))
    # listofimages
    # return listofimages