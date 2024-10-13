@echo off
echo adding certs to chrome
certutil -addstore -f "Root" %1
echo done
::pause