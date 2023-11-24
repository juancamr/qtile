import os

package_name = input('Enter the package name: ')
os.system(f'sudo pacman -S {package_name}')
