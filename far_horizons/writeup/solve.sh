strings ../dist/far_horizons.jpg | tail -6 | base64 -d > tmp.zip
unzip tmp.zip > /dev/null
cat f
rm tmp.zip
rm f
