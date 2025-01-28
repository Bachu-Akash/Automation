source="xpath://input[@id='src']"  # Source location input field
destination="xpath://input[@id='dest']"  # Destination location input field
search_button="xpath://button[@id='search_button']"  # Search button
buses_count="xpath://span[@class='f-bold busFound']"  # Total number of buses found
date_picker="xpath=//div[@id='onwardCal']"  # Date picker for selecting journey date
specific_date="xpath=//text[contains(text(),'6')]"  # Specific date selection (6th)
sort_fare="xpath=//span[normalize-space()='Fare']"  # Sort by fare option
free_seats="xpath=//div[@class='seat-left m-top-30'][1]"  # Free seats count in a bus
select_bus="xpath=//div[@class='button view-seats fr'][normalize-space()='View Seats'][1]"  # View seats button for a bus
low_price_seat="xpath=//li[@class='fl mulfare'][1]"  # Seat with the lowest fare
boarding_point = "xpath=//li[@class='db oh']/div/div[3]/div/span[@title='{}']"  # Select specific boarding point
destination_point_button = "xpath=//span[normalize-space()='DROPPING POINT']"  # Button to choose dropping point
destination_point = "xpath=//li[@class='db oh']/div[3]/div/span[@title='{}']"  # Select specific dropping point
proceed_to_book_button="xpath=//button[normalize-space()='Proceed to book']"  # Proceed to booking button
name_box="xpath=//input[@class='input_box ']"  # Name input field
age_box="xpath=//input[@id='seatno-01']"  # Age input field
state_of_residence_box="xpath=//input[@id='201']"  # State of residence input field
email_box="xpath=//input[@id='seatno-05']"  # Email input field
mobile_number="xpath=//input[@id='seatno-06']"  # Mobile number input field
final_button="xpath=//input[@value='Proceed to pay']"  # Final payment button
no_insurance="xpath=//input[@id='insuranceNotOpted_rap']"  # Option to skip insurance