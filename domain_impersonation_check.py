import operator


class lookalikedomain():

    def find_all(self,url, unique):
        start = 0
        while True:
            start = unique.find(url, start)
            if start == -1:
                return
            yield start
            start += len(url)


    def get_suffix():
        suffixes = [
            ("-shop"),
            ("-login"),
            ("-logon"),
            ("-secure"),
            ("-website"),
            ("-finance"),
            ("-domain"),
            ("-health"),
            ("-news"),
            ("-security"),
        ]
        return suffixes


    def get_prefixes():
        prefixes = [
            ("my-"),
            ("thedaily-"),
            ("go-"),
            ("cyber-"),
            ("travel-logon-"),
            ("login-"),
        ]
        return prefixes


    def get_tld():
        list = [
            (f"com"),
            # (f'co'),
            # (f'cm'),
            (f"net"),
            (f"edu"),
            # (f'org'),
            # (f'io'),
            # (f'biz'),
            # (f'company'),
            # (f'sa'),
            # (f'co.uk'),
            # (f'app'),
            # (f'xyz'),
            # (f'gov'),
        ]
        return list


    def get_replacers():
        replacers = [
            ("ijarah", "ijarahfinance"),
            ("rn", "m"),
            ("l", "t"),
            ("r", "i"),
            ("n", "m"),
            ("d", "cl"),
            ("vv", "w"),
            ("l", "i"),
            ("j", "i"),
            ("l", "1"),
            ("o", "c"),
            ("u", "v"),
            ("nn", "m"),
            ("a", "e"),
            ("a", "o"),
            ("a", "u"),
            ("i", "l"),
            ("j", "i"),
            ("r", "n"),
            ("h", "k"),
            ("s", "ss"),
            ("u", "v"),
            ("e", "o"),
        ]
        return replacers

    def generate_alternative_tlds(self, domain, naked):

        domains = []

        alt_tlds = self.get_tld()

        for alts in alt_tlds:
            domains.append((f"{naked}.{alts}"))

        return domains

    def generate_with_suffixes(self, domain, naked):
        domains = []
        tld = self.get_tld()
        suffixes = self.get_suffix()

        for suffix in suffixes:
            for tl in tld:
                alt = f"{naked}{suffix}.{tl}"
                domains.append((alt))

        prefixes = self.get_prefixes()

        for prefix in prefixes:
            for tl in tld:
                alt = f"{prefix}{naked}.{tl}"
                domains.append((alt))

        return domains

    @staticmethod
    def check_availability(domain):
        return True

    def generate_homoglyphs(self, domain, naked):

        replacers = self.get_replacers()

        domains = []
        replacements = []
        tlds = self.get_tld()
        for search, replace in replacers:
            for pos in list(self.find_all(search, naked)):
                replacements.append((search, replace, pos))
            for pos in list(self.find_all(replace, naked)):
                replacements.append((replace, search, pos))

        for find, replace, pos in replacements:
            for tl in tlds:
                candidate = naked[:pos] + replace + naked[pos + len(find) :]
                domains.append((f"{candidate}.{tl}"))

        return domains

    def generate_omission(self, naked, domain):
        domain = []
        tld = self.get_tld()
        count = 1
        for ommission in naked:
            for tl in tld:
                if count < len(naked):
                    naked_url = naked[count:]
                    domain.append((f"{naked_url}.{tl}"))
                    count = count + 1
        return domain

    def main(self, domain):
        naked, _, tld = domain.rpartition(".")

        selectors = {
            "alttlds": self.generate_alternative_tlds(domain, naked),
            "homoglyphs": self.generate_homoglyphs(domain, naked),
            "suffixes": self.generate_with_suffixes(domain, naked),
            "ommission": self.generate_omission(domain, naked),
        }

        return selectors


test = lookalikedomain()
