from django.shortcuts import render, get_object_or_404
from django.http import Http404

posts = [
    {
        'id': 0,
        'location': 'Остров отчаяния',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': (
            "Наш корабль, застрявший в открытом море страшным штормом, потерпел "
            "крушение. Весь экипаж, кроме меня, утонул; я же, несчастный Робинзон "
            "Крузо, был выброшен полумёртвым на берег этого проклятого острова."
        ),
        'title': 'Крушение у острова'
    },
    {
        'id': 1,
        'location': 'Остров отчаяния',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': (
            "Проснувшись поутру, я увидел, что наш корабль стало значительно ближе к берегу..."
        ),
        'title': 'Утро на острове'
    },

    {
        'id': 2,
        'location': 'Порт Неверленд',
        'date': '15 апреля 1701 года',
        'category': 'personal',
        'text': 'Короткая заметка про личные ощущения и планы.',
        'title': 'Личный дневник'
    },
]


def index(request):
    # выводим полный список публикаций на главной
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    # на страницу публикации вывести полный текст поста
    post = next((p for p in posts if p['id'] == id), None)
    if not post:
        raise Http404("Пост не найден")
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    # пока выводим только category_slug как текст (требование ТЗ)
    # и список постов в этой категории — если есть
    matched_posts = [p for p in posts if p.get('category') == category_slug]
    context = {
        'category_slug': category_slug,
        'posts': matched_posts,
    }
    return render(request, 'blog/category.html', context)
