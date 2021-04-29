from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from datetime import datetime
from django.contrib import messages
# Create your views here.
def blogs(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            title = request.POST['title']
            content = request.POST['content']
            image = request.POST['image']

            blog = Blog(title=title,content=content,image=image,status='0',author=request.user.email,date=datetime.today().date())
            blog.save()
            messages.success(request,"Your Blog is Saved. It will be displayed after admin Approval")
            return redirect("blogs")
        else:
            messages.error(request,"Make Login First")
            return redirect('blogs')

    blogs_data=False
    if request.GET.get('category',False):
        category = request.GET['category']
        blogs_data = Blog.objects.filter(status='1',category_iexact=category).order_by('-date')
    else:
        blogs_data = Blog.objects.filter(status='1').order_by('-date')
    paginator = Paginator(blogs_data, 6)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)
    return render(request,'blog.html',{"blogs":paged_blogs})

def single_blog(request,slug):
    recent_blogs = Blog.objects.filter(status='1').order_by('-date')[:3]
    categories_result = Blog.objects.order_by().values('category').distinct().annotate(the_count=Count('category'))
    categories = dict()
    for cat in categories_result:
        cat = dict(cat)
        categories.update({cat['category']:cat['the_count']})
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog-single.html', {"recent_blogs": recent_blogs,'categories':categories,'blog':blog})
