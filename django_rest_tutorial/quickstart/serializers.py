# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import User, Group

from rest_framework import serializers


class UserSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'username', 'email', 'groups')


class GroupSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
