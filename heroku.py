import os
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
USERAGENT = os.environ["USERAGENT"]