# Nextcloud_Elasticsearch
Store The Nextcloud Usage Statistics (Monitoring) to ElasticSearch 

Nextcloud usage statistics can be found in their web UI, by Admin->Settings->System. In that page bottom you can find the External monitoring tool URL. It will give you a more compenhensive Nextcloud usage data (including CPU/RAM/Disk utilitization). The output can be in JSON format and it makes sense if you already have your ElasticSearch instance to store this data. Here is a sample Python program (shell script can do the same thing too) to insert the output to Elasticsearch.

A cron job like this so you can store the data for future usage analysis
    01 10,14,18,22 * * * /usr/bin/python3 <insert.py path> 
