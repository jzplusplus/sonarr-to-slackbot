__author__ = 'jzplusplus'

import json
from slacker import Slacker
import BaseHTTPServer

channel = '#yourchannelhere'
slack = Slacker('yourapikeyhere')

HOST_NAME = 'localhost'
PORT_NUMBER = 8000


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('OK')
        self.wfile.close()

        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)

        data = json.loads(post_body)

        output = 'Downloaded "' + str(data['Series']['Title']) + '"\n' + \
                'S' + str(data['Episodes'][0]['SeasonNumber']) + ' E' + \
                str(data['Episodes'][0]['EpisodeNumber']) + ', "' + \
                str(data['Episodes'][0]['Title']) + '" (' + str(data['Episodes'][0]['Quality']) + ')'

        slack.chat.post_message(channel, output, as_user=True)

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print 'Starting sonarrToSlackbot server'
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print 'Stopping sonarrToSlackbot server...'
