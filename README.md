# Web-APP_Ride-Sharing-Service

After ```git pull```, Go to ./docker-deploy/web-app/Ride_Sharing_Service/Ride_Sharing_Service/settings.py

Change database based on your own

Then back to last directory:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Go to ./docker-deploy/web-app/Ride_Sharing_Service/

Start your server by
```
python3 manage.py runserver 0:8000
```
*Using 0.0.0.0 means the server runs on "all" interfaces on the machine, including the one which has a public IP.

Then go to http://vcm-30579.vm.duke.edu:8000/ or http://vcm-30900.vm.duke.edu:8000/

# Table of Contents
- [Project Overview](#Project-Overview)
  - [Project Design](#Project-Design)
  - [Web Deployment](#Web-Deployment)
- [Function](#Function)
  - [Account](#Account)
  - [Owner](#WOwner)
  - [Sharer](#Sharer)
  - [Driver](#Driver)

# Project Overview
## Project Design
```mermaid
erDiagram
    Guest ||--|{ CreateAccount : can
    Guest ||--|{ Login : can
    CreateAccount ||--|{ Login : to_
    Failure ||--|{ CreateAccount : can

    Login ||--|{ Failure : if
    Guest {
        Display home_html
        Buttom Login
        Buttom CreateAccount 
    }
    CreateAccount{
        Display CreateAccount_html
        Blank UserName
        Blank Password
    } 
    Login{
        Display Login_html
    }
    Failure{
        Display Failure_Message "Pop a Window"
        Buttom CreateAccount
        Buttom Retry
    }
    
    Login ||--|{ User : as
    User ||--|{ Logout : can
    User ||--|{ Register_as_Driver : can
    Register_as_Driver ||--|{ User : Back_to
    User{
        Display home_html
        Buttom Profile "Editable"
        Buttom Request_Ride
        Buttom Search_for_Open_Ride
        Buttom View_Ride_Status "If exists on-going ride, show it."
        Buttom Register_as_Driver "Avaliable only not is Driver"
        Buttom Vehicle_Info "Edit Avaliable only is Driver"
        Buttom Driver_status "Edit Avaliable only is Driver"
        Buttom Search_for_Open_Ride_Request "Avaliable only is Driver"
    } 
    Register_as_Driver{
        Display Registed_as_Driver "Pop a Window"
        Blank Name
        Blank Vehicle_Type
        Blank license_Plate_Number
        Blank Vehicle_Capacity
        Blank Special_Vehicle_Info "Optional"
        Buttom Confirm
    }

    User ||--|{ Owner : as
    User ||--|{ Sharer : as
    User ||--|{ Driver : as
    Owner{
        Display Please_Enter_Info
        Buttom Cancel
    }
    Sharer{
        Display Search_Open_Ride_Requests
        Buttom Cancel
    }
    Driver{
        Display Search_Open_Ride_Requests
        Buttom Cancel
    }

    Owner ||--|{ Request_Info_of_Owner : enter
    Request_Info_of_Owner ||--|{ Waiting_for_Driever : if_NotShared
    Open_Ride_List ||--|{ Request_Info_of_Owner : can_edit
    Waiting_for_Driever ||--|{ Request_Info_of_Owner : can_edit

    Request_Info_of_Owner{
        Display InfoFilling_html "Or Pop a Window"
        Blank Destination_Address
        Blank Arrial_Date_Time
        Blank Number_of_Passenger
        Blank Vehicle_Type "Optional"
        Blank Special_Request "Optional and free-text fields"
        Buttom Share_Or_Not "Can be joined by other ride sharers"
        Buttom Confirm "Start requesting"
    }
    Open_Ride_List{
        Display Waiting_Status "Window"
        DisplayInfo Ride_Details "From request info"
        DisplayInfo sharers_name "Sharers joining the ride"
        Buttom Edit "Only avaliable for owner"
    }
    Waiting_for_Driever{
        Display Waiting_Status "Window"
        DisplayInfo Ride_Details "From original request info"
        Buttom Edit
    }

    Sharer ||--|{ Request_Info_of_Sharer : enter
    Request_Info_of_Sharer ||--|{ Open_Ride_Lists : can_see
    Open_Ride_Lists ||--|{ Open_Ride_List : can_join
    Open_Ride_Lists ||--|{ Open_Ride_List2 : can_join
    Open_Ride_Lists ||--|{ Open_Ride_List3 : can_join
    Open_Ride_List2 ||--|{ Open_Ride_Lists : can_cancel
    Open_Ride_List3 ||--|{ Open_Ride_Lists : can_cancel
    Open_Ride_Lists ||--|{ Request_Info_of_Sharer : Re-enter
    Request_Info_of_Owner ||--|{ Open_Ride_List : if_Shared

    Request_Info_of_Sharer{
        Display InfoFilling_html "Or pop a window"
        Blank Destination_Address
        Blank Earliest_Arrival_Time "Should be in arrival window"
        Blank Latest_Arrival_Time "Should be in arrival window"
        Blank Number_of_Passenger
    }
    Open_Ride_Lists{
        Display All_Open_Ride_List "must match Sharer's request info"
        Buttom Choose
        Buttom Re-enter
    }
    Open_Ride_List2{
        Display Waiting_Status "Window"
        DisplayInfo Ride_Details "From request info"
        DisplayInfo sharers_name "Sharers joining the ride"
        Buttom Edit "Only avaliable for owner"
    }
    Open_Ride_List3{
        Display Waiting_Status "Window"
        DisplayInfo Ride_Details "From request info"
        DisplayInfo sharers_name "Sharers joining the ride"
        Buttom Edit "Only avaliable for owner"
    }
    

    Driver ||--|{ Request_Info_List_of_Driver : can_see
    Request_Info_List_of_Driver ||--|{ Conditions_of_Driver : match

    Request_Info_List_of_Driver ||--|{ Driver : can_see
    Request_Info_List_of_Driver ||--|{ Ride_Status_for_Driver : confirm
    Open_Ride_List ||--|{ Ride_Status_for_Passenger : being_confirmed
    Waiting_for_Driever ||--|{ Ride_Status_for_Passenger : being_confirmed

    Conditions_of_Driver{
        Match Vehicle_Capacity
        Match Vehicle_type
        Match Special_Vehicle_Info
    }
    Request_Info_List_of_Driver{
        Display All_Open_Ride_List "must match Driver's request info"
        Match Destination_Address
        Match Arrial_Date_Time
        Match Number_of_Passenger
        Match Special_Request
        Buttom Choose
        Buttom Back
    }
    Ride_Status_for_Driver{
        Display Info "All passengers"
        Display Number_of_Passenger
        Buttom Complete
    }
    Ride_Status_for_Passenger{
        Send email "To all passengers"
        Display Driver_Name
        Display Vehicle_Type
        Display license_Plate_Number
        Display Vehicle_Capacity
        Display Special_Vehicle_Info "Optional"
        Display Info "Vehicle"
    }
```
## Web Deployment
```mermaid
stateDiagram-v2

    Guest(Home.html) --> Login.html
    Guest(Home.html) --> CreateAccount.html
    CreateAccount.html --> Login.html
    
    Login.html --> UserHome.html
    Login.html --> DriverHome.html
    UserHome.html --> UserProfile.html
    UserHome.html --> DriverRegister.html
    UserHome.html --> UserOrder.html
    State UserOrder.html {
        History
    }

    UserHome.html --> Owner.html
    State Owner.html{
        Owner_InfoForm.html
    }

    Owner.html --> Owner_List.html
    Owner_List.html --> Owner.html : Edit Ride
    State Owner_List.html{
        Edit_Ride
        --
        OrderHistory
        --
        ShareInfo
    }
    
    UserHome.html --> Sharer.html
    State Sharer.html{
        Sharer_InfoForm.html
    }

    Sharer.html --> SharerSearch_List.html
    State SharerSearch_List.html{
        all_the_possible_rides_you_can_pick
    }

    UserHome.html --> Logout.html
    DriverHome.html --> Logout.html
    
    DriverHome.html --> DriverProfile.html  
    DriverHome.html --> Driver.html

    Driver.html --> DriverSearch_List.html
    State DriverSearch_List.html{
        all_the_possible_orders_you_can_pick
    }

    DriverHome.html --> DriverOrder.html
    State DriverOrder.html{
        CompleteButtom
    }
```

# Function
## Account

- Create a user account
- Login with a valid user account
- Handle login failure with an an invalid user account
- Logout from a user session

## Owner

- User should be able to register as a driver by entering their personal & vehicle info
- User should be able to submit a ride request by specifying the required and any combination of the optional info
- User should be able to make a selection to view any non-complete ride they belong to
- User should be able to make a selection to edit any open ride they belong to
- A ride owner should be able to edit the requested attributes of a ride until that ride is confirmed
- User should be able to view all ride details for any open ride they belong to
- User should be able to view all ride details + driver and vehicle details for any confirmed ride they belong to

## Sharer

- User should be able to search for sharable, open ride requests (by destination, arrival window, and # of passengers)
- User should be able to join a ride returned in a search

## Driver

- (Not Finish) User should be able to view and edit their driver status as well as personal & vehicle info
- (Not Finish) An email should be sent to the owner and any sharers of a ride once it is confirmed by a driver
- A registered driver should be able to search for open ride requests (filtered by the driver's vehicle capacity and type / special info, if applicable)
- A registered driver should be able to mark a selected ride (returned from a search) as confirmed (thus claiming and starting the ride)
- A driver should be able to see a list of their confirmed rides
- A driver should be able to select a confirmed ride and view all of the ride details
- A driver should be able to edit a confirmed ride for the purpose of marking it complete after the ride is over
