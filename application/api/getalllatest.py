from flask_restful import Resource
from application.models import Comic
from application.parsers.parser import Parser
from application.api.getlatest import GetLatest
from flask import jsonify
import logging

class GetAllLatest(Resource):
    def get(request):
        fingerpori = GetLatest.get(request, "fingerpori")
        xkcd = GetLatest.get(request, "xkcd")
        smbc = GetLatest.get(request, "smbc")
        vw = GetLatest.get(request, "vw")
        fokit = GetLatest.get(request, "fokit")
        redmeat = GetLatest.get(request, "redmeat")
        pbf = GetLatest.get(request, "pbf")
        luonto = GetLatest.get(request, "luonto")

        return jsonify([fingerpori.json(), xkcd.json(), smbc.json(), vw.json(), fokit.json(), redmeat.json(), pbf.json(), luonto.json()])
