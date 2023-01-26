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

    Guest ||--|{ Login : can
    Guest ||--|{ Logout : can
    Guest {
        Display home_html
        Buttom Login
        Buttom CreateAccount 
    }
    Login{
        Display Login_html
        Message LoginSuccess
        Error LoginFailure "User can choose to create an account."
        Buttom CreateAccount
    }

    Login ||--|{ User : as
    User{
        Display home_html
        Buttom Personal_and_Vehicle_Info "Editable"
        Buttom Request_Ride
        Buttom Driver_Status "Editable"
    }

    User ||--|{ RideRequesting : Rider_Owner_Start_Requesting
    RideRequesting{
        Display InfoFilling_html "Or just a Window"
        Blank Destination_Address
        Blank Arrial_Date_Time
        Blank Passenger_Number
        Blank Vehicle_Type "Optional"
        Blank Special_Request "Optional and free-text fields"
        Choose Share_Or_Not "joined by other ride sharers"
        Choose Confirm "Start requesting"
    }
    RideRequesting ||--|{ ConfirmRideRequesting : Confirm
    ConfirmRideRequesting |o--|{ RideRequesting : Edit
    ConfirmRideRequesting{
        Display Open_ride_details
        Choose Edit "Unaccessable after being confirmed by drivers"
    }
    ConfirmRideRequesting ||--|{ Ride : RideOwner_Confirm
    Ride{
        Display home_html
        Display Ride_status_Window "Pop up a Window"

    }
```
