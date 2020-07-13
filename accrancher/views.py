from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.views.generic import TemplateView
from .forms import CommunitySelectForm
from django.contrib.auth import authenticate, login
from django.contrib import messages



from .models import UserProfile, SaveChkbox
import time
from .forms import UserForm, ProfileForm
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your views here.


def scrap(request):
    my_list = []
    url = 'http://172.16.0.111:8080/env/1a5/apps/stacks?which=all'
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe", options=options)
    driver.get(url)
    time.sleep(3)
    page = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page, 'html.parser')
    container = soup.find_all('div', attrs={
        'class': 'ember-view stack-section'})
    for item in container:
        name = item.find('a', attrs={'class': 'ember-view'}).text
        my_list.append(name)
        print(name)

    return render(request, 'index.html', {'name': my_list})
#
#
def register(request):
    if request.method == 'POST':  # meaning when i click sigup
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, pasword=password)
            login(request,user)
            print(request.user)
            return redirect('/index/login')
    else:
         form = UserCreationForm
    context = {
            'form': form,
        }

    return render(request, 'signup.html', context)

# def profile(request, slug):
#     profile = get_object_or_404(UserProfile, slug=slug)
#     context = {
#         'profile':profile,
#     }
#     return render(request, 'profile.html', context)


def change_password(request, slug):
    profile = get_object_or_404(UserProfile, slug=slug)
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            password_form.save()
            return redirect('/index/login')
    else:
        password_form = PasswordChangeForm(request.user)
    context = {
        'password_form': password_form
    }

    return render(request,'change_password.html',context)


def edit_profile(request, slug):
    profile = get_object_or_404(UserProfile,slug=slug) # to call the user
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES,instance=profile)
        if user_form.is_valid() and profile_form.is_valid() :
            user_form.save()
            new_profile = profile_form.save()
            return redirect('/index')




    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form

    }
    return render(request, 'edit_profile.html',context)


# def allusers(request):
#     name = [str(user) for user in User.objects.all()]
#     context = {
#         'name':name
#     }
#     return render(request,'stack_detail.html',context)



def stack_detail(request):
    name = [str(user) for user in User.objects.all()]

    if request.method == 'POST':
        if request.POST.get('usernames') and request.POST.get('stacknames'):

            stack_detail1 = SaveChkbox()
            stack_detail1.usernames = request.POST.get('usernames')
            stack_detail1.stacknames = request.POST.get('stacknames')
            stack_detail1.save()
            messages.success(request, "The Selected Names " + request.POST.get('usernames')+"is Saved")
            #return redirect('/index')


            return  render(request, 'stack_detail.html')
    else:
        return render(request, 'stack_detail.html')

    context = {
        'name': name
    }

    return render(request, 'stack_detail.html', context)


































    # submitted = False
    # if request.method == 'POST':
    #     form = CommunitySelectForm(request.POST)
    #     if form.is_valid():
    #         new_form = form.cleaned_data
    #         # new_form = request.POST.getlist('ModelMultipleChoiceField')
    #         # for x in new_form:
    #         #     new_form.append(str(x))
    #         new_form.save()
    #
    #
    #         return redirect('/index')
    # else:
    #
    #
    #    form = CommunitySelectForm()
    #    if 'submitted' in request.GET:
    #        submitted = True
    # print(form)
    # return render(request, 'stack_detail.html', {'form': form})


# if request.method == 'POST':
    #     form = CommunitySelectForm(request.POST)
    #     if form.is_valid():
    #         new_form = form.cleaned_data
    #         new_form.user = request.user
    #
    #         new_form.save()

           # new_form.user = request.save(commit=True)
            #new_form.save()




                #new_form = form.cleaned_data
            #new_form.user = request.user
                #new_form.save()
    #     return redirect('/index')
    # else:
    #     form = CommunitySelectForm()
    #     #if 'submitted' in request.GET:
    #         #submitted = True
    #     print(form)
    # return render(request, 'stack_detail.html', {'form': form})



# def profile(request,slug):
#     profile = get_object_or_404(UserProfile,slug=slug)
#     context = {
#         'profile':profile,
#     }
#
#     return render(request,'profile.html',context)




def loginPage(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/index')
        else:
            messages.info(request,'username or password is incorrect')
    context = {}
    return render(request,'login.html', context)


def logutuser(request):
    return redirect('/index/login')