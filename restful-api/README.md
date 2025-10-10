1 Differences between HTTP and HTTPS

|-----------------|--------------------------------------------------------|--------------------------------------------------------------------------|
| Feature         | **HTTP (HyperText Transfer Protocol)**                 | **HTTPS (HyperText Transfer Protocol Secure)**                           |
|-----------------|--------------------------------------------------------|--------------------------------------------------------------------------|
| **Security**    | Data is sent in plain text — vulnerable to             | Data is encrypted using SSL/TLS,                                         |
|                 | interception (not encrypted).                          | protecting against eavesdropping and tampering.                          |
|-----------------|--------------------------------------------------------|--------------------------------------------------------------------------|
| **Port used**   | Port **80** by default.                                | Port **443** by default.                                                 |
|-----------------|--------------------------------------------------------|--------------------------------------------------------------------------|
| **Encryption**  | No encryption.                                         | Encrypted with SSL/TLS.                                                  |
|-----------------|--------------------------------------------------------|--------------------------------------------------------------------------|
| **Certificate** | No certificate required.                               | Requires a **digital SSL certificate** issued by a trusted authority.    |
|-----------------|--------------------------------------------------------|--------------------------------------------------------------------------|
| **Use cases**   | Simple or internal sites where security isn’t critical.| Websites handling personal data, logins, or payments (e.g., banking,     |
|                 |                                                        | e_commerce).                                                             |
|-----------------|--------------------------------------------------------|--------------------------------------------------------------------------|


2 Understanding HTTP Structure:


HTTP is a communication protocol between a client (navigateur, application..) and a serveur (the website). Every time we open a web page, the Navigator send a HTTP request to the servor and he respond with a HTTP answer.


A Structure of a HTTP request

There is three big parts

1 Request line
It's the first ligne of the request, it gives:
⦁	The method
⦁	The PATH
⦁	The version of the protocol HTTP

exemple: GET /index.html HTTP/1.1

2 Headers
They are supplementary lines that give more informations on the request or the client (Navigator, système, type allow…)

exemple:
 	Host: www.example.com
 	User-Agent: Mozilla/5.0
 	Accept: text/html

3 Body
The body if often empty in a GET request, but it's present in POST, PUT or PATCH requests.
It contains the datas to send to the serveur (for exemple a file or a JSON)

exemple: (send connexion datas to the servor in JSON)
POST /login HTTP/1.1
Host: www.example.com
Content-Type: application/json
Content-Length: 48

{
  "username": "thea",
  "password": "mypassword"
}


B HTTP anwsered

An aswered HTTP have three big parts.

1 Status Line
It gives:
⦁	The HTTP protocol version
⦁	The statut code
⦁	A message of the code

exemple: HTTP/1.1 200 OK

2 Headers
It's the informations send by the serveur

content-type -> type of the content (HTML)
content-length -> The taille of what he send
set-cookies -> send a cookie to the Navigator

exemple:
Content-Type: text/html
Content-Length: 1256
Set-Cookie: sessionId=abc123

3 Body
it's the principal part: the serveur puts the HTML page, the JSON, images, etc

exemple:
<html>
  <body>
    <h1>Welcome, Théa!</h1>
  </body>
</html>


exempler of a conplete exchange :

the customers send:
GET /home HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html

Ther servor answered:
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 57

<html>
  <body>Bienvenue sur ma page d'accueil !</body>
</html>


En résumé :
Le client fait une demande → “Peux-tu me donner cette page ?”
Le serveur répond → “Oui, voici la page demandée (ou un message d’erreur si elle n’existe pas).”


3. Common HTTP Methods

| ----------- | ----------------------------------------------------------------- | --------------------------------------------------- |
| **Method**  | **Description**                                                   | **Typical Use Case**                                |
| ----------- | ----------------------------------------------------------------- | --------------------------------------------------- |
| **GET**     | Retrieves data from a server.                                     | Loading a web page or fetching data from an API.    |
| ----------- | ----------------------------------------------------------------- | --------------------------------------------------- |
| **POST**    | Sends data to the server (often creates a resource).              | Submitting a form or uploading a file.              |
| ----------- | ----------------------------------------------------------------- | --------------------------------------------------- |
| **PUT**     | Replaces an existing resource or creates one if it doesn’t exist. | Updating user profile data.                         |
| ----------- | ----------------------------------------------------------------- | --------------------------------------------------- |
| **PATCH**   | Partially updates an existing resource.                           | Modifying one field in a database record.           |
| ----------- | ----------------------------------------------------------------- | --------------------------------------------------- |
| **DELETE**  | Removes a resource from the server.                               | Deleting a comment or account.                      |
| ----------- | ----------------------------------------------------------------- | --------------------------------------------------- |
| **HEAD**    | Similar to GET but retrieves headers only (no body).              | Checking if a resource exists or has changed.       |
| ----------- | ----------------------------------------------------------------- | --------------------------------------------------- |
| **OPTIONS** | Describes the communication options for a resource.               | Checking which methods are supported by the server. |
| ----------- | ----------------------------------------------------------------- | --------------------------------------------------- |


4. Common HTTP Status Codes

|------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------|
| **Code**                           | **Description**                                                       | **Typical Scenario**                              |
|------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------|
| **200 OK**                         | Request succeeded.                                                    | Page loads correctly.                             |
|------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------|
| **201 Created**                    | A new resource was created.                                           | After submitting a POST to create an item.        |
|------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------|
| **204 No Content**                 | Request succeeded, no content returned.                               | Deleting a resource successfully.                 |
|------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------|
| **301 Moved Permanently**          | Resource has been permanently redirected.                             | Redirecting to a new URL.                         |
|------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------|
| **302 Found (Temporary Redirect)** | Resource temporarily at another location.                             | Temporary URL redirect.                           |
|------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------|
| **400 Bad Request**                | Server couldn’t understand the request.                               | Missing or invalid parameters in an API call.     |
|------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------|
| **401 Unauthorized**               | Authentication required or failed.                                    | Accessing protected content without logging in.   |
|------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------|
| **403 Forbidden**                  | Server understood but refuses to authorize.                           | Trying to access an admin page without permission.|
|------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------|
| **404 Not Found**                  | Resource not found.                                                   | Accessing a missing page.                         |
|------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------|
| **500 Internal Server Error**      | General server-side error.                                            | Bug or crash in backend code.                     |
|------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------|
| **503 Service Unavailable**        | Server is temporarily unavailable (overloaded or under maintenance).  | Website down for maintenance.                     |
|------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------|
