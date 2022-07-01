# Django
from django.db import models

# Create your models here.
class BaseModel(models.Model):
  """Base model.
    It acts as an abstract base class that all other models in the project will inherit from.
    This class provides each table with the following attributes:
      + id(PK): PrimaryKey of the instance.
      + state(Boolean): State of the instance, if it is active or not.
      + created(DateTime): Stores the date and time the instance was created.
      + modified(DateTime): Stores the date and time of the last modification of each instance.
  """

  id = models.AutoField(primary_key = True)
  is_active = models.BooleanField(default = True)
  created_date = models.DateField(auto_now_add=True)
  modified_date = models.DateField(auto_now=True)

  class Meta:
      """Meta definition for BaseModel."""
      abstract = True
      get_latest_by = 'created'
      ordering = ['-created_date', '-modified_date']