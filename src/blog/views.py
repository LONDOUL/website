from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from blog.models import BlogPost


def blog_posts_redirect(request):
    print("La vue retournée")
    return redirect('https://www.udemy.com/course/machine-learning-engineer/?couponCode=VIP_ONLY_2023_JULY')


@user_passes_test(lambda u: 'Modérateurs' in [group.name for group in u.groups.all()])
def blog_posts(request):
    blog_post = get_object_or_404(BlogPost, pk=1)
    return HttpResponse(blog_post.title)

# Décorateur connexion
# @login_required
# def blog_posts(request):
#     blog_post = get_object_or_404(BlogPost, pk=1)
#     return HttpResponse(blog_post.title)

# get_object_or_404() # Fonction racourccis pour try except
# try:
#     blog_post = BlogPost.objects.get(pk=3)
# except BlogPost.DoesNotExist as e:
#     raise Http404('L\'article n\'existe pas') from e
# return render(request, 'blog/blog.html', context={'blog_post': blog_post.title})

# response = render_to_string('blog/blog.html', context={'blog_post': blog_post.title})
# return HttpResponse(response)

# return HttpResponse(blog_post.title)
# return HttpResponse('<h2 class="not_found">L\'étudiant</h2>')
# return JsonResponse({"1": "Premier blog"})
