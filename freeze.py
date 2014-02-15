# -*- coding: utf-8 -*-
import os

from flask_frozen import Freezer

from sublee import app


@app.route('/404.html')
def not_found():
    client = app.test_client()
    response = client.get('/404')
    return response.data


if os.path.exists('../gh-pages'):
    app.config['FREEZER_DESTINATION'] = '../gh-pages'
    app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'runker', 'CNAME']
freezer = Freezer(app, with_static_files=False)


if __name__ == '__main__':
    freezer.freeze()
