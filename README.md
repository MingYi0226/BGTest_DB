# Getting Started with Create React App
This repository represents database schema used for ByteGenie test project.
## Create additional columns for event_industry and email
	1. I used LLM model(llama-3-sqlcoder-8b) to extract event industry from event_description and created event.event_industry.
	2. Created people.email column from people.email_template column.

	You can find above functions in utility.py
## Convert CSV files to Database(SQLLite)
1. Create a Database
2. Import CSV files into tables
    - .mode csv
    - .import xxxx\company_info.csv company
    - .import xxxx\event_info.csv event
    - .import xxxx\people_info.csv people

## Database Schema
### people 
    CREATE TABLE IF NOT EXISTS "people" (
	"first_name"	TEXT,
	"middle_name"	TEXT,
	"last_name"	TEXT,
	"job_title"	TEXT,
	"person_city"	TEXT,
	"person_state"	TEXT,
	"person_country"	TEXT,
	"email_pattern"	TEXT,
	"homepage_base_url"	TEXT,
	"duration_in_current_job"	TEXT,
	"duration_in_current_company"	TEXT,
	"email" TEXT
    )

### event
    CREATE TABLE IF NOT EXISTS "event" (
	"event_logo_url"	TEXT,
	"event_name"	TEXT,
	"event_start_date"	TEXT,
	"event_end_date"	TEXT,
	"event_venue"	TEXT,
	"event_country"	TEXT,
	"event_description"	TEXT,
	"event_url"	TEXT,
	"event_industry" TEXT

### company
    CREATE TABLE IF NOT EXISTS "company" (
	"company_logo_url"	TEXT,
	"company_logo_text"	TEXT,
	"company_name"	TEXT,
	"relation_to_event"	TEXT,
	"event_url"	TEXT,
	"company_revenue"	TEXT,
	"n_employees"	TEXT,
	"company_phone"	TEXT,
	"company_founding_year"	TEXT,
	"company_address"	TEXT,
	"company_industry"	TEXT,
	"company_overview"	TEXT,
	"homepage_url"	TEXT,
	"linkedin_company_url"	TEXT,
	"homepage_base_url"	TEXT,
	"company_logo_url_on_event_page"	TEXT,
	"company_logo_match_flag"	TEXT,
	"id"	INTEGER,
	PRIMARY KEY("id")
)

## Challenges you faced in working with this data
While creating additional columns, I need to consider exceptions that column data is not unavailable.

## Things to improve database desgin:
    - 
    - 