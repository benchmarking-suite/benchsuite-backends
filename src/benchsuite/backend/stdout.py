# Benchmarking Suite
# Copyright 2014-2017 Engineering Ingegneria Informatica S.p.A.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Developed in the ARTIST EU project (www.artist-project.eu) and in the
# CloudPerfect EU project (https://cloudperfect.eu/)
import logging

import datetime
import pytz
from pymongo import MongoClient
from benchsuite.core.model.storage import StorageConnector
from benchsuite.core.model.execution import ExecutionResult

logger = logging.getLogger(__name__)


class StdOutStorageConnector(StorageConnector):

    def save_execution_error(self, exec_error):
        print(exec_error)

    def save_execution_result(self, execution_result: ExecutionResult):
        print(execution_result)

    @staticmethod
    def load_from_config(config):
        o = StdOutStorageConnector()
        return o


