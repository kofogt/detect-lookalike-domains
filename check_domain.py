import domain_impersonation_check
import whois21


class validate_domain:
    def add_domain(url="google.com"):
        domains = domain_impersonation_check.lookalikedomain()
        return domains.main(url)

    def whois_check(self, url):
        twisted = self.add_domain(url)
        for fuzzer, domain_list in twisted.items():
            for domain in domain_list:
                print(whois21.WHOIS(domain))


# only show the twisted dns found
testing = validate_domain()
print(testing.whois_check("google.com"))
