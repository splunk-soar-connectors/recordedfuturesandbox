# Copyright (C) 2021 Hatching B.V.
# Recorded Future Sandbox
# All rights reserved.

from .hatching_triage_api import TriageAPI


def test_api_path():
    api = TriageAPI("apikey", api_path="/v0/")
    assert api.api_url == "https://api.tria.ge/v0"
