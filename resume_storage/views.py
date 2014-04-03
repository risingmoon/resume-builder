from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from outline.models import Section, Entry, Data, Profile, Web
from resume_storage.models import Resume, Resume_Web
from resume_storage.models import Saved_Entry, Saved_Section
from resume_storage.forms import ResumeForm, SectionForm, EntryForm, DataForm
from django.forms import model_to_dict
from django.contrib.auth.models import User

#report lab imports for making pdfs
from reportlab.platypus import SimpleDocTemplate, PageTemplate, Frame
from reportlab.platypus import Paragraph, Table, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle


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


@permission_required('resume_storage.add_resume')
def create_resume(request):
    prof = Profile.objects.get(user=request.user)
    webs = Web.objects.filter(profile=prof)
    kwargs = model_to_dict(prof, exclude=['user', 'id'])
    res = Resume.objects.create(
        user=request.user,
        title='New Resume',
        **kwargs
    )
    for item in webs:
        Resume_Web.objects.create(resume=res, account=item.account)
    return HttpResponseRedirect(reverse('resume_view', args=(res.pk,)))


@permission_required('resume_storage.change_resume')
def resume_view(request, resume_no):
    sections = Section.objects.filter(user=request.user).prefetch_related()
    resume = Resume.objects.get(pk=resume_no)
    data = model_to_dict(resume)
    data.pop('title')
    accts = Resume_Web.objects.filter(resume=resume)
    websites = {}
    for i in range(len(accts)):
        websites.update({'account%d' % i: accts[i].account})
    if request.method == 'POST':
        data.update(request.POST)
        form = ResumeForm(data)

        # Edit the stuff in the resume
        if form.is_valid():
            resume.title = form.cleaned_data['title'][3:-2]
            if not form.data.get('Middle name', False):
                resume.middle_name = ''
            if not form.data.get('Cell', False):
                resume.cell = ''
            if not form.data.get('Home', False):
                resume.home = ''
            if not form.data.get('Fax', False):
                resume.fax = ''
            if not form.data.get('Address1', False):
                resume.address1 = ''
            if not form.data.get('Address2', False):
                resume.address2 = ''
            if not form.data.get('City', False):
                resume.city = ''
            if not form.data.get('State', False):
                resume.state = ''
            if not form.data.get('Zipcode', False):
                resume.zipcode = ''
            if not form.data.get('Email', False):
                resume.email = ''
            if not form.data.get('Region', False):
                resume.region = ''
            resume.save()

            # Edit the web accounts associated with the resume
            for i in range(len(websites)):
                if not form.data.get('account%d' % i, False):
                    Resume_Web.objects.filter(
                        resume=resume,
                        account=websites['account%d' % i]
                    ).delete()

            return HttpResponseRedirect(reverse('home'))
    form = ResumeForm(data=data)
    return render(
        request,
        'resume_storage/resume.html',
        {'form': form, 'websites': websites, 'resume': resume, 'sections': sections}
    )


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
