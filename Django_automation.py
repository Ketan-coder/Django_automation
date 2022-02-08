import os

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
    new_file = '\n\n#----------------Replace INSTALLED_APPS with the below code----------------\/\n' + replace_text
    file.write(new_file)
    file.truncate()