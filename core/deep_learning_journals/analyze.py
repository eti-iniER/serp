import fitz
from concurrent.futures import ThreadPoolExecutor, as_completed
import os


def extract_headings_from_pdf(file_path: str) -> list[str]:
    """
    Extract headings from a PDF file using PyMuPDF.

    This function opens the PDF, iterates through each page and text block,
    and considers any text span with a font size >= 15 as a heading.
    """
    print(f"Processing file: {file_path}")

    headings = []

    try:
        doc = fitz.open(file_path)
        # Loop through each page in the document.
        for page in doc:
            page_dict = page.get_text("dict")
            for block in page_dict.get("blocks", []):
                if block.get("type") == 0:
                    for line in block.get("lines", []):
                        for span in line.get("spans", []):
                            text = span.get("text", "").strip()
                            if not text:
                                continue

                            font_size = span.get("size", 0)

                            flags = span.get("flags", 0)
                            is_bold = bool(flags & 2)

                            # Use the font size to determine heading vs subheading.
                            if font_size >= 12 or (font_size >= 11 and is_bold):
                                headings.append(text)
        doc.close()

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

    return headings


def extract_headings_from_folder_files(folder_path: str) -> dict[str, list[str]]:
    """
    Extract headings from all PDF files in the given folder concurrently.

    Uses ThreadPoolExecutor to process multiple PDFs at the same time.
    """
    headings_by_file = {}

    # Filter for PDF files in the folder.
    pdf_files = [
        file
        for file in os.listdir(folder_path)
        if file.lower().endswith(".pdf")
        and os.path.isfile(os.path.join(folder_path, file))
    ]

    # Process each PDF concurrently.
    with ThreadPoolExecutor() as executor:
        future_to_file = {
            executor.submit(
                extract_headings_from_pdf, os.path.join(folder_path, file)
            ): file
            for file in pdf_files
        }
        for future in as_completed(future_to_file):
            file = future_to_file[future]
            try:
                headings = future.result()
                headings_by_file[file] = headings
            except Exception as exc:
                print(f"{file} generated an exception: {exc}")

    print("Finished processing all files. \n")
    return headings_by_file
