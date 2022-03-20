### Test Case Id: 
1. signin_pmatch_200
2. signin_perr_401
3. signin_uerr_401

### Description:
1. Tests that given a username that does exist as well as a password the api returns data specifying that the user was valid
2. Tests that given a username that does exist as well as a password the api returns data specifying the user was valid but the password was invalid
3. Tests that given a username and password the username does not exist and is invalid

### Test Steps
(1) signin_pmatch_200: 
- Call the signup api at POST /api/signup with the a valid username and password that does not exist already.
- Call the signin api at POST /api/signin with the same username and password that you previously used to signup.

(2) signin_perr_401:
- Call the signup api at POST /api/signup with the a valid username and password that does not exist already.
- Call the signin api at POST /api/signin with the same username but a different password than you previously used to signup.

(3) signin_uerr_401:
- Call the signin api at POST /api/signin with a username that does not exist already

### Pre-requisities
(1) signin_pmatch_200:
1. Signup API created and working correctly
2. Signin API created and working correctly

(2) signin_perr_401:
1. Signup API created and working correctly
2. Signin API created and working correctly

(3) signin_uerr_401
1. Signup API created and working correctly
2. Signin API created and working correctly

### Author
John Paglia

### Test Method
(1): test_signin_200_pass_match
(2): test_signin_401_pass_error
(3): test_signin_401

### Pass/Fail Criteria

(1) test_signin_200_pass_match:
Passes if data returned has user_error as "false" and pass_error as "false" as well as a 200 status code. Otherwise test fails

(2) test_signin_401_pass_error:
Passes if data returned has user_error as "false" and pass_error as "true" as well as a 401 status code. Otherwise test fails

(3) test_signin_401:
Passes if data returned has user_error as "true" and pass_error as "true" as well as a 401 status code. Otherwise test fails