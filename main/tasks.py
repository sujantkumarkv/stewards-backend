import os
import requests
from background_task import background, tasks
from logging import getLogger

from .models import WorkStream

logger = getLogger(__name__)

apiKey = os.environ["DUNE_API_KEY"]


def duneQueryResults(query_id):
    url = f"https://api.dune.com/api/v0/query/{query_id}/results"
    response = requests.get(url, headers={'X-Dune-API-Key': apiKey})
    return response.json()


def query_id_from_url(dune_url):
    return int(dune_url.split('/')[4])


@background
def update_workstreams():
    workstreams = WorkStream.objects.all()
    print("All Workstreams", workstreams)
    for w in workstreams:
        print(f"Updating Workstream: {w.short_name}")
        w.stats.gtc_balance = duneQueryResults(
            query_id_from_url(w.current_gtc_num))
        w.stats.stable_coin_balance = duneQueryResults(
            query_id_from_url(w.current_stable_num))
        w.stats.stable_graph = duneQueryResults(
            query_id_from_url(w.current_stable_graph))
        w.stats.gtc_graph = duneQueryResults(
            query_id_from_url(w.current_gtc_graph))
        w.stats.all_time_contributors = duneQueryResults(
            query_id_from_url(w.all_time_contributors))
        w.stats.save()
        w.save()


update_workstreams(schedule=60, repeat=3600)
