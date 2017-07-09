# -*- coding: utf-8 -*-
from django.apps import apps


def get_object(app_name, model_name, **kwargs):
    """
    Returns a model object if it exists, else None
    """
    model_cls = apps.get_model(app_name, model_name)
    try:
        return model_cls.objects.get(**kwargs)
    except model_cls.DoesNotExist:
        return None


def get_manager(app_name, model_name):
    """
    Returns the queryset manager of the specified model
    """
    model_cls = apps.get_model(app_name, model_name)
    try:
        return model_cls.objects
    except model_cls.DoesNotExist:
        return None


def create_instance(serializer):
    """
    Takes a serializer and creates an instance

    If the serializer returns an object on successful creation/updation,
    then object is returned, else None

    If an error occurs, then `BadRequest` exception is raised,
    with serializer errors
    """
    serializer.is_valid(raise_exception=True)
    obj = serializer.save()
    return obj or None
