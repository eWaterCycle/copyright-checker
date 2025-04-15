"""Check if copyright statements are added to all image files."""

from pathlib import Path

EXTS = ["png", "svg", "jpg", "jpeg", "tiff", "bmp", "gif"]
VALID_LICENSES = {
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
}


class MissingMetadataFileError(Exception):
    """Missing Copyright yaml file."""

    ...


class InvalidCopyrightError(Exception):
    """No valid license found in yaml file."""

    ...


def validate_image_copyright(
    book: str, extensions: list[str] = EXTS, fail_fast: bool = False
) -> bool:
    """Validate if any correct copyright statements are present for all image files.

    The copyright statements should be in a yaml file with the same name as the image.
    For example:
        - content/my_image.png
        - content/my_image.png.yml

    Args:
        book: Path to book directory that should be checked.
        extensions: Which file extensions to check. Defaults to;
            jpg, jpeg, png, svg, tiff, bmp, gif
        fail_fast: If the validator should raise an error upon the first invalid file,
            or check all files before failing.
    """
    book_dir = Path(book).absolute()

    if not book_dir.is_dir():
        msg = (
            f"Passed book_dir argument '{book_dir}' does not exist or is "
            "not a directory!"
        )
        raise ValueError(msg)

    img_files: list[Path] = []
    for ext in extensions:
        img_files += list(Path(book_dir).glob(f"**/*.{ext}", case_sensitive=False))

    missing_ymls = []
    invalid_licenses = []
    for img in img_files:
        yml_file = img.with_suffix(img.suffix + ".yml")
        if not yml_file.exists():
            msg = f"{img}.yml file is missing."
            missing_ymls.append(str(img))
            if fail_fast:
                raise MissingMetadataFileError(msg)
        else:
            with yml_file.open("r") as f:
                content = "".join(f.readlines())
                content = content.strip('"').strip("'")
                if not any(f'license: "{lic}' in content for lic in VALID_LICENSES):
                    msg = f"No valid license detected in file '{yml_file}'"
                    invalid_licenses.append(str(img))
                    if fail_fast:
                        raise InvalidCopyrightError(msg)

    if len(missing_ymls) > 0:
        print(
            "The following files had no .yml files associated with them:", end="\n    "
        )
        print("\n    ".join(missing_ymls) + "\n")
    if len(invalid_licenses) > 0:
        print("The following files had no valid licence:", end="\n    ")
        print("\n    ".join(invalid_licenses) + "\n")

    if len(missing_ymls) > 0 or len(invalid_licenses) > 0:
        msg = "Validation failed. See printed errors."
        raise ValueError(msg)
