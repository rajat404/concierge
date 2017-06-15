# -*- coding: utf-8 -*-
from concierge.base.models import UUIDModel
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """Creates and saves a User with the given email and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class UserType(models.Model):
    kind = models.CharField(max_length=30)

    class Meta:
        db_table = 'users_usertype'
        verbose_name = _('UserType')
        verbose_name_plural = _('UserTypes')


@python_2_unicode_compatible
class User(AbstractBaseUser, UUIDModel, PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )

    # TSHIRT_SIZE_CHOICES = (
    #     ('U', 'UNDECIDED'),
    #     ('S', 'S'),
    #     ('M', 'M'),
    #     ('L', 'L'),
    #     ('XL', 'XL'),
    #     ('XXL', 'XXL'),
    # )

    first_name = models.CharField(_('First Name'), max_length=120, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=120, blank=True)
    email = models.EmailField(_('email address'), unique=True, db_index=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text='Designates whether the user can log into this admin site.')

    is_active = models.BooleanField('active', default=True,
                                    help_text='Designates whether this user should be treated as '
                                              'active. Unselect this instead of deleting accounts.')
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    institution = models.CharField(max_length=100, blank=True)
    # kind = models.ManyToManyField(UserType)
    github_username = models.CharField(max_length=100, blank=True)
    twitter_username = models.CharField(max_length=100, blank=True)
    contact = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    # tshirt_size = models.CharField(max_length=1, choices=TSHIRT_SIZE_CHOICES, default='U')

    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        db_table = 'users_users'
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined', )

    def __str__(self):
        return str(self.id)

    def get_full_name(self):
        """Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Returns the short name for the user.
        """
        return self.first_name.strip()
