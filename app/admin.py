from django.contrib import admin

# Register your models here.
from app.models import User, SentenceData, UserGameInfo, Ranking, ExampleData

admin.site.register(User)
admin.site.register(SentenceData)
#admin.site.register(UserStudyInfo)
admin.site.register(UserGameInfo)
admin.site.register(Ranking)
admin.site.register(ExampleData)