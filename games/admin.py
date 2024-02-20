# from django.contrib import admin
# from .models import *


# class GameScreenshotInline(admin.TabularInline)


# class GameAdmin(admin.ModelAdmin):
#     readonly_fields = ['views', 'downloaded']



# admin.site.register(Game, GameAdmin)
# admin.site.register(GameScreenshot)


from django.contrib import admin
from .models import *


class GameScreenshotInline(admin.TabularInline):
    model = GameScreenshot
    


class GameAdmin(admin.ModelAdmin):
    readonly_fields = ['views', 'downloaded']
    inlines = [GameScreenshotInline]  


admin.site.register(Game, GameAdmin)
admin.site.register(GameScreenshot)
admin.site.register(GameReviews)
