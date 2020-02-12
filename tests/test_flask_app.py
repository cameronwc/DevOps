import pytest

def test_root_responds_200_success(client):
    res = client.get('/')
    assert res.status_code == 200

def test_root_responds_with_correct_data(client):
    res = client.get('/')
    assert b'per month' in res.data