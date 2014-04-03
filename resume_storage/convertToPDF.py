from models import Resume, Resume_Web, Saved_Section, Saved_Entry
from outline.models import Section, Entry, Data
from reportlab.platypus import SimpleDocTemplate, PageTemplate, Frame
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

PAGE_HEIGHT = defaultPageSize[1]
PAGE_WIDTH = defaultPageSize[0]
styles = getSampleStyleSheet()


#this function will take the database entry from Resume, as resumeEntry
#and a file-like object, as outputFile
#and writes a pretty-ish looking resume into the file as a pdf
def writeResumePDF(resumeEntry, outputFile):
    doc = SimpleDocTemplate(outputFile, pagesize=letter)
    normalFrame = Frame(doc.leftMargin,
                        doc.rightMargin,
                        doc.width,
                        doc.height,
                        id='normal')
    page = PageTemplate(frames=[normalFrame])
    doc.addPageTemplates([page, ])

    Document = []  # list of flowables for doc.build
    for column in [resumeEntry.first_name,
                   resumeEntry.middle_name,
                   resumeEntry.last_name,
                   resumeEntry.cell,
                   resumeEntry.home,
                   resumeEntry.fax,
                   resumeEntry.address1,
                   resumeEntry.address2,
                   resumeEntry.city,
                   resumeEntry.state,
                   resumeEntry.zipcode,
                   resumeEntry.email,
                   resumeEntry.region,
                   resumeEntry.user, ]:
        Document.append(Paragraph(column))

    doc.build(Document)
    return outputFile
