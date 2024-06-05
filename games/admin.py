from django.contrib import admin

from .models import Game, Category


class GameAdmin(admin.ModelAdmin):
    list_display = ["category", "name", "price", "type", "review"]


admin.site.register(Category)
admin.site.register(Game, GameAdmin)

