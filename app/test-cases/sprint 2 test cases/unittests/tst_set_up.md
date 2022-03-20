### Test Case Id: 
1. tst_set_up_add
2. tst_set_up_rem
3. tst_set_up_err

### Description:
1. Tests that given a valid category set to a value of true in the params for the request the category is successfully added to the user's account
2. Tests that after adding a category to the user's account you can submit the same category with a value of false and the category is removed from the user's account.
3. Tests that given an invalid username in the request a data value of "false" is returned as well as a 401 status code

### Test Steps
(1) tst_set_up_add: 
- Call the signup api at POST /api/signup with the a valid username and password that does not exist already.
- Call the update settings api at /api/new/<user>/categories" and add a url param using "?<category>=true" and pass the user in the request url.
-As long as the category is valid it should be added to the new account

(2) tst_set_up_rem:
- Call the signup api at POST /api/signup with the a valid username and password that does not exist already.
- Call the update settings api at /api/new/<user>/categories" and add a url param using "?<category>=true" and pass the user in the request url.
-As long as the category is valid it should be added to the new account
-Now once again call /api/new/<user>/categories" and add a url param using "?<category>=false" for the same category.  
-Now check to see if the category was removed. If it was the test passes.

(3) tst_set_up_err:
- Call the update settings api at /api/new/<user>/categories" and add a url param using "?<category>=true" and pass a user that does not exist in the request url.
-You should get a 401 status code signifying the test passed.

### Pre-requisities
(1) tst_set_up_add:
1. Signup API created and working correctly
2. Settings Update API Created and working

(2) tst_set_up_rem:
1. Signup API created and working correctly
2. Settings Update API Created and working

(3) tst_set_up_err:
1. Settings Update API Created and working

### Author
John Paglia

### Test Method
(1): test_settings_update_200_Add
(2): test_settings_update_200_Rem
(3): test_settings_update_401

### Pass/Fail Criteria

(1) test_settings_update_200_Add:
Passes if data returned has user_error as "false" and pass_error as "false" as well as a 200 status code. Otherwise test fails

(2) test_settings_update_200_Rem:
Passes if data returned has user_error as "false" and pass_error as "true" as well as a 200 status code. Otherwise test fails

(3) test_settings_update_401:
Passes if data returned has a "false" value as well as a 401 response code. Otherwise the test fails.