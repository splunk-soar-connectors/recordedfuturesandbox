# File: recordedfuturesandbox_test_api.py
#
# Copyright (c) 2022-2023 Recorded Future, Inc.
#
# This unpublished material is proprietary to Recorded Future. All
# rights reserved. The methods and techniques described herein are
# considered trade secrets and/or confidential. Reproduction or
# distribution, in whole or in part, is forbidden except by express
# written permission of Recorded Future.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.

from .recordedfuturesandbox_api import TriageAPI


def test_api_path():
    api = TriageAPI("apikey", api_path="/v0/")
    assert api.api_url == "https://api.tria.ge/v0"
