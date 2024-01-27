#!/bin/bash

# Step 1: Download the Composer Installer
EXPECTED_SIGNATURE="$(wget -q -O - https://composer.github.io/installer.sig)"
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
ACTUAL_SIGNATURE="$(php -r "echo hash_file('SHA384', 'composer-setup.php');")"

# Step 2: Verify the Installer Signature
if [ "$EXPECTED_SIGNATURE" != "$ACTUAL_SIGNATURE" ]
then
    >&2 echo 'ERROR: Invalid installer signature'
    rm composer-setup.php
    exit 1
fi

# Step 3: Run the Installer
php composer-setup.php --quiet
RESULT=$?
rm composer-setup.php

# Step 4: Move Composer to a Global Location
sudo mv composer.phar /usr/local/bin/composer

# Check if Composer installed successfully
if [ $RESULT -eq 0 ]; then
    echo "Composer installed successfully"
else
    echo "Composer installation failed"
    exit 1
fi

# Step 5: Verify Composer Installation
composer --version
