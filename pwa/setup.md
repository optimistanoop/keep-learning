# PWA local setup

To generate cirtificates for local `https` server setup, use :-

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
