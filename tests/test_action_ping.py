# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and

from networking_utils_base_test_case import NetworkingUtilsBaseActionTestCase

from ping import Ping

__all__ = [
    'PingActionTestCase'
]


class PingActionTestCase(NetworkingUtilsBaseActionTestCase):
    __test__ = True
    action_cls = Ping

    def test_run_ping_google_dns(self):
        action = self.get_action_instance()

        (success, result) = action.run("8.8.8.8", force_success=True)

        self.assertTrue(success)
