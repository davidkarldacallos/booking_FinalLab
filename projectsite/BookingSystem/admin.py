from django.contrib import admin
from .models import Skill, Artist, Venue, Client, Booking



# Register your models here.
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at", "updated_at")
    search_fields = ("name",)
    
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "email", "display_skills", "created_at", "updated_at")
    search_fields = ("name",)
    
    def display_skills(self, obj):
        return ', '.join([skill.name for skill in obj.skills.all()])

    display_skills.short_description = 'skills'
    
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "email", "created_at", "updated_at")
    search_fields = ("name",)
    
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "type", "image", "created_at", "updated_at")
    search_fields = ("name",)
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("artist", "client", "venue", "start_date", "end_date", "created_at", "updated_at")
    search_fields = ("client","artist")    