from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from outline.models import Profile, Web, Section, Entry, Data
from outline.forms import ProfileForm, WebForm, SectionForm, EntryForm, DataForm
from django.forms.models import inlineformset_factory
import pdb


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
def profile(request):
    prof = Profile.objects.get(user=request.user)
    WebFormSet = inlineformset_factory(Profile, Web, extra=1)
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
    # form = ProfileForm(instance=prof)
    form = ProfileForm()
    # formset = WebFormSet(instance=prof)
    # context = {'form': form, 'formset': formset}
    context = {'form': form}
    return render(
        request,
        'outline/profile.html',
        context,
    )

#NOT WORKING
def section(request, pk):
    sect = Section.objects.get(pk=pk)
    # EntryFormSet = inlineformset_factory(Section, Entry, extra=1)
    if request.method == 'POST':
        form = SectionForm(request.POST, instance=sect)
        # formset = EntryFormSet(request.POST, instance=sect)
        # pdb.set_trace()
        if form.is_valid(): #and formset.is_valid():
            sect.title = form.cleaned_data['title']
            sect.description = form.cleaned_data['description']
            sect.save()
            # formset.save()
            return HttpResponseRedirect(reverse('home'))
    form = SectionForm(instance=sect)
    # formset = EntryForm(instance=sect)
    context = {
        'form': form,
        # 'formset': formset,
        'pk': pk}
    return render(
        request,
        'outline/section.html',
        context,
    )


def entry(request, pk):
    entry = Entry.objects.get(pk=pk)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry.title = form.cleaned_data['title']
            entry.subtitle = form.cleaned_data['subtitle']
            entry.start_date = form.cleaned_data['start_date']
            entry.end_date = form.cleaned_data['end_date']
            entry.present = form.cleaned_data['present']
            entry.city = form.cleaned_data['city']
            entry.state = form.cleaned_data['state']
            entry.contact = form.cleaned_data['contact']
            entry.description = form.cleaned_data['description']
            entry.display = form.cleaned_data['display']
            entry.save()
            return HttpResponseRedirect(reverse('home'))
    form = EntryForm(instance=entry)
    context = {
        'form': form,
        'pk': pk}
    return render(
        request,
        'outline/entry.html',
        context,
    )
