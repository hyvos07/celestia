from django.forms import ModelForm
from django.utils.html import strip_tags
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'description',
            'stock',
            'chara',
            'game',
            'category',
            'image',
        ]
    
    def clean_name(self):
        name = self.cleaned_data['name']
        return strip_tags(name)
    
    def clean_price(self):
        price = self.cleaned_data['price']
        return strip_tags(price)
    
    def clean_description(self):
        description = self.cleaned_data['description']
        return strip_tags(description)
    
    def clean_stock(self):
        stock = self.cleaned_data['stock']
        return strip_tags(stock)
    
    def clean_chara(self):
        chara = self.cleaned_data['chara']
        return strip_tags(chara)
    
    def clean_game(self):
        game = self.cleaned_data['game']
        return strip_tags(game)
    
    def clean_category(self):
        category = self.cleaned_data['category']
        return strip_tags(category)
    
    def clean_image(self):
        image = self.cleaned_data['image']
        return strip_tags(image)