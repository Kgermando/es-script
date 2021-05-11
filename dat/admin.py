from django.contrib import admin

from daterangefilter.filters import PastDateRangeFilter, FutureDateRangeFilter

from dat.models import Dat
# Register your models here.


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;' \
                                      'filename={}.csv'.format(
                                          opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields(
    ) if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_to_csv.short_description = 'Export to CSV'

class DatAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'created_date', 'questions1', 'questions2', 'Nom', 'Post_Nom', 'Prenom', 'Numero', 'Quartier', 'Commune', 'Province', 
        'Tel1', 'Email', 'Statut', 'Bound', 'Remarque'
    )

    list_filter = (
        ('created_date', PastDateRangeFilter), 
        'user', 'Statut', 'Bound'
    )

    actions = [export_to_csv]

    ordering = ['-created_date',]

admin.site.register(Dat, DatAdmin)
