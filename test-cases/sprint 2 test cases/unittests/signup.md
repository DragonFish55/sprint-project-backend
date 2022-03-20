### Test Case Id: 
1. signup_200
2. signup_401

### Description:
1. Tests that given a username that doesnt exist that as well as a password, will create the user in the database 
2. Tests that given a username that doesnt exist that as well as a password, once the signup api creates the user if the api is called again with the same username the api will reject the duplicate username.

### Test Steps
(1) signup_200: 
- Call the signup api at POST /api/signup with the a valid username and password that does exist already.

(2) signup_401:
- Call the signup api at POST /api/signup with the a valid username and password that does not exist already.
- Call the signup api again and supply the same username and password thus getting an error because the user exists already

### Pre-requisities
(1) signup_200:
1. Default API created and working correctly

(2) signup_401:
1. Default API created and working correctly


### Author
John Paglia

### Test Method
(1): test_signup_200
(2): test_signup_401

### Pass/Fail Criteria

(1): test_signup_200:
Passes if data returned is not "true" and response code is 200. Otherwise test fails.

(2): test_signup_401:
Passes if data returned is "false" and response code is 401. Otherwise test fails.