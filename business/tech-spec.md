# Tech Spec: Consent-Guardrails v1
## Stack

* **Language:** TypeScript
* **Framework:** Express.js with NestJS
* **Runtime:** Node.js (14.x)
* **Database:** PostgreSQL (13.x) with TypeORM
* **Storage:** AWS S3 for storing consent templates and other static assets

## Hosting

* **Free-tier-first:** Yes, with AWS Free Tier for the first 12 months
* **Platforms:**
	+ AWS Elastic Beanstalk for deployment and scaling
	+ AWS RDS for PostgreSQL database management
	+ AWS S3 for storage

## Data Model

* **Tables/Collections:**
	+ `consents`: stores consent records with metadata
	+ `templates`: stores consent templates with metadata
	+ `users`: stores user information with roles and permissions
* **Key Fields:**
	+ `consents`:
		- `id` (primary key): UUID
		- `template_id`: foreign key referencing `templates.id`
		- `user_id`: foreign key referencing `users.id`
		- `created_at`: timestamp
		- `updated_at`: timestamp
	+ `templates`:
		- `id` (primary key): UUID
		- `name`: string
		- `description`: string
		- `created_at`: timestamp
		- `updated_at`: timestamp
	+ `users`:
		- `id` (primary key): UUID
		- `email`: string
		- `role`: string (e.g., "admin", "user")
		- `created_at`: timestamp
		- `updated_at`: timestamp

## API Surface

* **Endpoints:**
	1. **GET /consents**: retrieve all consent records
		- Method: GET
		- Path: `/consents`
		- Purpose: retrieve a list of all consent records
	2. **GET /consents/{id}**: retrieve a single consent record
		- Method: GET
		- Path: `/consents/{id}`
		- Purpose: retrieve a single consent record by ID
	3. **POST /consents**: create a new consent record
		- Method: POST
		- Path: `/consents`
		- Purpose: create a new consent record
	4. **PUT /consents/{id}**: update an existing consent record
		- Method: PUT
		- Path: `/consents/{id}`
		- Purpose: update an existing consent record
	5. **DELETE /consents/{id}**: delete a consent record
		- Method: DELETE
		- Path: `/consents/{id}`
		- Purpose: delete a consent record
	6. **GET /templates**: retrieve all consent templates
		- Method: GET
		- Path: `/templates`
		- Purpose: retrieve a list of all consent templates
	7. **GET /templates/{id}**: retrieve a single consent template
		- Method: GET
		- Path: `/templates/{id}`
		- Purpose: retrieve a single consent template by ID
	8. **POST /templates**: create a new consent template
		- Method: POST
		- Path: `/templates`
		- Purpose: create a new consent template
	9. **PUT /templates/{id}**: update an existing consent template
		- Method: PUT
		- Path: `/templates/{id}`
		- Purpose: update an existing consent template
	10. **DELETE /templates/{id}**: delete a consent template
		- Method: DELETE
		- Path: `/templates/{id}`
		- Purpose: delete a consent template

## Security Model

* **Authentication:** JSON Web Tokens (JWT) with refresh tokens
* **Authorization:** Role-based access control (RBAC) with permissions
* **Secrets:** environment variables for sensitive data (e.g., database credentials)
* **IAM:** AWS IAM for managing user access and permissions

## Observability

* **Logs:** AWS CloudWatch Logs for storing and monitoring logs
* **Metrics:** AWS CloudWatch Metrics for monitoring application performance
* **Traces:** AWS X-Ray for tracing and debugging

## Build/CI

* **Build:** Node.js 14.x with TypeScript 4.x
* **CI:** GitHub Actions with Node.js 14.x and TypeScript 4.x
* **Testing:** Jest with TypeScript 4.x for unit testing and integration testing
* **Deployment:** AWS Elastic Beanstalk for deployment and scaling