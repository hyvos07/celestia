from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Pop Up Parade Figure Furina - Animula Choragi Ver. Genshin Impact',
        'price': 2300000,
        'description': 'This is a description of the product. It is very long and detailed so that it will exceed the maximum length of the field.',
        'stock': 2,
        'chara': 'Furina',
        'game': 'Genshin Impact',
        'category': 'Plush',
        'image_URL' : r'assets\dev\Error.png',
        'price_with_comma': '2,300,000',
        'is_stock_empty': False,
    }

    return render(request, "main.html", context)
