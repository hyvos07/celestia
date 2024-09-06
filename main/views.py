from django.shortcuts import render

def show_main(request):
    context = {
        'image_URL' : r'assets\dev\Error.png',
        'name': 'Pop Up Parade Figure Furina - Animula Choragi Ver. Genshin Impact',
        'price_with_comma': '2,300,000',
        'description': 'This is a description of the product. It is very long and detailed so that it will exceed the maximum length of the field.',
        'chara': 'Furina',
        'game': 'Genshin Impact',
        'category': 'Pop Up Parade',
    }

    return render(request, "main.html", context)
