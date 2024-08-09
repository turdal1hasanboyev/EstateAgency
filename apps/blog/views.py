from django.shortcuts import render, redirect

from apps.blog.models import Blog, Comment


def blog(request):
    blogs = Blog.objects.all().order_by("id")[:6]

    return render(request, "blog-grid.html", {"blogs": blogs})

def blog_single(request, slug):
    blog = Blog.objects.get(slug__iexact=slug)

    comments = Comment.objects.filter(blog_id=blog.id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        website = request.POST.get("website")

        Comment.objects.create(
            blog_id=blog.id,
            user=request.user,
            name=name,
            email=email,
            message=message,
            website=website,
        )

        return redirect("blog-single", blog.slug)

    context = {
        "blog": blog,
        "comments": comments,
    }

    return render(request, "blog-single.html", context)
