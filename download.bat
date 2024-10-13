@echo off
echo Downloading %1
yt-dlp --socket-timeout 60 -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best %1
echo Downloading %1 completed
pause