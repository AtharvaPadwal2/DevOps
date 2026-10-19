
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
import pytest
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parents[1]

QR_FILES = [
    "qr-code.png",
    "qr-code.svg",
    "qr-code-path.svg",
    "qr-code-fragment.svg",
]


@pytest.fixture(scope="module")
def generated_qr(tmp_path_factory):
    output_dir = tmp_path_factory.mktemp("qr_output")

    subprocess.run(
        [
            sys.executable,
            str(PROJECT_ROOT / "src" / "qrproject" / "main.py"),
        ],
        cwd=output_dir,
        check=True,
        capture_output=True,
        text=True,
    )

    return output_dir


@pytest.mark.parametrize("filename", QR_FILES)
def test_qr_file_created(generated_qr, filename):
    assert (generated_qr / filename).is_file()


@pytest.mark.parametrize("filename", QR_FILES)
def test_qr_file_not_empty(generated_qr, filename):
    assert (generated_qr / filename).stat().st_size > 0


def test_png_is_valid(generated_qr):
    with Image.open(generated_qr / "qr-code.png") as img:
        img.verify()


@pytest.mark.parametrize("filename", QR_FILES[1:])
def test_svg_is_valid(generated_qr, filename):
    ET.parse(generated_qr / filename)
