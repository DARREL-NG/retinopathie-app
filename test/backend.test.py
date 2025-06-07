# tests/backend.test.py
import io, pytest
from backend.app import app

@pytest.fixture
def client():
    app.config['TESTING']=True
    return app.test_client()

def test_no_file(client):
    r=client.post('/predict',data={})
    assert r.status_code==400

def test_dummy_image(client):
    img=io.BytesIO(b'\x89PNG\r\n\x1a\n'+b'\x00'*100)
    data={'image':(img,'img.png')}
    r=client.post('/predict',data=data,content_type='multipart/form-data')
    assert r.status_code==200
    d=r.get_json()
    assert 'code' in d and 'label' in d
