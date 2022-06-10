# VidTrimmer
This is a simple **python script** to _trim_ videos into _smaller clips_. It can be used as a tool in *content management* and is pretty *intuitive* and *simple* to use.
The script is cmli-based a GUI may be added in later versions.


As soon as the main script runs it prompts the user for the path to the directory where the unprocessed videos are located. 
The script also prompts the user for a duration. That value is stored as in integer in the timeset variable and all the processed video will have that value as maximum length.

These values are then passed to the findandtrim function. The output clips will be located in the script folder. That behavior can be easily modified in future versions. 

Some useful information are tracked all along and are kept in a log file.
