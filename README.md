# **Netblend Backend API**

---

Netblend is a social media website where the inter**NET** and coffee beans (that get **BLEND**ed together to make drinkable goodness), merge to one! Users are able to share photos of their best looking coffee's, create articles and set up events to meet with other coffee fanatics!

- The repository for the Frontend that is linked to this project can be found [HERE](https://github.com/DSP1994/netblend). This will come with its own Readme file, so please head over there to have a read of that. Thank you.

---

## **Live Sites**

### Deployed Frontend [LIVE](https://netblend.herokuapp.com/)

### Deploy Backend API [LIVE](https://netblend-api.herokuapp.com/)

## **Table of Contents**
+ [User Stories](#user-stories)
+ [Database](#database)
+ [Testing](#testing)
  + [Validator Testing](#validator-testing)
  + [Bugs & Fixes](#bugs--fixes)
  + [Unfixed Bugs](#unfixed-bugs)
+ [Technologies](#technologies)
  + [Main Language](#main-language)
  + [Frameworks, Libraries & Programs](#frameworks-libraries--programs)
+ [Deployment](#deployment)
+ [Credits](#credits)
  + [Content](#content)
  + [Media](#media)

## **User Stories:**
All User Stories can be found [HERE](/static/Userstories.md).

## **Database**:
![SQL Database model](/static/Readme-DrawSQL.png)

## **Testing**:
### Validator Testing: 
All files passed through [PEP8 CI](https://pep8ci.herokuapp.com/) without error.

### Bugs & Fixes

A list of bugs and fixes during the production of the API can be found [HERE](/static/bugs-fixes.md)

### Manual Testing:
1. Manually verified each url path created works.
2. Verified that the CRUD functionality is available in each app via the development version: Articles, Events, Comments, Followers, Likes, Posts, Profiles
 - Went to each link.
 - Created a new item.
 - Checked new item URL path. 
 - Edited the item (not available for Likes, Followers or Users)
 - Deleted the item (Not available for Users or Profiles)
3. Ensured search feature for Posts, Events & Articles apps returns results. Results not filtered for events:
 - Checked the views file for Events.
4. Repeated the steps for the deployed API.
5. In my Frontend Readme.md I mentioned that I had an error where I had to delete my entire DB in order for the following button to function correctly. In order to do this I had to do the following;

- Remove the all migrations files within your project. Go through each of your project apps' migration folders and remove everything inside, except the __init__.py file.
- Drop the database. Go to the Elephant SQL dashboard, select your database, and select the reset button. Locally, you can just delete the db.sqlite3  file.
- Run the commands python3 manage.py makemigrations and python3 manage.py migrate to remake migrations and setup the new database.

- I then had the unfortunate error in which clearing my cookies wouldn't allow me to access anything on the page. I ended up talking to Oisin, who informed me to click the lock icon on the left hand side of the URL, and manually remove the cookies, and this seemed to resolve the error and I was able to log in normally. 

### Unfixed Bugs
- N/A

## **Technologies**:
### Main Language:
- Python

### Frameworks, Libraries & Programs:
- Django
- Django RestFramework
- Cloudinary
- Heroku
- Pillow
- Django Rest Auth
- PostgreSQL
- Cors Headers
- DrawSQL

## **Deployment**:
### Project creation:
1. Create the GitHub repository.
2. Create the project app on [Heroku](heroku.com).
3. Add the Postgres package to the Heroku app via the Resources tab.
4. Once the GitHub repository was launched on GitPod, installed the following packages using the `pip install` command:
```
'django<4'
dj3-cloudinary-storage
Pillow
djangorestframework
django-filter
dj-rest-auth
'dj-rest-auth[with_social]'
djangorestframework-simplejwt
dj_database_url psycopg2
gunicorn
django-cors-headers
```
5. Created the Django project with the following command:
```
django-admin startproject project_name .
```
6. Navigated back to [Heroku](heroku.com), and under the Settings tab, added the following configvars:
 - Key: SECRET_KEY | Value: hidden
 - Key: CLOUDINARY_URL | Value: cloudinary://hidden
 - Key: DISABLE_COLLECTSTATIC | Value: 1
 - Key: ALLOWED_HOST | Value: api-app-name.herokuapp.com
7. Add two additional configvars once the ReactApp has been created:
 - Key: CLIENT_ORIGIN | Value: https://react-app-name.herokuapp.com
 - Key: CLIENT_ORIGIN_DEV | Value: https://gitpod-browser-link.ws-eu54.gitpod.io
  - Check that the trailing slash `\` at the end of both links has been removed.
  - Gitpod occasionally updates the browser preview link. Should this occur, the CLIENT_ORIGIN_DEV value shall need to be updated.

8. Created the env.py file, and added the following variables. The value for DATABASE_URL was obtained from the Heroku configvars in the previous step:
```
import os

os.environ['CLOUDINARY_URL'] = 'cloudinary://hidden'
os.environ['DEV'] = '1'
os.environ['SECRET_KEY'] = 'hidden'
os.environ['DATABASE_URL'] = 'postgres://hidden'
```
### In settings.py: 
<!-- For reference, refer to: [DRF-API walkthrough settings.py](https://github.com/Code-Institute-Solutions/drf-api/blob/2c0931a2b569704f96c646555b0bee2a4d883f01/drf_api/settings.py) -->
9. Add the following to INSTALLED_APPS to support the newly installed packages:
```
'cloudinary_storage',
'django.contrib.staticfiles',
'cloudinary',
'rest_framework',
'django_filters',
'rest_framework.authtoken',
'dj_rest_auth',
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'dj_rest_auth.registration',
'corsheaders',
```
10. Import the database, the regular expression module & the env.py
```
import dj_database_url
import re
import os
if os.path.exists('env.py')
    import env
```

11. Below the import statements, add the following variable for Cloudinary:
```
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.ger('CLOUDINARY_URL')
}

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinartStorage'
```
- Below INSTALLED_APPS, set site ID:
```
SITE_ID = 1
```
12. Below BASE_DIR, create the REST_FRAMEWORK, and include page pagination to improve app loading times, pagination count, and date/time format:
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}
```
13. Set the default renderer to JSON:
```
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```
14. Beneath that, added the following:
```
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'
```
15. Then added:
```
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'project_name.serializers.CurrentUserSerializer'
}
```
16. Updated DEBUG variable to:
```
DEBUG = 'DEV' in os.environ
```
17. Updated the DATABASES variable to:
```
DATABASES = {
    'default': ({
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    )
    )
}
```
18. Added the Heroku app to the ALLOWED_HOSTS variable:
```
os.environ.get('ALLOWED_HOST'),
'localhost',
```
19. Below ALLOWED_HOST, added the CORS_ALLOWED variable as shown in [DRF-API walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/a6250c9e9b284dbf99e53ac8e8b68d3e/0c9a4768eea44c38b06d6474ad21cf75/?child=first):
```
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]
```
20. Also added to the top of MIDDLEWARE:
```
'corsheaders.middleware.CorsMiddleware',
```
- During a deployment issue, it was suggested by a fellow student, Johan, to add the following lines of code below CORS_ALLOW_CREDENTIALS:
```
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = list(default_headers)
CORS_ALLOW_METHODS = list(default_methods)
CSRF_TRUSTED_ORIGINS = [os.environ.get(
    'CLIENT_ORIGIN_DEV', 'CLIENT_ORIGIN',
)]
```
- In addition, Johan also suggested to add the following import statement at the top of the settings.py file:
```
from corsheaders.defaults import default_headers, default_methods
```

### Final requirements:
21. Created a Procfile, & added the following two lines:
```
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn project_name.wsgi
```
22. Migrated the database:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
23. Froze requirements:
```
pip3 freeze --local > requirements.txt
```
24. Added, committed & pushed the changes to GitHub
25. Navigated back to heroku, and under the ‘Deploy’ tab, connect the GitHub repository.
26. Deployed the branch.

### Deploy to Render & ElephantSQL:
* Due to Heroku revoking their frie tier access, the project has been redeployed using (ElephantSQL)[https://www.elephantsql.com/] using the following [instructions](https://code-institute-students.github.io/deployment-docs/41-pp5-adv-fe/pp5-adv-fe-drf-01-create-a-database)

## **CREDITS**:

- This API database was provided through the step by step guide of the CI DRF-API walkthrough project.
- An additional two apps along with models, serializers & views have been created by myself.
- I would like to thank the CI tutors for the continued support throughout both sections of my project. They were of immense help.