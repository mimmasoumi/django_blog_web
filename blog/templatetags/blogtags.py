from django import template

from blog.models import Article, Group

register = template.Library()


@register.inclusion_tag('blog/sidebar.html')
def sidebar():
    most_visited = Article.published.order_by('visit')[:3]
    groups = Group.objects.all()
    recent_posts = Article.published.order_by('created')[:3]

    return {'most_visited': most_visited, 'groups': groups, 'recent_post': recent_posts}


@register.inclusion_tag('blog/top_navbar.html')
def top_navbar():
    groups = Group.objects.all()
    return {'groups': groups}
