try:
    import os, sys, fnmatch
except ImportError:
    print '[+] Required modules missing.\n[+]Please install the required modules and try again.'
    sys.exit(0)

def banner():
    print '''###################################################################################
# Module:   OpenVAS LSC NVTs Remover
# Purpose:  Faster rebuilding of OpenVAS NVT Plugin caches
# Date:     27th April 2013
# Author:   Sujit Ghosal
# Email:    x13.x37@gmail.com
# Blog:     http://wikisecure.net/
# 
# NOTE:     Use this script ONLY if you dont need to make use of Local Security Checks (LSC)!
##################################################################################\n'''

def lscFiles():
    default_dir = os.getcwd()
    pluginsDir = '/var/lib/openvas/plugins/'

    if os.path.exists(pluginsDir) is True:
        if os.path.isfile(pluginsDir + 'version_func.inc') is True:
            print '[+] Valid plugins directory found!'
            pass
    else:
        print '[+] Please provide a valid OpenVAS NVT Plugins directory!'
        sys.exit(0)

    # Grep all the nasl and asc files
    criterias = ['esoft_slk_ssa_*.nasl', 'esoft_slk_ssa_*.nasl.asc', \
                 'fcore_200*.nasl', 'fcore_200*.nasl', \
                 'freebsd_*.nasl', 'freebsd_*.nasl.asc', \
                 'gb_CESA-20*.nasl', 'gb_CESA-20*.nasl.asc', \
                 'gb_fedora_20*.nasl', 'gb_fedora_20*.nasl.asc', \
                 'gb_hp_ux_HP*.nasl', 'gb_hp_ux_HP*.nasl.asc', \
                 'gb_mandriva_MDKA_20*.nasl', 'gb_mandriva_MDKA_20*.nasl.asc', \
                 'gb_mandriva_MDKSA_20*.nasl', 'gb_mandriva_MDKSA_20*.nasl.asc', \
                 'gb_mandriva_MDVA_20*.nasl', 'gb_mandriva_MDVA_20*.nasl.asc', \
                 'gb_mandriva_MDVSA_20*.nasl', 'gb_mandriva_MDVSA_20*.nasl.asc', \
                 'gb_RHSA-20*.nasl', 'gb_RHSA-20*.nasl.asc', \
                 'gb_solaris_1*.nasl', 'gb_solaris_1*.nasl.asc', \
                 'gb_suse_20*.nasl', 'gb_suse_20*.nasl.asc', \
                 'gb_ubuntu_USN_*.nasl', 'gb_ubuntu_USN_*.nasl.asc', \
                 'gb_VMSA-20*.nasl', 'gb_VMSA-20*.nasl.asc', \
                 'glsa_20*.nasl', 'glsa_20*.nasl.asc', \
                 'mdksa_200*.nasl', 'mdksa_200*.nasl.asc', \
                 'ovcesa20*.nasl', 'ovcesa20*.nasl.asc', \
                 'RHSA_20*.nasl', 'RHSA_20*.nasl.asc', \
                 'sles1_*.nasl', 'sles1_*.nasl.asc', \
                 'sles9p*.nasl', 'sles9p*.nasl.asc', \
                 'suse_sa_20*.nasl', 'suse_sa_20*.nasl.asc', \
                 'suse_sr_20*.nasl', 'suse_sr_20*.nasl.asc', \
                 'ubuntu_6*.nasl', 'ubuntu_6*.nasl.asc', \
                 'ubuntu_7*.nasl', 'ubuntu_7*.nasl.asc', \
                 'ubuntu_8*.nasl', 'ubuntu_8*.nasl.asc', \
                 'ubuntu_9*.nasl', 'ubuntu_9*.nasl.asc', \
                 'deb_*.nasl', 'deb_*.nasl.asc']

    files = os.chdir(pluginsDir)
    files = os.listdir('.')
    filesToRemove = []
    for i in criterias:
        found = fnmatch.filter(files, i)
        for eachFile in found:
            filesToRemove.append(eachFile)

    filesToRemove = (set(list(filesToRemove)))
    filesToRemove = sorted(filesToRemove)

    if len(filesToRemove) == 0:
        print '[+] No LSC based checks found as per the wildcard search criteria!'
        sys.exit(0)
    elif len(filesToRemove) > 0:
        print '[+] Number of NVTs to delete:', len(filesToRemove)

    try:
        for delFile in filesToRemove:
            os.remove(delFile)
    except:
        print '[+] Couldn\'t delete the file\(s\), may be due to directory permission error.'
        sys.exit(0)

    print '[+] All OpenVAS LSC based NVTs deleted successfully!'
    print '[+] Please rebuild the NVT cache by the following command: #openvasmd --rebuild'

if __name__ == "__main__":
    if len(sys.argv) == 1:
        banner() ; lscFiles()
    else:
        print '[+]Error: Invalid number of arguments passed.'
        print '[+]Usage: #python lsc_remover.py'
