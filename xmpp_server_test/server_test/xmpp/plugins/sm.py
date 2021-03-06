# -*- coding: utf-8 -*-
#
# This file is part of django-xmpp-server-test
# (https://github.com/mathiasertl/django-xmpp-server-test).
#
# django-xmpp-server-test is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
#
# django-xmpp-server-test is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# django-xmpp-server-test.  If not, see <http://www.gnu.org/licenses/>.

from sleekxmpp.plugins import BasePlugin
from sleekxmpp.stanza import StreamFeatures
from sleekxmpp.xmlstream import register_stanza_plugin
from sleekxmpp.xmlstream import ElementBase


class SMStanza2(ElementBase):
    """
    XEP-0198 <= 1.1 uses older version namespace.
    """

    name = 'sm'
    namespace = 'urn:xmpp:sm:2'
    interfaces = set()
    plugin_attrib = 'sm'


class SMStanza3(ElementBase):
    name = 'sm'
    namespace = 'urn:xmpp:sm:3'
    interfaces = set()
    plugin_attrib = 'sm'


class feature_sm(BasePlugin):
    """Plugin for Stream Management (XEP-0198).

    .. seealso:: http://www.xmpp.org/extensions/xep-0198.html
    """

    def plugin_init(self):
        self.description = 'XEP-0198: Stream Management'
        self.xmpp.register_feature(
            'sm',
            self._handle_sm,
            restart=False,
            order=self.config.get('order', 0))

        register_stanza_plugin(StreamFeatures, SMStanza2)
        register_stanza_plugin(StreamFeatures, SMStanza3)

    def _handle_sm(self, features):
        pass
