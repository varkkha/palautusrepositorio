*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}        localhost:5001
${DELAY}         0.5 seconds
${HOME_URL}      http://${SERVER}
${REGISTER_URL}  http://${SERVER}/register

*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Starting Page

*** Test Cases ***
Click Login Link
    Click Link  Login
    Login Page Should Be Open

Click Register Link
    Click Link  Register new user
    Register Page Should Be Open

*** Keywords ***

Go To Starting Page
  Go To  /

Reset Application And Go To Starting Page
  Reset Application
  Go To  ${HOME_URL}

Register Page Should Be Open
  Go To  ${REGISTER_URL}