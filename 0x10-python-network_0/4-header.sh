#!/bin/bash
# A script to send custom headers to the servers
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
