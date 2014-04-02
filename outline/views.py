from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from outline.models import Profile, Web, Section, Entry, Data
from outline.forms import ProfileForm, WebForm
from django.forms.models import inlineformset_factory


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
    form = ProfileForm(instance=prof)
    formset = WebFormSet(instance=prof)
    context = {'form': form, 'formset': formset}
    return render(
        request,
        'outline/profile.html',
        context,
    )
