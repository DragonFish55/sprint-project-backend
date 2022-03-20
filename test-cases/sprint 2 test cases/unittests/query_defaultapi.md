### Test Case Id: 
1. qry_def_200
2. qry_def_401

### Description:
1. Tests that given a valid query type for newsapi that the api is queried based on the given types default query 
2. Tests that given an incorrect default query type the api responds with a 401 error for invalid default query

### Test Steps
(1) qry_def_200: 
- Call the default api at GET /api/<entry>/defaultApi with the "top_headline" entry

(2) qry_def_401:
- Call the default api at GET /api/<entry>/defaultApi with the any entry except "top_headline"

### Pre-requisities
(1) qry_def_200:
1. Default API created and working correctly

(2) qry_def_401:
1. Default API created and working correctly


### Author
John Paglia

### Test Method
(1): test_default_200
(2): test_default_401

### Pass/Fail Criteria

(1): test_default_200:
Passes if data returned is not "None" and response code is 200. Otherwise test fails.

(2): test_default_401:
Passes if data returned is "None" and response code is 401. Otherwise test fails.