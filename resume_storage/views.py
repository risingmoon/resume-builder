from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from outline.models import Section, Entry, Data, Profile
from resume_storage.models import Resume, Saved_Entry, Saved_Section
from resume_storage.forms import ResumeForm, SectionForm, EntryForm, DataForm
from django.forms import model_to_dict


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


@permission_required('resume_storage.add_resume')
def create_resume(request):
    prof = Profile.objects.get(user=request.user)
    kwargs = model_to_dict(prof, exclude=['user', 'id'])
    res = Resume.objects.create(user=request.user, **kwargs)
    return HttpResponseRedirect(reverse('resume_view', args=(res.pk,)))


@permission_required('resume_storage.change_resume')
def resume_view(request, resume_no):
    resume = Resume.objects.get(pk=resume_no)
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            if not form.cleaned_data['Include middle_name?']:
                resume.middle_name = ''
            resume.save()
            return HttpResponseRedirect(reverse('home'))
    form = ResumeForm(instance=resume)
    form
    context = {
        'resume': resume,
        'form': form,
    }
    return render(request, 'resume_storage/resume.html', context)


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