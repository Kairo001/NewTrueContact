#Django
from django.db import models
from django.utils.translation import gettext as _

# Base model
from apps.base.models import BaseModel

# Models
from apps.users.models import UserProfile

class Label(models.Model):
  """Model definition for Label."""

  name = models.CharField(_("Name"), max_length=50)

  class Meta:
    """Meta definition for Label."""

    verbose_name = 'Label'
    verbose_name_plural = 'Labels'

  def __str__(self):
    """Unicode representation of Label."""
    return self.name

class Type(models.Model):
  """Model definition for Type."""

  name = models.CharField(_("Name"), max_length=50)
  label = models.ManyToManyField(Label)

  class Meta:
    """Meta definition for Type."""

    verbose_name = 'Type'
    verbose_name_plural = 'Types'

  def __str__(self):
    """Unicode representation of Type."""
    return self.name

class DataProfile(models.Model):
  """Model definition for DataProfile."""

  user_profile = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name="data")
  label = models.ForeignKey(Label, on_delete=models.PROTECT)
  type = models.ForeignKey(Type, on_delete=models.PROTECT)
  data = models.CharField(_("Data"), max_length=50)

  class Meta:
    """Meta definition for DataProfile."""

    verbose_name = 'DataProfile'
    verbose_name_plural = 'DataProfiles'

  def __str__(self):
    """Unicode representation of DataProfile."""
    return self.user_profile.get_full_name()
