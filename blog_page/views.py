from django.shortcuts import render,get_object_or_404
from .models import Category, Article
# Importamos la libreria que nos permitira hacer la paginacion 
from django.core.paginator import Paginator
# Create your views here.


def list(request):

    # Hacemos una consulta a la base de datos
    articles = Article.objects.all()

    #Paginamos los articulos
    paginator = Paginator(articles, 3)
    
    #Recogemos el numero de paginas 
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'articles/list.html', {
        'title': 'Articulos',
        'articles': page_articles
    })


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id) 
    #articles = Article.objects.filter(categories=category_id)
    #Podemos hacer estoy obteniendo todos los datos 
    #category = Category.objects.get(id=category_id)
    return render(request, 'categories/category.html',{
        'category':category
        #'articles':articles
    })

def article(request, article_id):
    """_summary_

    Args:
        request (_request_): Retorna la respuesta del navegador
        article_id (_int_): _pasamos un id _

    Returns:
        _dic_: _retorna una vista 
    """
    # Hacemos la consula a la base de datos
    article = get_object_or_404(Article, id= article_id)
    return render(request, 'articles/detail.html',{
        'article':article
    })
