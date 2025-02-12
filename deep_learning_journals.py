from core.deep_learning_journals import *


def main():
    folder_path = "./papers"
    print(f"\n\nExtracting headings from PDF files in {folder_path}...\n")
    pdfs = extract_headings_from_folder_files(folder_path)

    for filename, headings in pdfs.items():
        heading_count = len(headings)
        print(f'There are {heading_count} heading(s) in "{filename}":')
        for heading in headings:
            print(f"  - {heading}")
        print("\n")


if __name__ == "__main__":
    main()
