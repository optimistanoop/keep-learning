# PWA local setup

## To generate self signed cirtificates for local `https` server setup, use :-

      openssl req \
          -newkey rsa:2048 \
          -x509 \
          -nodes \
          -keyout server.key \
          -new \
          -out server.crt \
          -subj /CN=dev.mycompany.com \
          -reqexts SAN \
          -extensions SAN \
          -config <(cat /System/Library/OpenSSL/openssl.cnf \
              <(printf '[SAN]\nsubjectAltName=DNS:dev.mycompany.com')) \
          -sha256 \
          -days 3650

####  Locally self signed cirtificates to be added in server config

####  Locally self signed cirtificates to be trusted in browser as well as in the key-chain access in mac because they are still not trustable cirtificates

####  Self signed cirtificates are only required when your local server is not served through localhost, ex- local.optimistanoop.com

## CORS pluggin in browser

To avoid cors issues in local browser you can use `allow-control-allow-origin:*` chrome plugging
and enable it for use.
Or local server should have config to allow CORS calls as `allow-control-allow-origin:*`


## inportScripts inside service worker file
inportScripts will only work when the service worker file is served form service worker
contex i.e( from base origin, not from routes because files served from routes comes under page context not in sw context)
