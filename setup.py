from setuptools import setup


def get_requirements_from_file():
    with open("./requirements.txt") as f_in:
        requirements = f_in.read().splitlines()
    return requirements


setup(
    name="meaPolygon",
    version="0.0.1",
    author="dokaben1003",
    author_email="aki2262hiro103kawano@gmail.com",
    description="This repository provides a tool to calculate the area of polygons in semantic segmentation data, specifically for images in YOLO format. It enables the precise calculation of areas for objects defined as polygons within images. This tool is useful for researchers and developers in analyzing and evaluating segmentation tasks.",
    package_dir={"": "src"},
    install_requires=get_requirements_from_file()
)