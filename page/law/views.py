from django.shortcuts import render

def index(request):
    template = 'law/index.html'
    title = 'Юридическая фирма "Правосудие". г. Магнитогорск'
    context = {
        'title': title,
        'text': 'Главная страница',
    }
    return render(request, template, context) 

def article(request):
    template = 'law/article.html'
    return render(request, template)

def reviews(request):
    template = 'law/reviews.html'
    return render(request, template) 
