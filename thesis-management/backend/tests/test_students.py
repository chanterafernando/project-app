STUDENT = {
    "first_name": "Ana",
    "last_name": "Torres",
    "email": "ana.torres@uni.edu.ec",
    "school": "Mathematical and Computational Sciences",
}


def test_list_students_empty(client):
    response = client.get("/api/students")
    assert response.status_code == 200
    assert response.json() == []


def test_create_student(client):
    response = client.post("/api/students", json=STUDENT)
    assert response.status_code == 201
    data = response.json()
    assert data["student_id"] == 1
    assert data["email"] == STUDENT["email"]


def test_create_student_duplicate_email(client):
    client.post("/api/students", json=STUDENT)
    response = client.post("/api/students", json={**STUDENT, "email": "ANA.TORRES@uni.edu.ec"})
    assert response.status_code == 409


def test_create_student_invalid_email(client):
    response = client.post("/api/students", json={**STUDENT, "email": "no-es-un-email"})
    assert response.status_code == 422


def test_get_student_by_id(client):
    created = client.post("/api/students", json=STUDENT).json()
    response = client.get(f"/api/students/{created['student_id']}")
    assert response.status_code == 200
    assert response.json()["last_name"] == "Torres"


def test_get_student_not_found(client):
    assert client.get("/api/students/999").status_code == 404
