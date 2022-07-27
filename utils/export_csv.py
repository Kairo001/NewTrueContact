import csv
from django.http import HttpResponse

def get_model_field_names(model, ignore_fields=['content_object']):
    """This method gets all model field names (as strings) and returns a list 
    of them ignoring the ones we know don't work (like the 'content_object' field).

    Parameters
    ----------
    model: Is a Django model class
    ignore_fields: Is a list of field names to ignore by default
    """
    model_fields = model._meta.get_fields()
    model_field_names = list(set([f.name for f in model_fields if f.name not in ignore_fields]))
    return model_field_names

def get_lookup_fields(model, fields=None):
    """This method compares the lookups we want vs the lookups
    that are available. It ignores the unavailable fields we passed.

    Parameters
    ----------
    model: is a Django model class
    fields: is a list of field name strings.
    """
    model_field_names = get_model_field_names(model)
    if fields is not None:
        '''
        we'll iterate through all the passed field_names
        and verify they are valid by only including the valid ones
        '''
        lookup_fields = []
        for x in fields:
            if "__" in x:
                # the __ is for ForeignKey lookups
                lookup_fields.append(x)
            elif x in model_field_names:
                lookup_fields.append(x)
    else:
        '''
        No field names were passed, use the default model fields
        '''
        lookup_fields = model_field_names
    return lookup_fields

def export_to_csv(queryset, fields, titles, file_name):
    """Will export the model data in the form of csv file.
    
    Parameters
    ----------
    queryset: queryset that need to be exported as csv
    fields: fields of a model that will be included in csv
    titles: title for each cell of the csv record
    file_name: the exported csv file name
    """
    model = queryset.model
    response = HttpResponse(content_type='text/csv')
    # force download
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(file_name)
    # the csv writer
    writer = csv.writer(response)
    if fields:
        headers = fields
        if titles:
            titles = titles
        else:
            titles = headers
    else:
        headers = get_model_field_names(queryset.model)
        titles = headers

    # Writes the title for the file
    writer.writerow(titles)

    # write data rows

    lookup_fields = get_lookup_fields(model, fields)
    queryset = queryset.values(*lookup_fields)
    for item in queryset:
        writer.writerow([item[field] if field in item.keys() else '' for field in headers])
    return response