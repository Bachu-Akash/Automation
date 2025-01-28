*** Settings ***
Library     SeleniumLibrary
Variables   ../PageElements/locators.py

*** Variables ***
${siteurl}  https://www.redbus.in/
${browser}  chrome
${source_place}   Bangalore
${destination_place}   Hyderabad
${boarding_point_name}    Bellandur
${destination_point_name}    Shadnagar
${name}    Akash
${age}    21
${state}    Andhra Pradesh
${email}    akashbachu06@gmail.com
${mobile}    8297871050


*** Keywords ***
Open RedBus Website
    [Arguments]    ${SiteUrl}    ${Browser}
    Open Browser    ${SiteUrl}    ${Browser}
    Maximize Browser Window
    Set Selenium Implicit Wait    5

Send Keys To Element
    [Arguments]    ${element}    ${value}
    Input Text    ${element}     ${value}

Clicking Element
    [Arguments]     ${element}
    Click Element    ${element}

Pressing Keys
    [Arguments]     ${element}
    Press Keys    ${element}    ENTER

Print Buses Count
    ${bus_count}=   Get Text    ${buses_count}
    Log To Console    ${bus_count}

Print Free Seats
    ${free_seat}=   Get Text    ${free_seats}
    Log To Console    ${free_seat}

Scroll Element
    [Arguments]     ${element}
    Scroll Element Into View    ${element}

Select Boarding Point
    ${boarding_locator}=    Set Variable    xpath=//li[@class='db oh']/div/div[3]/div/span[@title='${boarding_point_name}']
    Click Element    ${boarding_locator}

Select Destination Point
    ${destination_locator}=    Set Variable    xpath=//li[@class='db oh']/div[3]/div/span[@title='${destination_point_name}']
    Click Element    ${destination_locator}


