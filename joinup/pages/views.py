from django.shortcuts import render

# Create your views here.
def make_page(page):
    return lambda request: render(request, 'pages/'+page+'.html', {
            'page_title': page,
        })