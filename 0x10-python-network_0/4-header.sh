#!/bin/bash
# A script to send custom headers to the servers
curl -s -H "X-School-User-Id: 98" "$1"
