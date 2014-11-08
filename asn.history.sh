#!/bin/bash

GOVASNIN="government.ASNs.csv.bkp"
GOVASNOUT="government.ASNs.csv"

while read -r line; do
	ASNONLY=$(echo $line | cut -d, -f1)
	HIST=$(whois -h whois.ripe.net -- "--show-version 1 $ASNONLY" | awk '/UPDATE/ {print $9}')
	echo "$line,$HIST" >> $GOVASNOUT 
done <${GOVASNIN}
