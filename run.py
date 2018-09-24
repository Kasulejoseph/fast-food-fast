from app import app
from app.api.views import routes
if __name__ == '__main__':
    app.run(debug=True)