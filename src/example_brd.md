# Business Requirements Doc

## Goal
The goal of the request is to take data from the (Travelers endpoint)[http://restapi.adequateshop.com/api/Traveler/] and store it into a database for later extraction.

## Data

See (their documentation)[https://www.appsloveworld.com/free-online-sample-xml-api-for-testing-purpose/] for details.

The source data is in XML format and contains these fields in each `Travelerinformation` element.

| Field Name  | Type     | Example               |
|-------------|----------|-----------------------|
| id          | int      | 1234                  |
| name        | string   | Jamie Doe             |
| email       | string   | jamie.doe@test.org    |
| address     | string   | USA                   |
| create_date | datetime | YYYY-MM-DDTHH:mm:ss.S |

## Must Haves
Be able to accept repeated data (same IDs) and update any changes that come through from the source data.

Be able to be run on a schedule or on-demand.
