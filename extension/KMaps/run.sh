sqlite3 /var/local/appreg.db "INSERT INTO handlerIds VALUES ('com.aranwe.kmaps')"
sqlite3 /var/local/appreg.db "INSERT INTO properties (handlerId, name, value) VALUES ('com.aranwe.kmaps','command','/usr/bin/wafapp -l com.aranwe.kmaps -c /mnt/us/extensions/KMaps/kmaps/')"
sqlite3 /var/local/appreg.db "INSERT INTO properties (handlerId, name, value) VALUES ('com.aranwe.kmaps','unloadPolicy','unloadOnPause');"

lipc-set-prop com.lab126.appmgrd start app://com.aranwe.kmaps
