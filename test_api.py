#!pytest test_api .v
import requests,pytest

@pytest.fixture
def dynamic_user():
    users_response = requests.get("https://dummyjson.com/users?limit=1")
    assert  users_response.status_code == 200 , f"Error al obtener usuarios : {users_response.txt}"
    users = users_response.json()
    user = users ["users"][0]
    return user

def test_login_api_dynamic_user(dynamic_user): #"users": ["alexis"]
    user = dynamic_user
    payload ={
        "username": user["username"],
        "password": user["password"]
        }
    
    response = requests.post("https://dummyjson.com/auth/login", json=payload)
    
    if response.status_code != 200:
        #fulanito : 403:forbbiden
        print ("USER:",user)
        print("ESTATUS:",response.status_code)
        print("RESPONSE:",response.text)
        
    assert response.status_code == 200, f"login fallo:{response.text}"
    json_data = response.json()
    
    #cambio a accesstoken
    assert "accessToken" in json_data, f"no se genero accessToken:{json_data}"
    assert json_data.get("username")==user["username"],"el username no coincide"
    
def test_login_invalid_password(dynamic_user):
    user = dynamic_user
    payload ={
        "username":user["username"],
        "password":"contraseña_incorrecta"
        }
    
    response = requests.post(
        "https://dummyjson.com/auth/login",
        json=payload
        )
    
    assert response.status_code == 400, f"Esperada 400, pero recibio {response.status_code}"
    json_data = response.json()
    assert "message" in json_data, "no se recibio mensaje de error"
    assert json_data ["message"]=="Invalid credentials", f"Mensaje insesperado: {json_data["message"]}"