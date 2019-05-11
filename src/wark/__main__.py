import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)

if SRC not in sys.path:
    sys.path.insert(0, SRC)

import wark.server
import wark.settings


app = wark.server.app

app.run(
    host=wark.settings.HOSTNAME,
    port=wark.settings.PORT,
)
