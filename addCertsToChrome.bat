@echo off
echo adding certs to chrome
certutil -addstore -f "Root" C:\Users\Strahinja\Documents\cp\python\hockey\ca.crt
echo done
::pause