from flask import Flask, request, send_file, jsonify
from bin.filters import apply_filter

app = Flask(__name__)

# Read the PIL (Python Imaging Library) documentation to find out which filters are available out-of the box
# the following filters are out-of-the-box from the PIL
filters_available = [
                        "blur",
                        "contour",
                        "detail",
                        "edge_enhance",
                        "edge_enhance_more",
                        "emboss",
                        "find_edges",
                        "sharpen",
                        "smooth",
                        "smooth_more",
                    ]

# @app.route allows multiple routes to be specified simultaneously
@app.route("/", methods=["GET", "POST"])
def index():
    """
    TODO:
    1. Return the usage instructions:
        a) filters available
        b) the method format
    """
    response = {
        "filters_available": filters_available,
        "usage": {"http_method": "POST", "URL": "/<filter_available>/"}
    }
    return jsonify(response)

# the route is expressed as a parameter, in order to capture the filter name in a variable
# URL/blur will capture blur as the value of the filter variable
@app.post("/<filter>")
# filter specified in url is passed to image_filter() method
def image_filter(filter):
    """
    TODO:
    1. Verify that the provided filter is available. If not, return error message.
    2. Check if file submitted via POST request. If not, return error message.
    3. Apply filter by calling apply_filter() method from bin.filters
    4. Return filtered image as response.
    """

    # Verify that the provided filter is available. If not, return error message.
    if filter not in filters_available:
        response = {"error": "specified filter not available"}
        return jsonify(response)

    # obtain the file to filter from the files hash (payload)
    file = request.files["image"]

    # verify that an image is provided to be filtered
    if not file:
        response = {"error": "no file provided"}
        return jsonify(response)

    # apply the filter to the supplied file
    filtered_image = apply_filter(file, filter)

    # return the filtered image to the user
    return send_file(filtered_image, mimetype="image/JPEG")


if __name__ == "__main__":
    app.run()
    