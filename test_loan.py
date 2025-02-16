import pytest
from loan_tap import app

@pytest.fixture

def client():
    return app.test_client()

def test_loan_get(client):
    res = client.get("/hello")
    assert res.status_code == 200
    assert res.text == "<h1> welcome to LOAN TAP!!</h2>"


def test_loan_fill_get(client):
    res = client.get("/fill")
    assert res.status_code == 200
    assert res.text == "<h1> fill your details</h2>"

def test_loan_post(client):
    test_data= {
                "ApplicantIncome":10,
                "Credit_History":1.0,
                "Gender":"Male",
                "LoanAmount":111111,
                "Married":"Yes"
                }
    res1 = client.post("/predict",json=test_data)
    assert res1.status_code == 200
    assert res1.json == {"loan_approval_status":"Rejected"}

