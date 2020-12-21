import json
from pathlib import Path

import responses
from helpjuice import Client
from requests import Request

helpjuice = Client(account="your-account", api_key="your-account-api-key")

with Path(__file__).parent.joinpath("responses.json").open() as f:
    responses_json = json.load(f)

meta = {"meta": responses_json.pop("meta")}
limit = meta["meta"]["current"]


def get_url(endpoint, **kwargs):
    pr = Request("GET", f"{helpjuice.host}{endpoint}", params=kwargs).prepare()

    return pr.url.rstrip("/")


@responses.activate
def collection_tester(collection, key, **kwargs):
    collection_json = responses_json[key]
    endpoint = collection_json["endpoint"]

    for method, j in collection_json.items():
        if method == "endpoint":
            continue

        responses.add(
            method,
            get_url(endpoint),
            json={**meta, **{key: j}},
        )

        c = collection()
        response = getattr(collection, method.lower())(c, limit=limit, **kwargs)

        assert response == j


@responses.activate
def resource_tester(resource, key):
    resource_json = responses_json[key]
    endpoint = resource_json["endpoint"]

    for method, j in resource_json.items():
        if method == "endpoint":
            continue

        resource_id = j.setdefault("id", 1 if method != "POST" else "")

        if isinstance(endpoint, dict):
            for m, e in endpoint.items():
                responses.add(
                    m,
                    get_url(f"{e}/{resource_id}"),
                    json={key: j},
                )
        else:
            responses.add(
                method,
                get_url(f"{endpoint}/{resource_id}"),
                json={key: j},
            )

        r = resource(id=resource_id)
        response = getattr(resource, method.lower())(r)

        assert response == j


def test_activities():
    collection_tester(helpjuice.Activities, "activities")


def test_activity():
    resource_tester(helpjuice.Activity, "activity")


def test_articles():
    collection_tester(helpjuice.Articles, "articles")


def test_article():
    resource_tester(helpjuice.Article, "article")


def test_categories():
    collection_tester(helpjuice.Categories, "categories")


def test_category():
    resource_tester(helpjuice.Category, "category")


def test_groups():
    collection_tester(helpjuice.Groups, "groups")


def test_group():
    resource_tester(helpjuice.Group, "group")


def test_search():
    collection_tester(helpjuice.Search, "search", query="your-query")


def test_settings():
    resource_tester(helpjuice.Settings, "settings")


def test_users():
    collection_tester(helpjuice.Users, "users")


def test_user():
    resource_tester(helpjuice.User, "user")
