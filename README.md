# keep-up

Simple app for tracking keeping up with friends and family

## TODO

Items to plan:

- Flask Endpoints
- HTML templates
- Front-end design

## Database

There are three tables which will be used:

|Table|Description|Relationships|
|--|--|--|
|users|List of all users|Parent to Contacts and Interactions|
|contacts|List of Contacts linked to specific User|Child of Users. Foreign key of Users.id|
|interactions|Logs of interactions between User and Contacts|Child Users. Has foreign keys of Users.id and Contacts.id|

### users

|id|auth_id|email|password|full name|preferred name|
|--|--|--|--|--|--|--|
|`int`|`int`|`string` (unique)|`string`|`string`|`string`|
|1|123|stefanbfritz@gmail.com|hashed_pw|Stefan Fritz|Mac Daddy|


### contacts

|id|User.auth_id|full name|last contacted|contact frequency (days)|
|--|--|--|--|--|
|`int`|`int`|`string`|`datetime`|`int`|
|3|123|Lars Anderson|2020-04-20 13:21:03.234810|30|
|4|123|Brittany Fritz|2020-04-22 16:23:03.134820|5|

### interactions

|id|User.auth_id|Contact.id|timestamp|method of contact|duration (min)|Notes|
|--|--|--|--|--|--|--|
|`int`|`int`|`string`|`datetime`|`string`|`int`|`string`|
|1|123|4|2020-04-22 16:23:03.134820|Duo|22|<ul><li>Played "Let it Go" on ukelele</li><li>next year will be first time working two years at same job</li></ul>|

## API Endpoints

### GET '/login'

- Render template for login page
- Check for 