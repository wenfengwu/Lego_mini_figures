from miniFig_app import app
import os

if __name__ == "__main__":
    app.run(
        host='0.0.0.0', 
        port=int(os.getenv('POST', 5000)),
        debug=bool(os.getenv('DEBUG', 'True'))
    )