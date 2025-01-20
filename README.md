Please make sure that the below requirements are satisfied for the dependencies:

fastapi
uvicorn
influxdb-client
paho-mqtt
python-dotenv
passlib
paho-mqtt==1.6.1
redis==4.5.1
psycopg2-binary==2.9.6


In case these are not available on your system, please install them directly from your terminal/IDE.

Next steps would then be for running the code. For this:

1) Unzip zip file "Smart_home_System.zip" to a folder named "Smart_home_System".

2) Load this folder onto your IDE.

3) Run the following command to get the docker containers up and running: "docker compose up --build".

4) Check that you see the Publisher and Subscriber are generating and caching the sensor data, which will be used later in InfluxDB.

5) To check structured data via PostgreSQL, copy and paste the URL "http://localhost:8000/docs#/" to your web browser to load the Swagger UI from fastAPI.

6) Use the username and password as "Admin" as follows:
	Username: admin
	Password: admin123
7) In case you want to login as a normal "User", please use:
	Username: user
	Password: user123
