# ResumeBuilder

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/b1c3d40406d996a29937)

POST /api/send-resume <br>
request data schema: <br>
```json
{
    "name" : "detail of person",
    "email" : "detail of person",
    "template" : "choice of template"
}
```
response data schema:
```json
{
  "email": "successful/unsuccessful",
  "resume": "link to resume is succeeded"
}
```
GET /api/resumes <br>
request data schema: <br>
\* no data required

response data schema: <br>

```json
{
  "files": ["list of resume templates link"]
}
```