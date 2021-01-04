from django.shortcuts import render, HttpResponse,redirect
from blog.models import Post,BlogComment
from home import views
from django.contrib import messages
# Create your views here.

def blogHome(request):
    allpost=Post.objects.all()
    context={
        'allpost':allpost
    }
    return render(request,'blog/blogHome.html',context)

def fullpost(request,slug):
    #return HttpResponse(f'this is blogpost:{slug}') 
    post=Post.objects.filter(slug=slug)
    comments=reversed(BlogComment.objects.filter(post__in=post))
    context={'post':post,'comments':comments}
    return render(request,'blog/fullpost.html',context)  

def postComment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postSno=request.POST.get("postSno")   
        post=Post.objects.get(sno=postSno)
        if len(comment)<1:
            messages.error(request,"don't post empty comment")
        else: 
            comment_obj=BlogComment(comment=comment,user=user,post=post)
            comment_obj.save()
            messages.success(request,"your comment has been posted successfully")   
            
    return redirect(f'/blog/{post.slug}')