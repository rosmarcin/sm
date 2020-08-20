from django.contrib import admin

from django.db.models import JSONField

#from django_json_widget.widgets import JSONEditorWidget
from django_admin_json_editor import JSONEditorWidget

from rsm.models import UserProfile, SalesModel, ParametersGroup, Parameter
# Register your models here.



class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)


class SalesModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(SalesModel, SalesModelAdmin)


class ParametersGroupAdmin(admin.ModelAdmin):
    pass

admin.site.register(ParametersGroup, ParametersGroupAdmin)




DATA_SCHEMA = {
    'type': 'object',
    'title': 'Data',
    'properties': {
        'text': {
            'title': 'Some text',
            'type': 'string',
            'format': 'textarea',
        },
        'status': {
            'title': 'Status',
            'type': 'boolean',
        },
    },
}

class ParameterAdmin(admin.ModelAdmin):
        # formfield_overrides = {
        #     JSONField: {'widget': JSONEditorWidget(DATA_SCHEMA)},
        # }
    pass


admin.site.register(Parameter, ParameterAdmin)
