# copyright-checker

Checks if teachbook user has added copyright statements to every image file.

Can be used in GitHub actions to prevent a user from merging a PR or building a 
GH Pages site with possibly copyrighted content.

## Installation

In a Python >=3.12 (virtual) environment, do;

```bash
pip install https://github.com/eWaterCycle/copyright-checker/archive/refs/heads/main.zip
```

## Usage

Any image file (jpg, jpeg, png, svg, tiff, bmp, or gif) will need a yml file 
with metadata associated with it, for example;

- `content/image.png`
- `content/image.png.yml`

The yaml file should be formatted like;

```yml
author: "Bart Schilperoort"
license: "Apache 2.0"
date: "2025-04-16"
```

You can run the tool with;

```bash
check-copyright /path/to/content/ 
```

The tool with raise an error if any .yml metadata files are missing,
or no valid copyright statement is found inside the metadata file.

It will print to the terminal which files are not complying.

## Valid licenses;

The tool currently accepts the following licenses;

```
    "MIT",
    "AGPL",
    "GPL",
    "LGPL",
    "Mozilla",
    "Apache",
    "CCPL",
    "CC-BY-NC",
    "CC-BY-4.0",
    "CC0",
    "BSD3",
    "EUPL",
```

## Tests

This repository has some tests associated with them.
You can run the test suite by first installing pytest (`pip install pytest`),
and then doing `pytest tests/`.
