#!/bin/bash
# Docker HUB user and image name
dh_username=ministrbob
dh_image_name=short-urls

echo -e "\n==> datetime now"
date

set -o pipefail
echo -e "\n==> docker stop $dh_image_name"
docker stop $dh_image_name
echo -e "\n==> docker rm $dh_image_name"
docker rm $dh_image_name

set +o pipefail
echo -e "\n==> docker pull image"
docker pull $dh_username/$dh_image_name:latest
echo -e "\n==> docker run"
docker run --name $dh_image_name --restart=always --net=gs_network --user 1006:1006 -d -v /home/$dh_image_name/.settings:/app/short_urls/settings.py -v /home/$dh_image_name/short_urls.sqlite3:/app/short_urls.sqlite3 $dh_username/$dh_image_name:latest
echo -e "\n==> Container info"
docker ps --filter "name=$dh_image_name"
echo -e "\n==> Container Image SHA256"
docker inspect --format='{{.Image}}' $dh_image_name
echo -e "\n==> Image SHA256"
docker image inspect --format='{{.Id}}' $dh_username/$dh_image_name:latest
echo -e "\n==> Docker HUB RepoDigests SHA256"
docker image inspect --format='{{index .RepoDigests 0}}' $dh_username/$dh_image_name:latest
