# Configuration for the Self Cloud Machine

## Crontab 
<pre>
@reboot sleep 60 && date >> /home/****/booted/boot_time.txt       
                                                       
#to do                                                                                                                                          
#delete boot_time.txt if size over 1MB or other size,                                                                                           
#but make sure the remain txt file of recent booting time     
</pre>
