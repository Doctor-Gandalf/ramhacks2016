from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.db.models import F
from django.contrib.auth import authenticate, login

