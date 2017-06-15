# Created with:
* python                3.6.1

* pipenv                5.0.0

* Django                1.11.2
* Django Debug Toolbar  1.8.0
* Django Rest Framework 3.6.3
* Django Rest Swagger   2.1.2

(complete dependencies list is in Pipfile.lock)

# Setup
* to install all dependencies and create new venv run (in the project's root):
    pipenv install --python python3.6
* To change env from develompnet to production change variable "production"
 in ./project/project.py to "True"
* at present stage projects uses only sqlite db, so no further db setup is necessary


# Project's URLs:
* Admin Panel: /admin/

* API:
    - /api-auth/
    - /api/task-list/
    - /api/task-list/<task-list-pk>

* API Schema (Swagger):
    - /api/schema/