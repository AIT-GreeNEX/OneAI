from flaskwebgui import FlaskUI
from main import app


FlaskUI(
    app,
    width=1200,
    height=800,
    start_server='flask',
    close_server_on_exit=True
).run()
