from django.contrib import admin

# Register your models here.
from .models import Poll
class vote(admin.ModelAdmin):
    list_display = ['candidate_name','candidate_logo','vote_count']


admin.site.register(Poll,vote)