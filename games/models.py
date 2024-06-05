from django.db import models


GAME_TYPE = (
    ("play_with_money", "Play With Money"),
    ("play_for_free", "Free Game")
)


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Game(models.Model):
    category = models.ForeignKey(Category, related_name="games", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=GAME_TYPE, default="play_with_money")
    image = models.ImageField(upload_to="game_pics")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    review = models.IntegerField(default=0)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
