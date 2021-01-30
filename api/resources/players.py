from flask import Response, request
from models.players import Player
from flask_restful import Resource
from flask_paginate import get_page_args
from urllib.parse import unquote


class PlayerResource(Resource):

    @staticmethod
    def get():
        """Lists chess players' information with extended features such as filtering and pagination."""

        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

        rank = request.args.get('rank', None)
        name = request.args.get('name', None)
        rating = request.args.get('rating', None)

        payload = {}

        if rank is not None: payload['rank'] = int(rank)
        if name is not None: payload['name'] = unquote(name)
        if rating is not None: payload['rating'] = int(rating)

        player = Player.objects.filter(__raw__=payload).skip(offset).limit(per_page).to_json()

        return Response(player, mimetype="application/json", status=200)

    @staticmethod
    def post():
        """Adds new chess players by validating them."""
        payload = request.get_json()
        new_item = Player(**payload).save()
        return Response(new_item.to_json(), mimetype="application/json", status=201)
