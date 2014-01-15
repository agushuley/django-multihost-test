from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import Context
import gu_multihost


def news_item(ctx, site_name, item_id):
    response = HttpResponse(site_name + " " + item_id, mimetype="text/plain")
    return response


def templates(request):
    return render_to_response("templates.html",
                              Context({'default_site': gu_multihost.get_default_site(),
                                       'current_site': gu_multihost.get_current_site(), })
    )