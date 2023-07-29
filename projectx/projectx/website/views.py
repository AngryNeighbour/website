from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView

from . import utils
import os
import markdown
import codecs
import requests
from . import forms

#import codecs и 'utf-8' для отображения русских букв
#poems_dir = os.path.join(os.path.dirname(__file__), 'poems')
#poems = [file for file in os.listdir(poems_dir) if file.endswith('.md')]


def index(request):
    poems_data = []
    poems_dir = os.path.join(os.path.dirname(__file__), 'poems')
    poems = [file for file in os.listdir(poems_dir) if file.endswith('.md')]
    for poem in poems:
        with codecs.open(os.path.join(poems_dir, poem), 'r', encoding='utf-8') as f:
            markdown_content = f.read()
            html_content = markdown.markdown(markdown_content)
            poem_title = poem
            poem_title = poem_title[:-3]
            poems_data.append({
                'poem_title': poem_title,
                'html_content': html_content,
                'title': poem_title
            })  
    return render(request, 'website/index.html', {
        'poems_data': poems_data
    })

def test(request):
    form = forms.ProfileForm
    return render(request, 'website/test.html', {
        "form": form
    })


def about(request):
        
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = response.json()
    name = "123"

    if data:
        image_url = data[0]["url"]
    

    context = {'name': name,
               'cat_image': image_url}
    
    return render(request, 'website/about.html', context)


def poem(request, title):
    html_poem = utils.md_to_html(title)
    
    if html_poem == None:
        return render(request, "website/error.html", {
            "message":"Стихотворения с таким названием нет в базе данных"
        })
    else:
        return render(request, "website/poem.html",{
            "content":html_poem,
            "title":title,
        })
    
def delete_poem(request, title):
    print(title)

    poem = f"website/poems/{title}.md"
    if default_storage.exists(poem):
        default_storage.delete(poem)
    #return render(request, "website/index.html")
    return redirect("index")

    
def edit(request):
    if request.method == "POST":
        title = request.POST['poem_title']
        content = utils.get_poem(title)
        return render(request, "website/edit.html",{
            "title":title,
            "content":content
        })


def save_edit(request):    
    #old_title = title 
    #print(old_title)
    if request.method=="POST":
        old_title = request.POST['old_title']
        old_title = f"website/poems/{old_title}.md"
        title = request.POST['title']
        content = request.POST['entry_text']
        file = f"website/poems/{title}.md"
        if default_storage.exists(old_title):
            default_storage.delete(old_title)
        with codecs.open(file, "w", "utf-8") as f:
            f.write(content)
        html_content =   utils.md_to_html(title)
        #Обновляем список стихов
        return render(request, "website/poem.html", {
            "title": title,
            "content": html_content
        })

    
def new_poem(request):
    if request.method=="GET":
        return render(request, "website/new_poem.html")
    else:
        title = request.POST['title']
        content = request.POST['poem_text']
        poem_exist = utils.get_poem(title)
        if poem_exist is not None:
            return render(request, "website/error.html", {
                "message": "Такое название уже существует"
            })
        else:
            utils.save_changes(title, content)
            html_content = utils.md_to_html(title)
            return render(request, "website/poem.html",{
                "title":title,
                "content":html_content
            })
        

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': forms.UserCreationForm1()
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = forms.UserCreationForm1(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")
        context = {
            'form':form
        }
        return render(request, self.template_name, context)
    
# 4 класса ниже нужны для переопределения страниц для регистрации/смены пароля и т.д., чтобы не использовать
# стандартные представления джанго с их стилями
class Password_reset_view1(PasswordResetView):
    template_name = 'registration/password_change.html'

class PasswordResetConfirmView_1(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm_1.html'

class PasswordResetCompleteView_1(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete_1.html'

class PasswordResetDoneView_1(PasswordResetDoneView):
    template_name = 'registration/password_reset_mail_sent.html'


class ProfileEdit(View):
    pass


class ProfilePage(View):
    template_name = "website/profile.html"
    def get(self, request):
        context = {
            "name": 34,
        }
        return render(request, self.template_name, context)






    

#def edit(request, poem_id):
#   poem = get_object_or_404(Poem, title=poem_id)
#   if request.method == 'POST':
#       form = PoemForm(request.POST, instance = poem)
#       if form.is_valid:
#           form.save()
#       return redirect("index  ")
#   else:
#       form = PoemForm()
#       return render(request, "edit.html", {
#       "form": form,
#       "poem": poem
#   })
 

