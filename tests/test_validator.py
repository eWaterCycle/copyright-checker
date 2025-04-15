from pathlib import Path

import pytest

from copyright_checker.validator import (
    InvalidCopyrightError,
    MissingMetadataFileError,
    validate_image_copyright,
)

TEST_DATA = Path(__file__).parent / "test_data"
VALID = TEST_DATA / "valid"
MISSING_YML = TEST_DATA / "invalid" / "no_yml"
INCORRECT_YML = TEST_DATA / "invalid" / "incorrect_yml"


def test_valid():
    validate_image_copyright(str(VALID))


def test_no_yml():
    with pytest.raises(ValueError, match="Validation failed"):
        validate_image_copyright(str(MISSING_YML))

    with pytest.raises(MissingMetadataFileError):
        validate_image_copyright(str(MISSING_YML), fail_fast=True)


def test_incorrect_yml():
    with pytest.raises(ValueError, match="Validation failed"):
        validate_image_copyright(str(INCORRECT_YML))

    with pytest.raises(InvalidCopyrightError):
        validate_image_copyright(str(INCORRECT_YML), fail_fast=True)
