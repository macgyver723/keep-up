# keep-up

Simple app for tracking keeping up with friends and family

## Database

There are three tables which will be used:

|Table|Description|Relationships|
|--|--|--|
|Users|List of all users|Parent to Contacts and Interactions|
|Contacts|List of Contacts linked to specific User|Child of Users. Foreign key of Users.id|
|Interactions|Logs of interactions between User and Contacts|Child Users. Has foreign keys of Users.id and Contacts.id|

### Users

|id|email|password|full name|preferred name|
|--|--|--|--|--|--|
|`int`|`string` (unique)|`string`|`string`|`string`|
|1|stefanbfritz@gmail.com|hashed_pw|Stefan Fritz|Mac Daddy|


### Contacts

|id|User.id|full name|last contacted|contact frequency (days)|
|--|--|--|--|--|
|`int`|`int`|`string`|`datetime`|`int`|
|3|1|Lars Anderson|2020-04-20 13:21:03.234810|30|
|4|1|Brittany Fritz|2020-04-22 16:23:03.134820|5|

### Interactions

|id|User.id|Contacts.id|timestamp|method of contact|duration (min)|Notes|
|--|--|--|--|--|--|--|
|`int`|`int`|`string`|`datetime`|`string`|`int`|`string`|
|1|1|4|2020-04-22 16:23:03.134820|Duo|22|<ul><li>Played "Let it Go" on ukelele</li><li>next year will be first time working two years at same job</li></ul>|
