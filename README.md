# Census_API_Testing
This test script needs 2 libraries to run properly: Pytest and Requests library. 
The test script prints a list of users from the get_api_status function (the amount of users determined by the "results" payload in the "https://randomuser.me/api?results=100" link. This function returns the status-code from the server when the post request is made. 
*The amount of items printed in the output will be based on the value in the "top" parameter. The value count though, is based on the array of users stored in the "users_for_payload" variable.
The test is passed if the response from server is 200 OK.
![image](https://user-images.githubusercontent.com/51688932/180365730-499089dc-721e-4165-b6e6-b32a4dddea76.png)
