from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from resume_storage.models import Resume, Saved_Entry, Saved_Section


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


@login_required
def resume_view(request, resume_no):
    resume = Resume.objects.get(pk=resume_no)
    return render(request, 'resume_storage/resume.html', {'resume': resume})


@login_required
def print_resume(request, resume_no):
    pass


@login_required
def delete_resume(request, resume_no):
    resume = Resume.objects.get(pk=resume_no)
    return render(request, 'resume_storage/delete.html', {'resume': resume})


@login_required
def real_delete(request, resume_no):
    Resume.objects.get(pk=resume_no).delete()
    return HttpResponseRedirect(reverse('home'))
