*** Settings ***
Library     SeleniumLibrary
Resource    ../Resources/Redbus_Keywords.robot
Variables   ../PageElements/locators.py

*** Test Cases ***
RedbusTest
    Open RedBus Website    ${siteurl}    ${browser}  # Open RedBus website in specified browser
    Send Keys To Element    ${source}      ${source_place}  # Enter source location
    Send Keys To Element    ${destination}    ${destination_place}  # Enter destination location
    Sleep    5
    Clicking Element    ${search_button}  # Click search button
    Print Buses Count  # Print the total number of buses available
    Clicking Element    ${sort_fare}  # Sort buses by fare
    Clicking Element    ${select_bus}  # Select a specific bus
    Print Free Seats  # Print the number of free seats in the bus
    Clicking Element    ${low_price_seat}  # Select the seat with the lowest fare
    Sleep    5
    Select Boarding Point  # Choose the boarding point
    Clicking Element    ${destination_point_button}  # Open dropping point options
    Select Destination Point  # Choose the dropping point
    Clicking Element    ${proceed_to_book_button}  # Proceed to book the selected bus
    Send Keys To Element    ${name_box}    ${name}  # Enter passenger's name
    Send Keys To Element    ${age_box}    ${age}  # Enter passenger's age
    Sleep    3  
    Send Keys To Element    ${state_of_residence_box}    ${state}  # Enter state of residence
    Pressing Keys    ${state_of_residence_box}  # Confirm state entry
    Send Keys To Element    ${email_box}    ${email}  # Enter passenger's email
    Send Keys To Element    ${mobile_number}    ${mobile}  # Enter passenger's mobile number
    Clicking Element    ${no_insurance}  # Opt-out of insurance
    Clicking Element    ${final_button}  # Proceed to payment page
    Sleep    5
