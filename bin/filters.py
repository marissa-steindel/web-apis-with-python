from PIL import Image, ImageFilter
import io


def apply_filter(file: object, filter: str) -> object:
    """
    TODO:
    1. Accept the image as file object, and the filter type as string
    2. Open the as an PIL Image object
    3. Apply the filter
    4. Convert the PIL Image object to file object
    5. Return the file object
    """

    # import two methods from the Python Imaging Library
    # Image() - stores the image data
    # ImageFilter() - applies the filter

    # open the image as a PIL object
    image = Image.open(file)

    # apply the filter - eg. ImageFilter.BLUR
    # eval() - converts a string to a python command
    image = image.filter(eval(f"ImageFilter.{filter.upper()}"))

    # convert the filtered PIL image object back to a file
    # create an empty buffer in memory
    file = io.BytesIO()

    # pass the pointer to the buffer, which stores the file in memory
    image.save(file,"JPEG")

    # reset the pointer to start
    file.seek(0)

    # return the file object
    return file
