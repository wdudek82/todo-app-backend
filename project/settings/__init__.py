from project import project


if project.production:
    from .production import *
else:
    from .development import *

