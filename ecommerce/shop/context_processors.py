from shop.models import Category


def menu_links(request):
    cat = Category.objects.all()
    return {'links': cat}
