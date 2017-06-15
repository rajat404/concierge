# -*- coding: utf-8 -*-
from django.apps import apps

from .. import exceptions as exc


def get_object(app_name, model_name, **kwargs):
    """
    Takes the name of the App, Model, and Filter kwargs
    """
    model_cls = apps.get_model(app_name, model_name)
    try:
        return model_cls.objects.get(**kwargs)
    except model_cls.DoesNotExist:
        return None


def get_qs(app_name, model_name, **kwargs):
    """
    Takes the name of the App, Model, and Filter kwargs
    """
    model_cls = apps.get_model(app_name, model_name)
    try:
        return model_cls.objects
    except model_cls.DoesNotExist:
        return None


def create_instance(serializer, payload):
    """
    Takes a serializer & it's payload as args, and creates an instance

    If the serializer returns an object on successful creation/updation,
    then object is returned, else None

    If an error occurs, then `BadRequest` exception is raised,
    with serializer errors
    """
    serializer_instance = serializer(data=payload)
    if serializer_instance.is_valid():
        obj = serializer_instance.save()
        if obj:
            return obj
        else:
            return None
    else:
        raise exc.BadRequest(dict(serializer_instance.errors))
