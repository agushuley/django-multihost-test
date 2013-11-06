from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.


def news_item(ctx, site_name, item_id):
    response = HttpResponse(site_name + " " + item_id, mimetype="text/plain")
    return response


def templates(ctx):
    return render_to_response("templates.html")