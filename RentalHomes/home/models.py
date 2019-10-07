from django.db import models

class Home(models.Model):
    HOME_TYPES = [
        ["SingleFamily", "Single Family"],
        ["VacantResidentialLand", "Vacant Residential Land"],
        ["Miscellaneous", "Miscellaneous"],
        ["MultiFamily2To4", "MultiFamily2To4"],
        ["Apartment", "Apartment"],
        ["Condominium","Condominium"],
        ["Duplex","Duplex"],
        ["Condominium","Condominium"]
    ]
    
   
    area_unit = models.CharField(max_length = 5, default= "SqFt" )
    bathrooms = models.FloatField(null=True, blank=True)
    bedrooms =  models.IntegerField(null=True, blank=True)
    home_size =  models.IntegerField(null=True, blank=True)
    home_type = models.CharField(max_length = 25 ,choices=HOME_TYPES, default="SingleFamily")
    last_sold_date = models.DateField(null=True, blank=True)
    last_sold_price =models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=0)
    link = models.URLField(max_length=250,null=True, blank=True )
    price = models.CharField(max_length=25, null=True, blank=True) 
    property_size = models.IntegerField(null=True, blank=True)
    rent_price = models.DecimalField(null=True, blank=True, max_digits=10,decimal_places=0)
    rentzestimate_amount = models.DecimalField(null=True, blank=True, max_digits=10,decimal_places=0)
    rentzestimate_last_updated= models.DateField(null=True, blank=True)
    tax_value = models.DecimalField(null=True, blank=True,max_digits=10, decimal_places=0)
    tax_year = models.IntegerField(null=True, blank=True)
    year_built = models.IntegerField(null=True, blank=True)
    zestimate_amount = models.DecimalField(null=True, blank=True, max_digits=10,decimal_places=0)
    zestimate_last_updated = models.DateField(null=True, blank=True)
    zillow_id = models.DecimalField(primary_key=True,max_digits=10,decimal_places=0)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=25,null=True, blank=True)
    state = models.CharField(max_length=25,null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    
