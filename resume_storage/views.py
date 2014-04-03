from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from outline.models import Section, Entry, Data
from resume_storage.models import Saved_Entry, Saved_Section
from resume_storage.models import Resume, Resume_Web
from resume_storage.forms import ResumeForm, SectionForm, EntryForm, DataForm

#report lab imports for making pdfs
from reportlab.platypus import SimpleDocTemplate, PageTemplate, Frame
from reportlab.platypus import Paragraph, Table, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle


def stub_view(request, *args, **kwargs):
    body = "Resume Storage stub view\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type='text/plain')


def front_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'resume_storage/front.html', {})


@login_required
def home_view(request):
    all_resumes = Resume.objects.all().prefetch_related()
    resumes = all_resumes.filter(user=request.user)
    context = {'resumes': resumes, }
    return render(request, 'resume_storage/home.html', context)


@permission_required('resume_storage.change_resume')
def resume_view(request, resume_no):
    resume = Resume.objects.get(pk=resume_no)
    section = Section.objects.get(pk=1)
    entry = Entry.objects.get(pk=1)
    datum = Data.objects.get(pk=1)
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            resume.save()
            return HttpResponseRedirect(reverse('home'))
    form = ResumeForm(instance=resume)
    form_s = SectionForm(instance=section)
    form_e = EntryForm(instance=entry)
    form_d = DataForm(instance=datum)
    form
    context = {
        'resume': resume,
        'form': form,
        'form_s': form_s,
        'form_e': form_e,
        'form_d': form_d,
    }
    return render(request, 'resume_storage/resume.html', context)


@login_required
def print_resume(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    existingresume = Resume.objects.filter(title='myFavoriteResume')[0]
    writeResumePDF(existingresume, response)
    return response


@permission_required('resume_storage.delete_resume')
def delete_resume(request, resume_no):
    resume = Resume.objects.get(pk=resume_no)
    return render(request, 'resume_storage/delete.html', {'resume': resume})


@permission_required('resume_storage.delete_resume')
def real_delete(request, resume_no):
    Resume.objects.get(pk=resume_no).delete()
    return HttpResponseRedirect(reverse('home'))


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
    HeaderData = []
    for column in [resumeEntry.middle_initial(),
                   resumeEntry.title,
                   resumeEntry.email, ]:
        if column != '':
            HeaderData.append([column])
    for website in resumeEntry.resume_web_set.all():
        HeaderData.append([website.account])

    i = 0
    for column in [resumeEntry.cell,
                   resumeEntry.home,
                   resumeEntry.fax,
                   resumeEntry.address1,
                   resumeEntry.address2,
                   resumeEntry.region, ]:
        if column != '':
            if i == len(HeaderData):
                HeaderData.append(['', ])
            HeaderData[i].append(column)
            i += 1

    citstazip = ''
    if resumeEntry.city != '':
        citstazip += resumeEntry.city
    if resumeEntry.state != '':
        if citstazip != '':
            citstazip += ', '
        citstazip += resumeEntry.state
    if resumeEntry.zipcode != '':
        if citstazip != '':
            citstazip += ' '
        citstazip += resumeEntry.zipcode

    if citstazip != '':
        if i == len(HeaderData):
            HeaderData.append(['', ])
        HeaderData[i].append(citstazip)
        i += 1

    Document.append(Table(HeaderData))
    doc.build(Document)
    return outputFile
