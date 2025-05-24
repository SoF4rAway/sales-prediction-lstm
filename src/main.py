from flask import Flask


def app_build():
    app = Flask(__name__)
    from views import views
    app.register_blueprint(views, url_prefix='/')
    return app


app = app_build()
if __name__ == '__main__':
    app.run(debug=True)
