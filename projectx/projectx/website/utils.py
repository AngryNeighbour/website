import os
import codecs
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import markdown

def get_poem(title):
    try:
        file_path = f"website/poems/{title}.md"
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return None
    
def save_changes(title, content):
    file = f"website/poems/{title}.md"
    if default_storage.exists(file):
        default_storage.delete(file)
    #default_storage.save(file, ContentFile(content))
    with codecs.open(file, "w", "utf-8") as f:
        f.write(content)
        #default_storage.save(file, ContentFile(content))


def md_to_html(text):
    content = get_poem(text)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)


#def save_edit(request):
#    if request.method=="POST":
#        old_title = request.POST['old_title']
#        title = request.POST['title']
#        content = request.POST['entry_text']
#        save_changes1(old_title, title, content)
#        html_content =   md_to_html(title)
#        return render(request, "website/poem.html", {
#            "title": title,
#            "content": html_content
#        })


    


#def poem(request, title):
#    html_poem = utils.get_poem(title)
#    if html_poem == None:
#        return render(request, "website/error.html", {
#            "message":"Стихотворения с таким названием нет в базе данных"
#        })
#    else:
#        html_poem = markdown.markdown(html_poem)
#        return render(request, "website/poem.html",{
#            "content":html_poem,
#            "title":title
#        })