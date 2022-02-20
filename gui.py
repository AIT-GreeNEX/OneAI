from flaskwebgui import FlaskUI
from main import app

FlaskUI(
    app,
    width = 1000,
    height = 800,
    maximized = True,
    start_server = 'flask',
    close_server_on_exit=True
).run()
