"""cli for the copyright validator."""

import argparse

from copyright_checker.validator import validate_image_copyright


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("book_dir")
    args = parser.parse_args()
    passed_dir = getattr(args, "book_dir", None)
    
    if passed_dir is None:
        msg = "Missing argument book_dir. Please provide dir to book."
        raise ValueError(msg)

    validate_image_copyright(passed_dir)
