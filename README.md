## Getting Started
**To run it locally:**

*1. Create a virtualenv:*
```bash
virtualenv venv
source venv/bin/activate
```
*2. Install dependencies:*

```bash
pip install -r requirements.txt
```

*3. Run migration:*

```bash
python manage.py migrate
```

*4. Run server:*

```bash
python manage.py runserver
```

**To run it using Docker**

```bash
docker compose up -d
```

**API**

*Endpoint*

```python
http://localhost:8000/weather/api/v1/forecast
```
*Method:* POST

*Payload*
```json
{
    "lat": 33.44,
    "lon": -94.04,
    "detailing_type": "hourly"
}
```