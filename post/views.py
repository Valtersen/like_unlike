from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Post, Like
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


@login_required
def index(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


# this tutorial : https://www.geeksforgeeks.org/handling-ajax-request-in-django/
def like_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        action = request.POST.get('action')

        try:
            post = Post.objects.get(pk=post_id)
        except ObjectDoesNotExist:
            return HttpResponse('Could not find post')

        if action == 'like':
            like = Like(post=post, user=request.user)
            like.save()
            message = f'Liked post :{post.heading}!'

        elif action == 'unlike':
            try:
                like = Like.objects.filter(post=post, user=request.user).latest('id')
                like.delete()
            except ObjectDoesNotExist:
                message = "You can't unlike this post"
                return HttpResponse(message)

            message = f'Unliked post :{post.heading}!'

        else:
            message = 'idk what action'

        return HttpResponse(message)
    else:
        return HttpResponse('Not a post request')








