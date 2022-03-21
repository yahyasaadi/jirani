from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Neighborhood, Business, Contact
from .forms import HoodForm, PostForm

# Create your views here.
def home(request):
    # if request.method == 'POST':
    #     title = request.POST['title']
    #     post = request.POST['post']

    #     posts = Post(title=title,post=post)
    #     posts.save()
    hoods = Neighborhood.objects.all()
    context ={
        'hoods':hoods,
    }
    return render(request,'dashboard/home.html',context)


# Creating a hood
@login_required
def add_hood(request):
    if request.method == 'POST':
        hood_name = request.POST['hood_name']
        hood_location = request.POST['hood_location']
        new_hood = Neighborhood(hood_name=hood_name, hood_location=hood_location, user=request.user)
        # new_form = HoodForm()
        hood_form = HoodForm(request.POST, instance=new_hood)
        if hood_form.is_valid():
            hood_form.save()
            messages.success(request, f'Your neighborhood has been added.')
            return redirect('home')
    else:
        hood_form = HoodForm(instance=request.user)
    
    return render(request, 'dashboard/add_hood.html', context={'hood_form':hood_form})


@login_required
def post(request, hood_id):
    if request.method == 'POST':
        title = request.POST['title']
        post = request.POST['post']
        new_post = Post(title=title, post=post, user=request.user, hood_id=hood_id)
        
        post_form = PostForm(request.POST, instance=new_post)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, f'Your post has been created!')
            return redirect('home')
    else:
        post_form = PostForm(instance=request.user)
    
    return render(request, 'dashboard/new_post.html', context={'post_form':post_form})



# Hood Detail View
@login_required
def hood_detail(request,id):
    hood = get_object_or_404(Neighborhood,id=id)
    businesses = Business.objects.filter(hood=hood)
    contacts = Contact.objects.filter(hood=hood)
    # posts = Post.objects.filter(hood_id=id)

    context = {
        'hood':hood,
        'businesses': businesses,
        'contacts':contacts
        }
    return render(request,'dashboard/hood_detail.html', context)
