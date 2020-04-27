import os, random
from app import ( app )
from app.query_helper import ( init_db )

if __name__ == "__main__":
    print('\n\n\n> Running init db', random.random(), '\n')
    init_db()
    app.run(debug=True, port=1337)