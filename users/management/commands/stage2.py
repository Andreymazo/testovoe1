from django.core.management import BaseCommand

class Command(BaseCommand):  ##Chtobi file ispolnialsya nado zaregistrirovat prilozhenie

    def handle(self, *args, **options):
        print('_________________ Stage1 _______________________')
