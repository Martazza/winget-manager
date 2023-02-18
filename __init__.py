import subprocess

class WingetManager:
    def install(self, package_name):
        """
        Installa il pacchetto specificato utilizzando winget
        """
        subprocess.run(["winget", "install", package_name], check=True)

        
    def install_from_list(self, package_list):
        """
        Installa i pacchetti specificati nella lista utilizzando winget
        """
        for package_name in package_list:
            self.install(package_name)

    def search(self, package_name):
        """
        Esegue una ricerca del pacchetto specificato utilizzando winget
        e restituisce l'output come una stringa
        """
        result = subprocess.run(["winget", "search", package_name], stdout=subprocess.PIPE, check=True)
        return result.stdout.decode()

    def show(self, package_name):
        """
        Mostra le informazioni del pacchetto specificato utilizzando winget
        e restituisce l'output come una stringa
        """
        result = subprocess.run(["winget", "show", package_name], stdout=subprocess.PIPE, check=True)
        return result.stdout.decode()

    def list(self):
        """
        Elencare i pacchetti installati utilizzando winget
        e restituisce l'output come una stringa
        """
        result = subprocess.run(["winget", "list"], stdout=subprocess.PIPE, check=True)
        return result.stdout.decode()
