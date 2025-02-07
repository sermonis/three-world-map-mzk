#!/usr/bin/env python3


# Python imports
import os
import sys
import shutil
import argparse
# Globals
global pluginVersion
pluginVersion = '0.9.3'


# To install this plugin, refer to ManaZeak wiki (https://github.com/ManaZeak/ManaZeak/wiki)
# ManaZeakPluginIntall script
# Script to install MzkWorldMap into ManaZeak (https://github.com/ManaZeak/ManaZeak)
# It needs either -i (install), -p (pull) or -u (uninstall) flags to manipulate plugin, in addition with
# the ManaZeak 'static/' folder and will copy all MzkWorldMap assets to static/plugins/MzkWorldMap/,
# with static being the given path. This way, it makes all JSON and images available for
# MzkWorldMap Js module without any nginx modification. MzkWorldMap javascript and css
# codes aren't copied, as their bundling is handled in ManaZeak, in the webpack configuration.
# @author Arthur Beaulieu - https://github.com/ArthurBeaulieu


def main():
    print('> ManaZeakPluginInstall for MzkWorldMap - Version {}'.format(pluginVersion))
    # Init argparse arguments
    ap = argparse.ArgumentParser()
    ap.add_argument('staticpath', help='The destination folder to install plugin assets in')
    # Install/Desinstall modes
    ap.add_argument('-i', '--install', help='Install plugin in given path', action='store_true')
    ap.add_argument('-u', '--uninstall', help='Uninstall plugin in given path', action='store_true')
    ap.add_argument('-p', '--pull', help='Update plugin to the latest master commit', action='store_true')
    args = vars(ap.parse_args())
    # Preventing path from missing its trailing slash
    if not args['staticpath'].endswith('/'):
        print('The path \'{}\' is invalid\n> Exiting installer'.format(args['staticpath']))
        sys.exit(-1)
    # Handle install/uninstall plugin
    if args['install']:
        print('Install MzkWorldMap plugin...')
        installPlugin(args['staticpath'])
        print('Installation complete in \'{}plugins/MzkWorldMap/\''.format(args['staticpath']))
    elif args['uninstall']:
        print('Uninstall MzkWorldMap plugin...')
        uninstallPlugin(args['staticpath'])
        print('Uninstallation complete in \'{}\''.format(args['staticpath']))
    elif args['pull']:
        print('Update MzkWorldMap plugin...')
        installPlugin(args['staticpath'])
        print('Update complete in \'{}\''.format(args['staticpath']))
    else:
        print('Missing arguments. See --help')


# Install MzkWorldMap plugin in path
def installPlugin(staticpath):
    # Removing any previous existing
    print('> Remove any previous MzkWorldMap installation')
    removePluginAssets(staticpath)
    # Start assets copy
    print('> Copying MzkWorldMap assets to \'{}\''.format(staticpath))
    addPluginAssets(staticpath)


# Uninstall MzkWorldMap plugin in path
def uninstallPlugin(staticpath):
    # Removing any previous existing
    print('> Remove MzkWorldMap assets in \'{}plugins/MzkWorldMap/\''.format(staticpath))
    removePluginAssets(staticpath)


# Copy MzkWorldMap assets to 'staticpath/plugins/MzkWorldMap'
def addPluginAssets(staticpath):
    try: # Try to copy MzkWorldMap assets directory into argPath/plugins/MzkWorldMap
        shutil.copytree('plugins/MzkWorldMap/assets/', '{}plugins/MzkWorldMap/'.format(staticpath))
    except OSError as error:
        print('{}'.format(error))
        sys.exit(-1)


# Delete folder 'plugins/MzkWorldMap' and all files in path
def removePluginAssets(staticpath):
    # Do not rm 'plugins', as there could be other plugins installed on instance
    if os.path.isdir('{}plugins/MzkWorldMap/'.format(staticpath)):
        shutil.rmtree('{}plugins/MzkWorldMap/'.format(staticpath))


# Script start point
if __name__ == '__main__':
    main()
