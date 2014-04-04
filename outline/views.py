from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from outline.models import Profile, Web, Section
from outline.forms import ProfileForm
from django.forms.models import inlineformset_factory, model_to_dict
from django import forms


def stub_view(request, *args, **kwargs):
    body = "Outline stub view\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type='text/plain')


@permission_required('outline.change_profile')
def outline(request):
    
    profile_model = Profile.objects.get(user=request.user)
    profile = model_to_dict(profile_model)
    web_set = Web.objects.filter(profile=profile_model)
    
    # resume = Resume.objects.get(pk=resume_no)
    # data = model_to_dict(resume)
    # data.pop('title')
    # accts = Resume_Web.objects.filter(resume=resume)
    # websites = {}
    # for i in range(len(accts)):
    #     websites.update({'account%d' % i: accts[i].account})
    sections = Section.objects.filter(user=request.user).prefetch_related()
    # if request.method == 'POST':
    #     data.update(request.POST)
    #     form = ResumeForm(data)
    #     form.data['title'] = form.data['title'][0]
    #     if form.is_valid():
    #         _edit_resume_profile(resume, form)
    #         _edit_resume_webs(resume, form, websites)
    #         _build_resume_fields(
    #             resume,
    #             request.user,
    #             request.POST.getlist('sections'),
    #             request.POST.getlist('entries'),
    #             request.POST.getlist('datas')
    #         )
    #         return HttpResponseRedirect(reverse('home'))
    # form = ResumeForm(data=data)
    # saved = resume.getResumeFields()
    # for key in saved.iterkeys():
    #     sections = sections.exclude(pk=key.section.pk)
    # return render(
    #     request,
    #     'resume_storage/resume.html',
    #     {
    #         'form': form,
    #         'websites': websites,
    #         'resume': resume,
    #         'sections': sections,
    #         'saved': saved,
    #     }
    # )
    # import pdb;pdb.set_trace()
    context = {
        'profile': profile,
        'web_set': web_set,
        'sections': sections}
    return render(
        request,
        'outline/outline.html',
        context,
    )


@permission_required('outline.change_profile')
def profile(request):
    prof = Profile.objects.get(user=request.user)
    WebFormSet = inlineformset_factory(
        Profile, Web, extra=1,
        widgets={'account': forms.TextInput(attrs={
            'class': 'col-sm-4 form-control',
            'placeholder': 'Account'}
        )})
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=prof)
        formset = WebFormSet(request.POST, instance=prof)
        if form.is_valid() and formset.is_valid():
            prof.first_name = form.cleaned_data['first_name']
            prof.middle_name = form.cleaned_data['middle_name']
            prof.last_name = form.cleaned_data['last_name']
            prof.cell = form.cleaned_data['cell']
            prof.home = form.cleaned_data['home']
            prof.fax = form.cleaned_data['fax']
            prof.address1 = form.cleaned_data['address1']
            prof.address2 = form.cleaned_data['address2']
            prof.city = form.cleaned_data['city']
            prof.state = form.cleaned_data['state']
            prof.zipcode = form.cleaned_data['zipcode']
            prof.email = form.cleaned_data['email']
            prof.region = form.cleaned_data['region']
            prof.save()
            formset.save()
            return HttpResponseRedirect(reverse('home'))
    form = ProfileForm(instance=prof)
    formset = WebFormSet(instance=prof)
    context = {'form': form, 'formset': formset}
    return render(
        request,
        'outline/profile.html',
        context,
    )