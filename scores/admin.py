from django.contrib import admin
from .models import File, Person, Instrument, Piece, Instrumentation, Editor, Licensing
# Register your models here.


admin.site.register(File)
admin.site.register(Person)
admin.site.register(Instrument)
admin.site.register(Instrumentation)
admin.site.register(Piece)
admin.site.register(Editor)
admin.site.register(Licensing)
