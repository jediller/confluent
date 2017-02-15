# Copyright 2017 Lenovo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class NodeHandler(object):

    def __init__(self, info, configmanager):
        self.info = info
        self.configmanager = configmanager
        targsa = None
        # first let us prefer LLA if possible, since that's most stable
        for sa in info['addresses']:
            if sa[0].startswith('fe80'):
                targsa = sa
                break
        else:
            targsa = info['addresses'][0]
        self.ipaddr = targsa[0]
        return

    def probe(self):
        # Use appropriate direct strategy to gather data such as
        # serial number and uuid to flesh out data as needed
        return

    def preconfig(self):
        return

    @property
    def discoverable_by_switch(self):
        return True