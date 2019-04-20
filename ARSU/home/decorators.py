from django.core.exceptions import PermissionDenied


def student_required(function):
    def wrap(request, args=None, **kwargs):
        if request.user.student == True:
            return function(request, **kwargs)
        else:
            raise PermissionDenied
    return wrap
