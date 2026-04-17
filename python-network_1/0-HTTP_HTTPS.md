# Basics of HTTP/HTTPS

## 1. Difference between HTTP and HTTPS
HTTP is not secure and does not encrypt data. HTTPS uses SSL/TLS encryption to protect data.

## 2. HTTP Request and Response Structure

### Request
GET /index.html HTTP/1.1
Host: example.com

### Response
HTTP/1.1 200 OK
Content-Type: text/html

## 3. HTTP Methods
- GET: Retrieve data (e.g., open webpage)
- POST: Send data (e.g., form submission)
- PUT: Update data
- DELETE: Remove data

## 4. HTTP Status Codes
- 200: OK (success)
- 301: Moved Permanently
- 400: Bad Request
- 404: Not Found
- 500: Internal Server Error
