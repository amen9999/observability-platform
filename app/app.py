from flask import Flask
import logging

from prometheus_client import Counter
from prometheus_client import generate_latest
from prometheus_client import CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP Requests'
)

logging.basicConfig(
    filename='logs/application.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

@app.route('/')
def home():

    REQUEST_COUNT.inc()

    logging.info("Home page visited")

    return "Observability Platform Running"

@app.route('/health')
def health():

    REQUEST_COUNT.inc()

    logging.info("Health endpoint called")

    return {"status": "UP"}

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {
        'Content-Type': CONTENT_TYPE_LATEST
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)