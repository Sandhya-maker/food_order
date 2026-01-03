from django.shortcuts import render, get_object_or_404
from eapp.models import categories, food_items, food_variants


def index(request, slug=None):
    categories_1 = categories.objects.all()
    food_items_list = None

    if slug:
        food_items_list = food_items.objects.filter(
            category__name__iexact=slug
        )

    return render(
        request,
        "eapp/index.html",
        {
            "categories_1": categories_1,
            "food_items_list": food_items_list,
        },
    )


def food_detail(request, id):
    food = get_object_or_404(food_items, id=id)
    variants = food.variants.all()
    categories_1 = categories.objects.all()

    return render(
        request,
        "eapp/food_variants.html",
        {
            "food": food,
            "variants": variants,
            "categories_1": categories_1,
        },
    )



