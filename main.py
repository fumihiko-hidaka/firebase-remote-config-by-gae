import json
import webapp2

from remote_config import RemoteConfigRequest


class RemoteConfigPage(webapp2.RequestHandler):
    def get(self):
        res = RemoteConfigRequest().get()

        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(res))

    def post(self):
        res = {}
        set_value = self._get_post_value()

        if set_value is not None:
            res = RemoteConfigRequest().put({
                'test_value': set_value,
            })

        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(res))

    def _get_post_value(self):
        if "value" in self.request.POST:
            set_value = self.request.POST["value"]
            if isinstance(set_value, str) or isinstance(set_value, unicode):
                return set_value

        return None


app = webapp2.WSGIApplication([
    ('/remote_config', RemoteConfigPage),
])
