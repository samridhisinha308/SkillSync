
import fitz


def extract_resume_text(uploaded_file):

    # Read PDF file
    pdf_document = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    extracted_text = ""

    # Extract text from every page
    for page in pdf_document:
        extracted_text += page.get_text()

    pdf_document.close()

    return extracted_text
