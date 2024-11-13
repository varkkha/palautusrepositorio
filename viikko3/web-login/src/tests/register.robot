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
${OHTU_URL}  http://${SERVER}/ohtu
${LOGIN_URL}     http://${SERVER}/login

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
    Registering Should Fail With Message  Too short password

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  validuser
    Set Password  onlyletters
    Submit Credentials
    Registering Should Fail With Message  Password should contain letters and numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  validuser
    Set Password  validPass123
    Set Password Confirmation  differentPass123
    Submit Credentials
    Registering Should Fail With Message  Passwords differ

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Registering Should Fail With Message  Username already in use

Login After Successful Registration
    Set Username  testuser
    Set Password  test12345
    Set Password Confirmation  test12345
    Submit Credentials
    Registering Should Succeed
    Main Page
    Logout
    Logout Should Succeed
    Go To Login Page
    Set Username  testuser
    Set Password  test12345
    Submit Login
    Login Should Succeed

Login After Failed Registration
    Set Username  te
    Set Password  testi123
    Submit Credentials
    Registering Should Fail With Message  Invalid username or password
    Go To Login Page
    Set Username  te
    Set Password  short
    Submit Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Submit Credentials
    Click Button  Register

Logout
    Click Button  Logout

Submit Login
    Click Button  Login

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

Go To Ohtu Page
    Go To  ${OHTU_URL}

Go To Login Page
    Go To  ${LOGIN_URL}

Registering Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register Page Should Be Open
    Location Should Be  ${REGISTER_URL}

Login Should Succeed
    Location Should Be    ${OHTU_URL}

Registering Should Succeed
    Location Should Be    ${WELCOME}

Logout Should Succeed
    Location Should Be  ${LOGIN_URL}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Main Page
    Click Link  Continue to main page

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page