# Web-APP_Ride-Sharing-Service


Go to ./docker-deploy/web-app/Ride_Sharing_Service/

Start your server by
```
python3 manage.py runserver 0:8000
```
*Using 0.0.0.0 means the server runs on "all" interfaces on the machine, including the one which has a public IP.

Then go to http://vcm-30579.vm.duke.edu:8000/ or http://vcm-30900.vm.duke.edu:8000/

# Project Overview
```mermaid
  erDiagram
    User }o--|{ Login : can
    User }o--|{ Logout : can
    User {
        Dispaly home_html
        Buttom Login
        Buttom CreateAccount 
    }
    
    Login ||--|{ Rider : as
    Login ||--|{ Driver : as
    Login{
        Display Login_html
        Message LoginSuccess
        Error LoginFailure "User can choose to create an account."
        Buttom CreateAccount
    }

    Rider {
        Display home_html
        Buttom Personal_and_Vehicle_Info "Editable"
        Buttom Request_Ride
    }

    Driver {
        Display home_html
        Buttom Personal_and_Vehicle_Info "Editable"
    }

    Rider }|--|{ Ride : Request


```
