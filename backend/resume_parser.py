import re
from pypdf import PdfReader


def extract_text(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def extract_email(text):

    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    return match.group() if match else None


def extract_name(text):

    lines = text.split("\n")

    for line in lines[:10]:

        line = line.strip()

        if (
            len(line.split()) >= 2
            and len(line.split()) <= 4
            and "@" not in line
            and not any(char.isdigit() for char in line)
        ):
            return line

    return "Candidate"