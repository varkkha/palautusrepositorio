*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Variables ***
${SERVER}        localhost:5001
${DELAY}         0.5 seconds
${WELCOME}      http://${SERVER}/welcome
${REGISTER_URL}  http://${SERVER}/register

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Go To Welcome Page

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Submit Credentials
    Registering Should Fail With Message  Invalid username or password

Register With Valid Username And Too Short Password
    Set Username  validuser
    Set Password  short1
    Submit Credentials
    Registering Should Fail With Message  Invalid username or password

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  validuser
    Set Password  onlyletters
    Submit Credentials
    Registering Should Fail With Message  Invalid username or password

Register With Nonmatching Password And Password Confirmation
    Set Username  validuser
    Set Password  validPass123
    Set Password Confirmation  differentPass123
    Submit Credentials
    Registering Should Fail With Message  Invalid username or password

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Registering Should Fail With Message  Invalid username or password

*** Keywords ***

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Go To Welcome Page
    Go To  ${WELCOME}

Go To Register Page
    Go To  ${REGISTER_URL}

Registering Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register Page Should Be Open
    Location Should Be  ${REGISTER_URL}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page