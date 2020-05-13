from django.shortcuts import render

posts =[
    {
        'author':'Divyansh',
        'title':'fgd',
        'content': 'Any Content here',
        'date_posted':'Date will come here '
    },
{
        'author':'Divyansh',
        'title':'fgd',
        'content': 'Any Content here',
        'date_posted':'Date will come here '
    },
{
        'author':'Divyansh',
        'title':'fgd',
        'content': 'Any Content here',
        'date_posted':'Date will come here '
    },
]

def home(request):
    context={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'Hell Yeah'})
