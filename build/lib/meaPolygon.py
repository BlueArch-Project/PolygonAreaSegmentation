import matplotlib.image as mpimg


def calculate_polygon_area(coords):
    """Calculate the area of a polygon.

    This function computes the area of a polygon given its coordinates.
    The coordinates should be provided as a list in the format 
    [x1, y1, x2, y2, ..., xn, yn], where (xi, yi) are the vertices of the polygon.

    Args:
        coords (list of float): A list of coordinates in the format [x1, y1, x2, y2, ..., xn, yn].

    Returns:
        float: The area of the polygon in square units.

    Raises:
        ValueError: If the length of the coordinates list is not even, which indicates 
        an incorrect format (not a valid sequence of (x, y) pairs).

    Yields:
        None: This function does not yield any values.

    Examples:
        Example usage of the `calculate_polygon_area` function:

        >>> coords = [0, 0, 4, 0, 4, 3, 0, 3]
        >>> calculate_polygon_area(coords)
        12.0

    Note:
        The formula used in this function is the Shoelace formula (also known as the 
        Surveyor's formula). The polygon should be simple (not self-intersecting) 
        and vertices should be ordered either clockwise or counterclockwise.
    """
    n = len(coords) // 2 
    area = 0
    for i in range(n):
        x1, y1 = coords[2 * i], coords[2 * i + 1]
        if i == n - 1:
            x2, y2 = coords[0], coords[1]
        else:
            x2, y2 = coords[2 * (i + 1)], coords[2 * (i + 1) + 1]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2


def meaPolygon(img_path, txt_path):
    """Calculate the area of polygons based on an image and a text file.

    This function reads an image and a corresponding text file that contains
    polygon coordinates in a normalized format. It then calculates the area
    of each polygon.

    Args:
        img_path (str): The file path to the image.
        txt_path (str): The file path to the text file containing polygon 
                        coordinates. The format should be one polygon per line, 
                        with the label followed by the normalized coordinates 
                        [x1, y1, x2, y2, ..., xn, yn].

    Returns:
        list of float: A list containing the area of each polygon in square units.

    Raises:
        FileNotFoundError: If the image or text file does not exist or cannot be read.
        ValueError: If the coordinates in the text file are not in the correct format.

    Yields:
        None: This function does not yield any values.

    Examples:
        Example usage of the `meaPolygon` function:

        >>> areas = meaPolygon("examples/data/example.png", "examples/data/example.txt")
        >>> print(areas)
        [12.0, 8.5, ...]

    Note:
        The polygon coordinates in the text file should be normalized relative to 
        the image dimensions. The coordinates will be denormalized before area 
        calculation using the image's actual width and height.
    """
    img = mpimg.imread(img_path)

    with open(txt_path, "r") as file:
        polygons = [list(map(float, line.split())) for line in file]

    polygon_boxes = []
    for points in polygons:
        coords = points[1:]
        
        # denormalization
        x_coords = [x * img.shape[1] for x in coords[0::2]]
        y_coords = [y * img.shape[0] for y in coords[1::2]]
        
        flat_coords = [coord for pair in zip(x_coords, y_coords) for coord in pair]
        area = calculate_polygon_area(flat_coords)
        polygon_boxes.append(area)
        print(f"Polygon area: {area:.2f} square units")
        
    return polygon_boxes
