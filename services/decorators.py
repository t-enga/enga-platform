from django.contrib.auth.decorators import user_passes_test

def group_required(*group_names):
    """Requiere que el usuario sea miembro de al menos uno de los grupos especificados."""
    def in_group(user):
        if user.is_authenticated:
            return bool(user.groups.filter(name__in=group_names))
        return False
    return user_passes_test(in_group)