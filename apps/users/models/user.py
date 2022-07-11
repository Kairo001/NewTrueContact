# Django
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser

class UserAccountManager(BaseUserManager):
  """Manager of User model."""
  def _create_user(self, first_name, last_name, username, password, is_staff, is_superuser, **extra_fields):

    if not username:
      raise ValueError('Users must have an username.')
    
    user = self.model(
      first_name = first_name,
      last_name = last_name,
      username = self.normalize_email(username),
      is_staff = is_staff,
      is_superuser = is_superuser,
      **extra_fields
    )

    user.set_password(password)
    user.save(using=self._db)

  def create_user(self, first_name, last_name, username, password=None, **extra_fields):
    return self._create_user(first_name, last_name, username, password, False, False, **extra_fields)

  def create_superuser(self, first_name, last_name, username, password, **extra_fields):
    return self._create_user(first_name, last_name, username, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
  """Model definition for User."""

  first_name = models.CharField(_("First name"), max_length=64)

  last_name = models.CharField(_("Last name"), max_length=64)

  image = models.ImageField(_('Profile picture'), upload_to='user_pictures/', blank=True, null=True)

  username = models.CharField(
        _("username"),
        max_length=64,
        unique=True,
        help_text=_(
            "Required. 64 characters or fewer."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

  is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
  
  is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
  
  objects = UserAccountManager()

  REQUIRED_FIELDS =  ['first_name', 'last_name']
  USERNAME_FIELD = "username"

  class Meta:
    """Meta definition for User."""

    verbose_name = 'User'
    verbose_name_plural = 'Users'

  def __str__(self):
    """Unicode representation of User."""
    return self.username

  def get_short_name(self):
    return self.first_name

  def get_full_name(self):
    return f"{self.first_name} {self.last_name}"
  
