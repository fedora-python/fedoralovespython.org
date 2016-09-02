#!/bin/bash -eu
curl -X DELETE "https://api.cloudflare.com/client/v4/zones/$CLOUDFLARE_ZONE/purge_cache" \
-H "X-Auth-Email: $CLOUDFLARE_EMAIL" \
-H "X-Auth-Key: $CLOUDFLARE_AUTHKEY" \
-H "Content-Type: application/json" \
--data '{"purge_everything":true}'
