from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from blog.forms import ContactusForm
from blog.models import Article, Contact
from django.views import View


class Index(View):

    def get(self, request):
        articles = Article.objects.all()
        paginator = Paginator(articles, 3)  # 3 post per page
        page = request.GET.get('page')

        try:
            posts = paginator.page(page)

        except PageNotAnInteger:
            # if page is not an integer
            posts = paginator.page(1)

        except EmptyPage:
            # if page is out of range
            posts = paginator.page(paginator.num_pages)
        return render(request, 'blog/index.html', {'articles': posts, 'page': page})



class Single(View):

    def get(self, request, article_id, article_title):
        article = get_object_or_404(Article, pk=article_id)
        article.visit += 1
        article.save()
        related_post = Article.published.filter(group=article.group)
        return render(request, 'blog/single.html', {'article': article, 'related_post': related_post})


class Search(View):
    def get(self, request):
        query = request.GET.get('q')
        articles = Article.published.filter(content__icontains=query)
        paginator = Paginator(articles, 3)  # 3 post per page
        page = request.GET.get('page')

        try :
            posts = paginator.page(page)

        except PageNotAnInteger:
            # if page is not an integer
            posts = paginator.page(1)

        except EmptyPage:
            # if page is out of range
            posts = paginator.page(paginator.num_pages)
        return render(request, 'blog/search.html', {'articles': posts, 'query': query})

class ContactUs(View):

    def post(self, request):
        form = ContactusForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            contact = Contact(fullname=fullname, subject=subject,
                              email=email, message=message)
            contact.save()

    def get(self, request):
        return render(request, 'blog/contactus.html')


class ShowGroup(View):
    
    def get(self, request, group_id, group_title):
        articles = Article.published.filter(group__id=group_id)
        return render(request, 'blog/group_list.html', {'articles': articles, 'group_title': group_title})


class AboutUs(View):
    
    def get(self, request):
        return render(request, 'blog/about_us.html')

