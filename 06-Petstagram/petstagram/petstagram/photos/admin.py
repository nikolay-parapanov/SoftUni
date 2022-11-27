from django.contrib import admin

from petstagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'publication_date', 'pets')

    def pets(self, current_photo_obj):
        return ', '.join(p.name for p in current_photo_obj.tagged_pets.all())
        
