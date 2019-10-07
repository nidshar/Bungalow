from django.core.management.base import BaseCommand, CommandError
from home.models import Home
import csv
import psycopg2
import datetime

class Command(BaseCommand):
    help = 'Import Data'

    def handle(self, *args, **options):
        self.stdout.write("Importing Home data...")
        get_data("/home/nidhi/repo/Bungalow/RentalHomes/home/management/data/challenge_data.csv")
        self.stdout.write(self.style.SUCCESS('Successfully imported Homes'))

    
def get_data(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        header_row =  next(reader)
        row_data = {}
        for row in reader:
            for index in range(23):
                if not row[index]:
                    row[index] =None
                if header_row[index] in ["last_sold_date","rentzestimate_last_updated","zestimate_last_updated"]:
                    if row[index]:
                        row[index] =  datetime.datetime.strptime(row[index], '%m/%d/%Y').strftime('%Y-%m-%d')
                row_data[header_row[index]] = row[index]
                
            try:
                Home.objects.get(**row_data)
            except Home.DoesNotExist:
                Home.objects.create(**row_data)
        f.close()
                    
    