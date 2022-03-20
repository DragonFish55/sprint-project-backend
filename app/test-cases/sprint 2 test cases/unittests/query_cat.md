### Test Case Id: 
1. qry_cat_exists
2. qry_cat_none
3. qry_cat_err

### Description:
1. Tests that given that the user is created and they have categories 
in their account that were previously added the newsapi endpoint
is queried for each of those categories. 
2. Tests that given that the user is created and they have no categories
in their account that were previously added the function returns "None" and
a response code of 200
3. Tests that given a username the user is not valid and a 401 error is returned

### Test Steps
(1) qry_cat_exists: 
- Create an account with a valid username and password
- Add at least one category to the user by calling the "/api/new/<user>/categories" endpoint and providing a valid query parameter 
- Call the GET /api/<user>/getApiData endpoint by providing the username that was created and if the json data returned is valid and a response code of 200 is returned the test passes

(2) qry_cat_none:
- Create an account with a valid username and password
- Call the GET /api/<user>/getApiData endpoint by providing the username that was created and if the json data returned is "None" and a response code of 200 is returned the test passes

(3) qry_cat_err:
- Without creating an account call the GET /api/<user>/getApiData endpoint by providing a user that is not created and if the json data returned is "None" and a response code of 401 is returned the test passes

### Pre-requisities
(1) qry_cat_exists:
1. Signup API working correctly
2. Settings API working correctly

(2) qry_cat_none:
1. Signup API working correctly

(3) qry_cat_err:
1. No pre-requisites besides the category api functioning correctly

### Author
John Paglia

### Test Method
(1): test_category_200_exists
(2): test_category_200_none
(3): test_category_401

### Pass/Fail Criteria

(1) qry_cat_exists:
 Passes if json newsapi data for each category in the users account is returned successfully from the function call as well as a 200 response code. Otherwise the test fails

(2) qry_cat_noe: 
 Passes if a response code of 200 is received and data is "None" otherwise test fails 

(3) qry_cat_err: 
 Passes if a response code of 401 is received and data is "None" otherwise test fails