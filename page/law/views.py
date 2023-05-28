from django.shortcuts import render

def index(request):
    template = 'law/index.html'
    title = 'Юридическая фирма "Правосудие". г. Магнитогорск'
    context = {
        'title': title,
    }
    return render(request, template, context) 

def article(request):
    template = 'law/article.html'
    title = 'Юридическая фирма "Правосудие". г. Магнитогорск | Полезные записи'
    context = {
        'title': title,
    }
    return render(request, template, context)

def reviews(request):
    template = 'law/reviews.html'
    return render(request, template) 
