from app import (
    app,
)
from app.query_helper import (
    init_db
)
import os

if __name__ == "__main__":
    init_db()
    print('Start init db')
    app.run(debug=True, port=1337)