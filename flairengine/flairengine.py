from flask import Flask
from werkzeug.routing import BaseConverter
import flairengine.app as flair_engine
import flairengine.configloader as config_loader

app = Flask(__name__)


class RegexConverter(BaseConverter):

    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter


@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    response.cache_control.no_cache = True
    response.cache_control.must_revalidate = True
    response.cache_control.proxy_revalidate = True
    return response


config = config_loader.load_configs()

flair_engine.init(app, config)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config['engine']['port'], threaded=True, debug=False)
