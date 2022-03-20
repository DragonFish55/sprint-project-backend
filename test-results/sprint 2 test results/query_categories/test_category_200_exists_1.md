# Test Results

# Test Method:
test_category_200_exists

# Test Case ID:
qry_cat_exists

# Group Member:
John Paglia

# Pass/Fail:
Fail

# Comments:
Test initialliy failed because since it is a test driven development
test case and the category api definitiion does not exist in the project.
The test fails when trying to retrieve json data from a response that
had a None type (did not succeed) using json.loads