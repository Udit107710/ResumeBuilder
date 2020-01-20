# ResumeBuilder

To use the application you will have to set various env variables:
1) AWS_ACCESS_KEY_ID # For S3 Bucket
2) AWS_SECRET_ACCESS_KEY # For S3 Bucket
3) AWS_STORAGE_BUCKET_NAME # For S3 Bucket
4) AWS_S3_REGION_NAME # For S3 Bucket
5) EMAIL_HOST_USER # For Email
6) EMAIL_HOST_PASSWORD # For Email


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
