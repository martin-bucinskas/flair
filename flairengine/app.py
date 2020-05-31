import os

from flask import request, abort, Response
import flairengine.transcoder.transcoder as transcoder


def init(app, config):

    @app.route('/media/<path:path>.<regex("\\w+"):file_format>')
    def get_transcoded_media(path, file_format):
        start = float(request.args.get('start') or 0)
        vcodec = request.args.get('vcodec')
        acodec = request.args.get('acodec')

        absolute_path = os.getcwd() + '/../flair-storage/media/' + path + '.' + file_format
        print(absolute_path)

        try:
            mime = transcoder.transcode_mime(file_format, config)
            return Response(
                response=transcoder.transcode(absolute_path, start, file_format, vcodec, acodec, config),
                status=200,
                mimetype=mime,
                headers={
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': mime,
                    'Content-Disposition': 'inline',
                    'Content-Transfer-Encoding': 'binary'
                }
            )
        except FileNotFoundError:
            abort(404)
