from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.utils import LayerMapping

from gc_geography.models import Baranggay


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        existing = Baranggay.objects.all()
        existing.delete()

        if len(args) == 1:
            shape_file_name = args[0]
        else:
            print 'Usage: python manage.py load_baranggays <baranggay shape file>'
            return

        shape_datasource = DataSource(shape_file_name)
        layer = shape_datasource[0]
        print layer.fields

        mapping = {
            'name': 'NAME_3',
            'polygon': 'POLYGON'
        }
        layer_mapping = LayerMapping(Baranggay, shape_file_name, mapping)
        layer_mapping.save(verbose=True)

