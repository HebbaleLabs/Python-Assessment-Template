from flask import Flask
import connexion
from swagger_server import encoder
from flask_cors import CORS

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username


# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

application = Flask(__name__)

if __name__ == '__main__':

    # EB looks for an 'application' callable by default.
    application = connexion.FlaskApp(__name__, specification_dir='./swagger_server/swagger/', swagger_ui=True)

    application.debug = False

    # add a rule for the index page.
    application.add_url_rule('/', 'index', (lambda: header_text +
                                                    say_hello() + instructions + footer_text))

    # add a rule when the page is accessed with a name appended to the site
    # URL.
    application.add_url_rule('/<username>', 'hello', (lambda username: header_text +
                                                                       say_hello(username) + home_link + footer_text))

    application.app.json_encoder = encoder.JSONEncoder
    application.add_api('swagger.yaml', arguments={'title': 'FundsCorner Customer Acquisition System API'})

    CORS(application.app)
    assert isinstance(application.run, object)
    application.run(host='0.0.0.0')
