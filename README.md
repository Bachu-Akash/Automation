# Automation Frameworks: Let's Kode It and Redbus

This repository contains two automation projects: Let's Kode It and Redbus, implemented using different frameworks and tools while following the Page Object Model (POM) design pattern.

# Let's Kode It Automation Framework

## Overview
The Let's Kode It project automates the practice website using Selenium WebDriver with Pytest, designed for scalability, modularity, and reusability.

## Project Structure
Let's Kode It/
├── TestCases/  # Contains Pytest-based test cases
└── Library/    # Contains reusable methods and page-specific utilities

## Features
- Framework: Selenium with Pytest
- Design Pattern: Page Object Model (POM)
- Highlights:
  - Encapsulation of page actions and locators in the Library folder.
  - Organized and modular test cases for easy execution and debugging.

## How to Run
1. Clone the Repository:
   git clone https://github.com/yourusername/repositoryname.git

2. Navigate to the Project Directory:
   cd "Let's Kode It"

3. Install Dependencies:
   - Ensure Python (>= 3.7) is installed.
   - Install required libraries:
     pip install selenium pytest

4. Run Test Cases:
   Execute all test cases or specific ones using:
   pytest TestCases/

5. Optional: Generate HTML Reports:
   Use pytest-html for HTML test execution reports:
   pip install pytest-html
   pytest TestCases/ --html=report.html

## Future Enhancements
- Add more complex scenarios to enhance coverage.
- Integrate with CI/CD pipelines for automated testing.

# Redbus Automation Framework

## Overview
The Redbus project automates the Redbus website using Robot Framework and Selenium WebDriver. The project is structured to ensure modularity, scalability, and easy maintenance.

## Project Structure
Redbus/
├── PageElements/  # Contains locators for web elements
├── Resources/     # Contains reusable Robot Framework keywords
└── TestCases/     # Contains test cases for end-to-end automation

## Features
- Framework: Robot Framework with Selenium
- Design Pattern: Page Object Model (POM)
- Highlights:
  - Reusable keywords stored in the Resources folder.
  - Page-specific locators managed in the PageElements folder.
  - Well-organized test cases in the TestCases folder for modular execution.

## How to Run
1. Clone the Repository:
   git clone https://github.com/yourusername/repositoryname.git

2. Navigate to the Project Directory:
   cd Redbus

3. Install Dependencies:
   - Ensure Python (>= 3.7) is installed.
   - Install required libraries:
     pip install robotframework robotframework-seleniumlibrary

4. Execute Test Cases:
   Run specific test cases or all tests from the TestCases folder:
   robot TestCases/<test_case_name>.robot

## Future Enhancements
- Add more scenarios to increase test coverage.
- Integrate with CI/CD pipelines for continuous testing.

# Summary

Both Let's Kode It and Redbus projects follow the Page Object Model (POM) design pattern, ensuring scalability, modularity, and ease of maintenance. While the Let's Kode It project utilizes Selenium with Pytest, the Redbus project is built using Robot Framework with Selenium. Both frameworks cater to specific testing needs, providing a solid foundation for automation.

Feel free to explore and contribute to the repository!
