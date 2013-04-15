from django import template

register = template.Library()

@register.filter
def has_answered(request, survey):
    if not hasattr(request, 'session'): return False
    return (survey.has_answers_from(request.session.session_key) or
            (request.user.is_authenticated() and
             survey.has_answers_from_user(request.user)))

@register.filter
def can_view_answers(user, survey):
    return survey.answers_viewable_by(user)

@register.filter_function
def order_by(queryset, args):
    args = [x.strip() for x in args.split(',')]
    return queryset.order_by(*args)
