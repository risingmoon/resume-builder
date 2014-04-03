from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from outline.models import Section, Entry, Data, Profile, Web
from resume_storage.models import Resume, Saved_Entry, Saved_Section, Resume_Web
from resume_storage.forms import ResumeForm, SectionForm, EntryForm, DataForm
from django.forms import model_to_dict


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
            for i in range(len(websites)):
                # import pdb; pdb.set_trace()
                if not form.data.get('account%d' % i, False):
                    Resume_Web.objects.filter(
                        resume=resume,
                        account=websites['account%d' % i]
                    ).delete()
            return HttpResponseRedirect(reverse('home'))
    form = ResumeForm(data=data)
    return render(request, 'resume_storage/resume.html', {'form': form, 'websites': websites, 'resume': resume})


@login_required
def print_resume(request, resume_no):
    pass


@permission_required('resume_storage.delete_resume')
def delete_resume(request, resume_no):
    resume = Resume.objects.get(pk=resume_no)
    return render(request, 'resume_storage/delete.html', {'resume': resume})


@permission_required('resume_storage.delete_resume')
def real_delete(request, resume_no):
    Resume.objects.get(pk=resume_no).delete()
    return HttpResponseRedirect(reverse('home'))