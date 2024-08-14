from setuptools import setup


def get_requirements_from_file():
    with open("./requirements.txt") as f_in:
        requirements = f_in.read().splitlines()
    return requirements

def get_long_description():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()


setup(
    name="meaPolygon",
    version="0.0.5",
    author="dokaben1003",
    author_email="aki2262hiro103kawano@gmail.com",
    description="This repository provides a tool to calculate the area of polygons in semantic segmentation data, specifically for images in YOLO format. It enables the precise calculation of areas for objects defined as polygons within images. This tool is useful for researchers and developers in analyzing and evaluating segmentation tasks.",
    long_description=get_long_description(),  # README.md から説明文を取得
    long_description_content_type="text/markdown",  # README.md が Markdown フォーマットであることを指定
    package_dir={"": "src"},
    install_requires=get_requirements_from_file(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)