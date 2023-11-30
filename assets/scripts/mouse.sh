#!/bin/bash

# ID del dispositivo (puedes encontrarlo ejecutando 'xinput list')
DEVICE_ID="14"

# Verifica si el dispositivo está habilitado o deshabilitado
if xinput list-props "$DEVICE_ID" | grep "Device Enabled (.*):.*1" &>/dev/null; then
	# El dispositivo está habilitado, deshabilítalo
	xinput disable "$DEVICE_ID"
	unclutter &
	echo "Mouse disabled"
else
	# El dispositivo está deshabilitado, habilítalo
	xinput enable "$DEVICE_ID"
	pkill unclutter
	echo "Mouse enabled"
fi
