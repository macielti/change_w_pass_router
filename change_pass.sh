curl -i -s -k -X $'POST' \
    -H $"Host: $3" -H $'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0' -H $'Accept: */*' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $"TokenID: $1" -H $'Content-Type: text/plain' -H $'Content-Length: 147' -H $"Origin: http://$3" -H $'Connection: close' -H $"Referer: http://$3/" -H $"Cookie: JSESSIONID=$2" \
    -b $"JSESSIONID=$2" \
    --data-binary $'[LAN_WLAN#1,1,0,0,0,0#0,0,0,0,0,0]0,5\x0d\x0aenable=1\x0d\x0aSSID=TP-Link_E324\x0d\x0aSSIDAdvertisementEnabled=1\x0d\x0aX_TP_PreSharedKey=pwd\x0d\x0a__syncApStatus=1\x0d\x0a' \
    $"http://$3/cgi?2"