""" This python file helps me to make full flushed static and templates directories """
import os

print("Please do not use space in your project/app name at the end!")
project_name = str(input("Whats your project name : ")).capitalize()
apps_name = str(input("What your apps name : ")).split(",")


# check if the project name is in the current directory
if os.path.isdir(project_name):
    print("Project name is already in the current directory")
    exit()
else:
    os.system('cmd /c "django-admin startproject ' + project_name)
    # change the directory to the project name
    os.chdir(project_name)
    # print the current directory
    print(os.getcwd())
    # check if the apps name is in the project directory
    if os.path.isdir(apps_name[0].capitalize()):
        print("Apps name is already in the project directory")
        exit()
    else:
        # check if apps_name has more than one app
        if len(apps_name) > 1:
            for app in apps_name:
                os.system('cmd /c "django-admin startapp ' + app.capitalize())
        else:
            os.system('cmd /c "django-admin startapp ' + apps_name[0].capitalize())
# change the directory to the project name
os.chdir('../'+project_name)
# print the current directory
print(os.getcwd())

search_text = '\nINSTALLED_APPS = [\n   "django.contrib.admin",\n  "django.contrib.auth",\n  "django.contrib.contenttypes",\n  "django.contrib.sessions",\n  "django.contrib.messages",\n  "django.contrib.staticfiles",\n'
for app in apps_name:
    search_text += '    "' + app.capitalize() + '.apps.' +  app.capitalize() +'Config",\n'
replace_text = search_text + ']\n'

print(replace_text)
# append the apps name to INSTALLED_APPS in settings.py
with open(project_name + '/settings.py', 'r+') as file:
    content=file.read()
    new_file = '\n\n#----------------Replace INSTALLED_APPS with the below code----------------\/\n' + replace_text + "\nimport os\nSTATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]\n"
    file.write(new_file)
    file.truncate()

os.chdir('../')
# print the current directory
print(os.getcwd())

for app_name in apps_name:
    with open(project_name + '/' + app_name.capitalize() + '/views.py', 'r+') as file:
        content=file.read()
        new_file = 'def index(request):\n    return render("index.html")\n'
        file.write(new_file)
        file.truncate()
    with open(project_name + '/' + app_name.capitalize() + '/urls.py', 'w+') as file:
        content=file.read()
        new_file = 'from django.urls import path\nfrom . import views\n\nurlpatterns = [\n    path("", views.index, name="index"),\n]\n'
        file.write(new_file)
        file.truncate()
    with open(project_name + '/' + project_name + '/urls.py', 'r+') as file:
        content=file.read()
        for app_name in apps_name:
            content = content.replace(']','include("",(' + app_name.capitalize() + '.urls")),\n]')
        # new_file = "from "+ app_name.capitalize() +" import views\n\nurlpatterns = [\n    path('admin/', admin.site.urls),\n    path('',include('"+ app_name.capitalize() +".urls')\n]\n"
        file.write(content)
        file.truncate()

os.chdir(project_name)
# print the current directory
print(os.getcwd())
# create the templates,static directory
os.makedirs("templates")
os.makedirs("static")

html_files=['index.html','base.html','about.html','contact.html','login.html','newuser.html']

dirs =['resoures', 'vendors']
sub_dirs = ["css","img","js"]

for html_file in html_files:
    open("templates/"+html_file, "w")

dirs =['resoures', 'vendors']

for dires in dirs:
    os.makedirs("static/" + dires)

for sub_dir in sub_dirs:
    os.makedirs("static/resoures/" + sub_dir)

os.makedirs("static/resoures/css/" + sub_dirs[1])

for sub_dir in sub_dirs:
    os.makedirs("static/vendors/" + sub_dir)