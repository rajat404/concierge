# -*- coding: utf-8 -*-
# Standard Library
import uuid

# Third Party Stuff
from autoslug import AutoSlugField
from django.db import models
from uuid_upload_path import upload_to
from versatileimagefield.fields import PPOIField, VersatileImageField


class UUIDModel(models.Model):
    """ An abstract base class model that makes primary key `id` as UUID
    instead of default auto incremented number.
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class TimeStampedSlugModel(TimeStampedModel):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    It also has a ``name`` field, and it's subsequent auto-generated ``slug``
    """
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        abstract = True


class TimeStampedUUIDModel(UUIDModel, TimeStampedModel):
    """An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields with UUID as primary_key field.
    """

    class Meta:
        abstract = True


class TimeStampedSlugUUIDModel(UUIDModel, TimeStampedSlugModel):
    """An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields with UUID as primary_key field.
    It also provides a `name` field and a self-forming `slug` field,
    based on that name
    """

    class Meta:
        abstract = True


class ImageMixin(models.Model):
    """An abstract base class model that provides a VersatileImageField Image with POI
    """

    image = VersatileImageField(upload_to=upload_to, blank=True, null=True, ppoi_field='image_poi',
                                verbose_name="image")
    image_poi = PPOIField(verbose_name="image's Point of Interest")  # point of interest

    class Meta:
        abstract = True
