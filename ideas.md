# Ideas

Items to plan:
 - Database structure
   - tables to use
 - Flask Endpoints
 - HTML templates
 - Front-end design

# Database

|Table|Description|Relationships|
|--|--|--|
|Users|Contains list of users|Parent table for Interactions|
|Contacts|Contains list of contacts, last contact, desired frequency of contact|Child of Users table, has foreign key of Users.id|
|Interactions|Contains all interaction records. Records user, contact, method, time of contact, duration (if applicable), and notes regarding the interaction (like life updates or things to know about the person)|Child of Users table, has foreign key of User.id and Contacts.id for each entry.|

## Examples

### Users

|ID|username|Full Name|preferred name|email|
|--|--|--|--|--|
|`int`|`string`|`string`|`string`|`string`|
|1|macgyver723|Stefan Fritz|Spudz mackenzie|stefanbfritz@gmail.com|

### Contacts

|ID|Full Name|Last Contacted|Frequency (Days)|
|--|--|--|--|
|`int`|`string`|`datetime`|`int`|
|3|Lars Anderson|2020-04-21 12:54:08.093238|30|

### Interactions

|ID|User ID|Contact ID|Method|timestamp|duration (min)|notes|
|--|--|--|--|--|--|--|
|`int`|`int`|`int`|`string`|`datetime`|`int`|`string`|
|1|1|3|Text|2020-04-21 12:54:08.093238|N/A|Noah got a haircut|
|2|1|4|Phone Call|2020-04-19 14:30:32.283203|14|Job is going well, coworkers are supportive, using Loom to make interpretation videos.

# API Endpoints

#### GET '/users/<user_id>'

- Fetches the user specified and returns summary of most contacted