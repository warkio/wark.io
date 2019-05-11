import os

import sanic
from sanic import response

from wark.templates import render


app = sanic.Sanic()


@app.route('/')
async def home(req):
    return response.html(await render('index.html'))
