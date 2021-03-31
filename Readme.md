A basic application for recording activities and notes.  
The main function is to allow recording and saving of
activities and notes so that they can later 
be analyzed for (behavioral) patterns.  
The basic unit of data is an activity record which has the following attributes:
* start and end times, as well as total length of activity
* user-defined tags associated with activity such as #work or #movie (there is a way to write definitions for tags in case that helps the user be more consistent/objective in labelling their activities)
    * The tags are meant to be the main thing to be analyzed, 
    so for example one could write a script to visualize how much time they 
    spent playing Bach on the piano after noon in the last month by iterating over the list of all records 
    (it's okay, this is small data) taking each entry that fits in the specified date and time range
    and has the tags #bach and #piano and then using numpy and matplotlib to make a graph of hours per day.
    (This is the way I intend to use it).
* (optional) details about the activity.
* (optional) brief title of activity

Also, can now define 'metatags' which will expand to a given set of tags to save entry time

Credit: App structure based off of https://github.com/jiffygist/TKimer